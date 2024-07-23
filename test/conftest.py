import os

import allure
import pytest


from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import BaseWebDriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.join(BASE_DIR, "resources")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        help="Browser for running tests",
        choices=["firefox", "chrome"],
        default="chrome"
    )
    parser.addoption(
        "--browser_version",
        help="Browser version",
        default="100.0"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    screenshot_source = None
    for fixture_name in node.fixturenames:
        if fixture_name in node.funcargs.keys():
            fixture = node.funcargs[fixture_name]
            if isinstance(fixture, BaseWebDriver):
                screenshot_source = fixture
                break

    if screenshot_source:
        png = screenshot_source.get_screenshot_as_png()
        allure.attach(
            png,
            name='screenshot on failure',
            attachment_type=AttachmentType.PNG
        )

    yield
   # web_driver.get_screenshot_as_file("/home/rattus-aristarchus/code/python/stackoverflow/generic_report/screenshots/on_failure.png")

