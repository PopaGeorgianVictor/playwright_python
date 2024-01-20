from playwright.sync_api import sync_playwright

'''' The Sync API takes care of syncing your Contentstack data with
your application and ensures that the data is always up-to-date by providing delta updates'''

# playwright = sync_playwright().start()

with sync_playwright() as playwright:
    # launch browser and stay open for 2 sec
    browser = playwright.chromium.launch(headless=False, slow_mo = 2000)
    # create a new page
    page = browser.new_page()
    page.goto('https://playwright.dev/python/')
    # browser.close()
