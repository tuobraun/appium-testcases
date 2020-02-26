import pytest


def test_dashboard_loaded(mainfixture):
    mainfixture.dash.dashboard_loaded()

def test_start_audit(mainfixture):
    mainfixture.dash.open_section(name='Start New')

def test_pass_audit(mainfixture):
    mainfixture.audit.choose_audit(audit='Wawa Food Safety and Defense Audit')
    mainfixture.audit.choose_supplier()
    mainfixture.audit.select_topic(topic='General Information')
    mainfixture.audit.pass_general_info_checklist()
    mainfixture.audit.select_topic(topic='Management Commitment')
    mainfixture.audit.pass_radiobutton_cheklists()
