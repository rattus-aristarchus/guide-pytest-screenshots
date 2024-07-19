import allure
from allure_commons.types import Severity
from selenium.webdriver.common.by import By


@allure.severity(severity_level=Severity.CRITICAL)
@allure.label("owner", 'lankinma')
@allure.feature("Software testing wiki page")
@allure.title("Page should have a word in the title")
def test_main_page_title_should_have_word_in_title(driver):
    with allure.step("Open the main page"):
        driver.get("https://en.wikipedia.org/wiki/Software_testing")
        attach_screenshot(driver)

    with allure.step("Look for a phrase in the title"):
        assert "Bad search" in driver.title


@allure.severity(severity_level=Severity.CRITICAL)
@allure.label("owner", 'lankinma')
@allure.feature("Software testing wiki page")
@allure.title("Page should have a text entry element")
def test_main_page_should_have_text_entry(driver):
    with allure.step("Open the main page"):
        driver.get("https://en.wikipedia.org/wiki/Software_testing")

    with allure.step("Find an element on the page"):
        elem = driver.find_element(By.ID, "searchInput")
        assert elem is not None


def attach_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )


def attach_element_screenshot(element):
    element.screenshot("screenshots/element_screenshot.png")
    allure.attach.file(
        "screenshots/element_screenshot.png",
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )
