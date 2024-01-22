from playwright.sync_api import sync_playwright

'''' The Sync API takes care of syncing your Contentstack data with
your application and ensures that the data is always up-to-date by providing delta updates'''

# playwright = sync_playwright().start()

with sync_playwright() as p:
    # launch browser and stay open for 2 sec
    browser = p.chromium.launch(headless=False, slow_mo = 2000)

    # create a new page
    page = browser.new_page()
    page.goto('https://playwright.dev/python/')

    # locate a link element with Docs text
    docs_button = page.get_by_role('link' , name ='Docs')
    docs_button.click()
    page.screenshot(path="demo.png")

    # ger the url
    print('Docs:' , page.url)




