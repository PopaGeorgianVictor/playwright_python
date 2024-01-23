# code genereate with codegen
# run  playwright codegen https://www.saucedemo.com/v1/

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()
    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")
