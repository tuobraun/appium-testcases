import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class AuditScreenAndroid:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        pckgnm = 'com.icertainty.forms:id/'

        self.audit_list = ['Dairy Pre-Op Audit (BIB)', 'Dairy Pre-Op Audit (FED 1)', 'Dairy Pre-Op Audit (FED 3)', 'Dairy Pre-Op Audit (FED 4)', 'Dairy Pre-Op Audit (FED 5)', '	Dairy Pre-Op Audit (NEP)', 'Key Partner Audit', 'QA Bi-Weekly Dairy GMP Audit', 'QA Monthly Warehouse GMP Audit', 'Supply Chain QA Operational GMP Audit', 'Wawa Food Safety and Defense Audit']
        self.vendor_audit = 'Wawa Food Safety and Defense Audit'
        self.bib_audit = 'Dairy Pre-Op Audit (BIB)'
        self.topic_list = ['Management Commitment', 'Audit Programs', 'Sanitation', 'Pathogen Environmental Monitoring', 'Analytical & Sensory Evaluation', 'Equipment', 'SOPs', 'Water Testing', 'Allergen Control', 'Foreign Object Control', 'Recall & Traceability', 'HARPC/HACCP', 'Training', 'Food Defense', 'Shipping & Receiving', 'Storage', 'Production Area', 'Employees', 'Housekeeping', 'Chemicals', 'Facility', 'Water & Sewage', 'Foreign Object Control', 'Pest Evidence', 'Allergen Control', 'Outside Facility', 'switching to Suppliers Topic']
        self.supplier_list = ['Alamance Foods - Burlington, NC', 'Alderfer/Leidy\'s - Harleysville']
        self.general_info_topic = 'General Information'
        self.general_info_list = ['Facility Manager Contact', 'Quality Assurance Contact', 'Default user for Corrective Actions', 'Products Produced', 'Products Produced for Wawa', 'Process Narrative', 'Hours of Operation', 'Facility Regulatory Authority', 'Off-Site Storage Facilities', 'Transportation & Distribution by', 'Size and Age of Facility', 'History of Company', 'Additional Facilities', 'R&D Facility']

        self.search_clear = (MobileBy.ID, pckgnm+'ListFragment_CancelSearchButton')
        #CHECKLIST NAVIGATION CONTROLS
        self.prev_arrow = pckgnm+"DetailsFragment_PrevButton"
        self.next_arrow = pckgnm+"DetailsFragment_NextButton"
        self.select_arrow = pckgnm+"DetailsFragment_WizardSelectItem"
        #DetailsFragment_TitlePanel
        self.topic_title = pckgnm+"DetailsFragment_Title"
        self.text_title = pckgnm+"DetailsGroupView_Title"
        self.comment_box = pckgnm+"DetailsEditTextItemView_Value"
        self.save_n_close = pckgnm+"DetailsButtonItemView_Button" #Also Unselect
        self.button_class = "android.widget.Button"
        self.audit_icon_class = "android.widget.ImageView"
        self.menu_frame_class = "android.widget.FrameLayout"
        self.items_view = pckgnm+"DetailsValueItemView_AccessoryImage"
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
        self.ca_comment = "Test Corrective Action"

        self.filter_incomplete = "Incomplete"
        self.filter_required = "Required"
        self.filter_all = "All"

        #DASHBOARD, PANNEL, LISTVIEWS
        self.dashboard_rght_btn = pckgnm+"HeaderPanelView_RightButton2"
        self.dashboard_header = pckgnm+"HeaderPanelView_Title"
        self.back_arrow = pckgnm+"HeaderPanelView_BackButton"

    def choose_audit(self, audit):
        self.wait.until(EC.presence_of_element_located(self.search_clear))
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("'+audit+'").instance(0))').click()
        #driver.find_element_by_android_uiautomator('new UiSelector().text("{}")').format(vendor_audit)
        print("Choosing: "+audit)

    def choose_supplier(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.audit_icon_class)))
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Suppliers")').click()
        self.wait.until(EC.presence_of_element_located((MobileBy.ID, self.items_view))).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.supplier_list[0]+'")').click()
        self.wait.until(EC.presence_of_element_located((MobileBy.ID, self.save_n_close))).click()
        print('Supplier chosen')

    def select_topic(self, topic):
        self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.audit_icon_class)))
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+topic+'")').click()

    def apply_ca(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.no+'")').click()
        self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.text_box_class))).send_keys('Test Corrective Action')
        save_ca = self.driver.find_elements_by_class_name(self.button_class) #Save button
        save_ca[1].click()
        self.wait.until(EC.text_to_be_present_in_element((MobileBy.ID, self.dashboard_header), "Answered:"))
        time.sleep(1)
        score_print = self.driver.find_element_by_id(self.dashboard_header)
        print("Corrective Action applied")
        print(score_print.text)

    def pass_radiobutton_cheklists(self):
        while True:
            try:
                topic_title_print = self.driver.find_element_by_id(self.topic_title).text
                print (f'- {topic_title_print}')
                # Apply Answer
                self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.dashboard_rght_btn))).click()
                self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.menu_frame_class)))
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.apply_default+'")').click()
                self.wait.until(EC.text_to_be_present_in_element((MobileBy.ID, self.dashboard_header), "Score: 100%"))
                score_print = self.driver.find_element_by_id(self.dashboard_header)
                print(score_print.text)

                # Apply CA
                self.apply_ca()

                # Go to next Topic
                self.driver.find_element_by_id(self.next_arrow).click()
            except NoSuchElementException:
                self.wait.until(EC.presence_of_element_located((MobileBy.ID, self.back_arrow))).click()
                time.sleep(2)
                break

    def populate_text_fields(self, text):
        self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.text_box_class)))
        text_field = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("'+text+'").instance(0))')
        self.wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, self.text_box_class))).send_keys(text_field.text)
        print(text_field.text+" field populated")

    def pass_general_info_checklist(self):
        # Populate text fields
        general_info = self.general_info_list
        [self.populate_text_fields(text) for text in general_info]
        
        # Populate radiobutton questions
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Yes").instance(0))').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Save and Close").instance(0))').click()
