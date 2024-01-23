# 🎭 [Playwright](https://playwright.dev) for Python
## Documentation

[https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)

## API Reference

[https://playwright.dev/python/docs/api/class-playwright](https://playwright.dev/python/docs/api/class-playwright)



```py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('http://playwright.dev')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
```

```py
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://playwright.dev')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())
```



# Run test with Pytest

## Configuration file

* create a configuration file inside the project (_name_file.ini_)

    <img src="https://i.postimg.cc/ZKjZfYdc/adds.png" height="150">


```py
   [pytest]
   addopts = --browser chromium --headed --slowmo 1000 (or other option )
```

* when run project with pytest is no need to write all comands , just run pytest(name_project) in terminal




## Run in multiple browser in the same time use :
```py
pytest --browser chromium --browser firefox
```
## Run in headed mode
```py
pytest --headed
```
## Run in real browser pytest --browser-channel
```py
pytest --browser-channel (specified browser)
```
## Trace test
```py
pytest --tracing on ; to view file run : playwright show-trace (directory/name  of the file)
```

## Running Codegen 

*  run the test generator followed by the URL of the website you want to generate tests for

*  the URL is optional and you can always run the command without it and then add the URL directly into the browser window instead.

```py
playwright codegen (url)
```

* also run in emulated device

```py
playwright codegen --device="name of device , for ex iPhone 13" (url) or set size playwright codegen --viewport-size=800,600
```
 
