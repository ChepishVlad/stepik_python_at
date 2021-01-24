# -*- coding: utf-8 -*-
from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser=browser, url=LINK)
    page.open()
    page.go_to_login_page()
