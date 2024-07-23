import os

import allure
import pytest

from playwright.async_api import Page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.join(BASE_DIR, "resources")


@pytest.fixture
def custom_page(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    page = None

    # find the fixture that provides a page
    for fixture_name in node.fixturenames:
        if fixture_name in node.funcargs.keys():
            fixture = node.funcargs[fixture_name]
            if isinstance(fixture, Page):
                page = fixture
                break

    if page:
        attach_screenshot(page)

    yield


def attach_screenshot(page):
    screenshot_bytes = page.screenshot()
    allure.attach(
        screenshot_bytes,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )


def attach_element_screenshot(elem):
    screenshot_bytes = elem.screenshot()
    allure.attach(
        screenshot_bytes,
        name="element",
        attachment_type=allure.attachment_type.PNG
    )


