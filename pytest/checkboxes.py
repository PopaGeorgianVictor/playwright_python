import asyncio
from playwright.async_api import async_playwright, expect


async def checkboxes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,slow_mo= 500)
        context = await browser.new_context()
        # await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/checkbox")
        await page.set_viewport_size({"width": 1920, "height": 1080})

        expected_number_of_options = 4
        all_checkboxes = await page.query_selector_all('input[name="age-group-checkbox"]')
        assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

        for checkbox in all_checkboxes:
            await checkbox.click()
            value = await checkbox.get_attribute('value')

            if await checkbox.is_checked():
                print(f"Checkbox with value '{value}' is selectable")
            else:
                raise  AssertionError(f"Value '{value}' is not selectable")

asyncio.run(checkboxes())