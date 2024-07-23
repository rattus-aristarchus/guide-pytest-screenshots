import allure
from allure_commons.types import Severity


@allure.severity(severity_level=Severity.CRITICAL)
@allure.label("owner", 'lankinma')
@allure.feature("Software testing wiki page")
@allure.title("Page should have a word in the title")
def test_main_page_title_should_have_word_in_title(context):
    with allure.step("Open the main page"):
        context.goto("https://en.wikipedia.org/wiki/Software_testing")

    with allure.step("Look for a phrase in the title"):
        assert "Bad search" in context.title()


@allure.severity(severity_level=Severity.CRITICAL)
@allure.label("owner", 'lankinma')
@allure.feature("Software testing wiki page")
@allure.title("Page should have a text entry element")
def test_main_page_should_have_text_entry(context):
    with allure.step("Open the main page"):
        context.goto("https://en.wikipedia.org/wiki/Software_testing")

    with allure.step("Find an element on the page"):
        elem = context.get_by_role("search")
        assert elem is not None
