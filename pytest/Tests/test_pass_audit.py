import pytest
import allure


@allure.title('Dashboard can be loaded')
def test_dashboard_loaded(mainfixture):
    mainfixture.dash.dashboard_loaded()

@allure.title('Audit can be started')
def test_start_audit(mainfixture):
    mainfixture.dash.open_section(name='Start New')

@allure.title('Audit can be passed')
def test_pass_audit(mainfixture):
    mainfixture.audit.choose_audit(audit='Wawa Food Safety and Defense Audit')
    mainfixture.audit.choose_supplier()
    #mainfixture.audit.select_topic(topic='General Information') #In Progress
    #mainfixture.audit.pass_general_info_checklist() #In Progress
    mainfixture.audit.select_topic(topic='Management Commitment')
    mainfixture.audit.pass_radiobutton_cheklists()
