from playwright.sync_api import Page
import pytest


# run in multiple browser in the same time use pytest --browser chromium --browser firefox
# run in real browser pytest --browser-channel (specified browser)
# trace test pytest  --tracing on ; to view file run :  playwright show-trace (directory/name of the file)

def test_title(page:  Page):
    page.goto('https://www.saucedemo.com')
    # page.goto('/')  pytest --headed --base-url https://www.saucedemo.com
    assert page.title() == 'Swag Labs'

def test_inventory(page: Page):
    page.goto('https://www.saucedemo.com/inventory.html') # page.goto('/inventory.html')
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."



