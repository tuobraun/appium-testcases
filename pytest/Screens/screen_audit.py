import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class AuditScreenAndroid:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        self.audit_list = ('Dairy Pre-Op Audit (BIB)', 'Dairy Pre-Op Audit (FED 1)', 'Dairy Pre-Op Audit (FED 3)', 'Dairy Pre-Op Audit (FED 4)', 'Dairy Pre-Op Audit (FED 5)', '	Dairy Pre-Op Audit (NEP)', 'Key Partner Audit', 'QA Bi-Weekly Dairy GMP Audit', 'QA Monthly Warehouse GMP Audit', 'Supply Chain QA Operational GMP Audit', 'Wawa Food Safety and Defense Audit')
        self.topic_list = ('Management Commitment', 'Audit Programs', 'Sanitation', 'Pathogen Environmental Monitoring', 'Analytical & Sensory Evaluation', 'Equipment', 'SOPs', 'Water Testing', 'Allergen Control', 'Foreign Object Control', 'Recall & Traceability', 'HARPC/HACCP', 'Training', 'Food Defense', 'Shipping & Receiving', 'Storage', 'Production Area', 'Employees', 'Housekeeping', 'Chemicals', 'Facility', 'Water & Sewage', 'Foreign Object Control', 'Pest Evidence', 'Allergen Control', 'Outside Facility', 'switching to Suppliers Topic')
        self.supplier_list = ('Alamance Foods - Burlington, NC', 'Alderfer/Leidy\'s - Harleysville')
        self.general_info_list = ('Facility Manager Contact', 'Quality Assurance Contact', 'Default user for Corrective Actions', 'Products Produced', 'Products Produced for Wawa', 'Process Narrative', 'Hours of Operation', 'Facility Regulatory Authority', 'Off-Site Storage Facilities', 'Transportation & Distribution by', 'Size and Age of Facility', 'History of Company', 'Additional Facilities', 'R&D Facility')

        self.search_clear = (MobileBy.ID, 'ListFragment_CancelSearchButton')
        #CHECKLIST NAVIGATION CONTROLS
        self.search_box = (MobileBy.ID, 'ListFragment_Keywords')
        self.prev_arrow = (MobileBy.ID, 'DetailsFragment_PrevButton')
        self.next_arrow = (MobileBy.ID, 'DetailsFragment_NextButton')
        self.select_arrow = (MobileBy.ID, 'DetailsFragment_WizardSelectItem')
        #DetailsFragment_TitlePanel
        self.topic_title = (MobileBy.ID, 'DetailsFragment_Title')
        self.text_title = (MobileBy.ID, 'DetailsGroupView_Title')
        self.comment_box = (MobileBy.ID, 'DetailsEditTextItemView_Value')
        self.save_n_close = (MobileBy.ID, 'DetailsButtonItemView_Button') #Also Unselect
        self.button_class = "android.widget.Button"
        self.audit_icon_class = "android.widget.ImageView"
        self.menu_frame_class = "android.widget.FrameLayout"
        self.items_view = (MobileBy.ID, 'DetailsValueItemView_AccessoryImage')
        self.question_text_class = "android.widget.TextView"
        self.text_box_class = "android.widget.EditText"

        #List of topics:
        self.suppliers = "Suppliers"
        self.general_info = "General Information"
        self.management_commit = "Management Commitment"
        self.audit_programs = "Audit Programs"

        #Possible Answers:
        self.yes = "Yes"
        self.no = "No"
        self.pas = "Pass"
        self.fail = "Fail"
        self.apply_default = "Apply Default Answers"
        self.answer_all = "Answer All"
        self.answer_empty = "Answer Empty"

        self.filter_incomplete = "Incomplete"
        self.filter_required = "Required"
        self.filter_all = "All"

        #DASHBOARD, PANNEL, LISTVIEWS
        self.dashboard_rght_btn = (MobileBy.ID, 'HeaderPanelView_RightButton2')
        self.dashboard_header = (MobileBy.ID, 'HeaderPanelView_Title')
        self.back_arrow = (MobileBy.ID, 'HeaderPanelView_BackButton')

    def search_audit(self, audit):
        self.app.wait_element(self.search_box).click()
        self.app.wait_element(self.search_box).send_keys(audit)
        self.driver.keyevent(66)
        self.app.find_element(self.search_clear).click()

    def choose_audit(self, audit):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("'+audit+'").instance(0))').click()
        print(f'Choosing: {audit}')

    def choose_supplier(self):
        self.app.wait_element((MobileBy.CLASS_NAME, self.audit_icon_class))
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Suppliers")').click()
        self.app.wait_element(self.items_view).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.supplier_list[0]+'")').click()
        self.app.wait_element(self.save_n_close).click()
        print('Supplier chosen')

    def select_topic(self, topic):
        self.app.wait_element((MobileBy.CLASS_NAME, self.audit_icon_class))
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+topic+'")').click()
        print(f'Topic selected: - {topic}')

    def apply_ca(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.no+'")').click()
        self.app.wait_element((MobileBy.CLASS_NAME, self.text_box_class)).send_keys('Test Corrective Action')
        save_ca = self.driver.find_elements_by_class_name(self.button_class) #Save button
        save_ca[1].click()
        self.wait.until(EC.text_to_be_present_in_element(self.dashboard_header, "Answered:"))
        time.sleep(1)
        score_print = self.app.find_element(self.dashboard_header)
        print('Corrective Action applied')
        print(score_print.text)

    def pass_radiobutton_cheklists(self):
        while True:
            try:
                topic_title_print = self.app.find_element(self.topic_title).text
                print (f'- {topic_title_print}')
                # Apply Answer
                self.wait.until(EC.element_to_be_clickable(self.dashboard_rght_btn)).click()
                self.app.wait_element((MobileBy.CLASS_NAME, self.menu_frame_class))
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.apply_default+'")').click()
                self.wait.until(EC.text_to_be_present_in_element(self.dashboard_header, "Score: 100%"))
                score_print = self.app.find_element(self.dashboard_header)
                print(score_print.text)

                # Apply CA
                self.apply_ca()

                # Go to next Topic
                self.app.find_element(self.next_arrow).click()
            except NoSuchElementException:
                self.app.wait_element(self.back_arrow).click()
                time.sleep(2)
                break

    def populate_text_fields(self, text):
        self.app.wait_element((MobileBy.CLASS_NAME, self.text_box_class))
        text_field = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("'+text+'").instance(0))')
        self.app.wait_element((MobileBy.CLASS_NAME, self.text_box_class)).send_keys(text_field.text)
        print(text_field.text+" field populated")

    def pass_general_info_checklist(self):
        # Populate text fields
        general_info = self.general_info_list
        [self.populate_text_fields(text) for text in general_info]
        
        # Populate radiobutton questions
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Yes").instance(0))').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Save and Close").instance(0))').click()


class AuditScreenIOs(AuditScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        self.dashboard_rght_btn = (MobileBy.ACCESSIBILITY_ID, '...')
        self.back_arrow = (MobileBy.ACCESSIBILITY_ID, 'LeftArrow')
        self.filter_icon = (MobileBy.ACCESSIBILITY_ID, 'bit dark filter')
        self.login_screen_clear = (MobileBy.ACCESSIBILITY_ID, 'Clear text')

        self.prev_arrow = (MobileBy.ACCESSIBILITY_ID, 'BlueLeftArrow')
        self.next_arrow = (MobileBy.ACCESSIBILITY_ID, 'BlueRightArrow')
        self.more_inf = (MobileBy.ACCESSIBILITY_ID, 'More Info')
        self.save_n_close = (MobileBy.ACCESSIBILITY_ID, 'Save and Close')
        self.unselect = (MobileBy.ACCESSIBILITY_ID, 'Unselect')
        self.apply_default = (MobileBy.ACCESSIBILITY_ID, 'Apply Default Answers')
        self.answer_all = (MobileBy.ACCESSIBILITY_ID, 'Answer All')
        self.answer_empty = (MobileBy.ACCESSIBILITY_ID, 'Answer Empty')

        self.text_box_class = (MobileBy.ACCESSIBILITY_ID, 'MultiLineTextItemCell:0:1')
        self.text_box_xpath = (MobileBy.XPATH, '//XCUIElementTypeCell[@name="MultiLineTextItemCell:0:0"]/XCUIElementTypeTextView')

    def filter_list(self, filter_name):
        self.app.wait_element(self.filter_icon).click()
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, filter_name)).click()

    def search_audit(self, audit):
        self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeSearchField"').click()
        self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeImage"').send_keys(audit)
        self.driver.find_element_by_accessibility_id('Search').click()
        self.app.wait_element(self.login_screen_clear).click()
    
    def choose_audit(self, audit):
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, audit)).click()
        print(f'Choosing: {audit}')

    def scroll_n_choose_audit(self, audit):
        scroll_table = self.app.find_element((MobileBy.XPATH, '//XCUIElementTypeApplication[@name=\"IC Forms\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable')) # For iPhone only
        self.driver.execute_script("mobile: scroll", {"direction": "down", "element": scroll_table, "predicateString": "label == 'Wawa Food Safety and Defense Audit' AND visible == 1"}) # For iPhone only
        self.app.find_element((MobileBy.ACCESSIBILITY_ID, audit)).click()
        print(f'Choosing: {audit}')

    def choose_supplier(self):
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, 'Suppliers')).click()
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, 'Selected')).click()
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, self.supplier_list[0])).click()
        self.app.wait_element(self.save_n_close).click()
        print('Supplier chosen')

    def select_topic(self, topic):
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, topic)).click()
        print(f'Topic selected: - {topic}')

    def apply_ca(self):
        self.app.wait_element((MobileBy.ID, 'No')).click()
        self.app.wait_element(self.text_box_class).click() #In case a Simulator runs very slow... :(
        self.app.wait_element(self.text_box_class).send_keys('Test Corrective Action')
        self.app.wait_element(self.save_n_close).click()
        self.app.wait_element(self.filter_icon)
        print('Corrective Action applied')

    def pass_radiobutton_cheklists(self):
        while True:
            try:
                #topic_title_print = self.driver.find_element_by_id(self.topic_title).text
                #print (f'- {topic_title_print}')
                
                # Apply Answer
                self.app.wait_element(self.dashboard_rght_btn).click()
                self.app.wait_element(self.apply_default).click()
                self.app.wait_element(self.filter_icon)

                # Apply CA
                self.apply_ca()

                # Go to next Topic
                self.app.find_element(self.next_arrow).click()
            except NoSuchElementException:
                self.app.wait_element(self.back_arrow).click()
                time.sleep(2)
                break
