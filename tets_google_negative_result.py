from selene.support.shared import browser
from selene import have


import pytest


@pytest.fixture()
def configure_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def open_browser():
    browser.open('https://google.com/ncr')


def test_google_dont_find_javascript(configure_browser, open_browser):
    browser.element('[name="q"]').type('ueryuywiergggggggy333').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))

