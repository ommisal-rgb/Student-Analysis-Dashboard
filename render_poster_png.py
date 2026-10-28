import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})
        html_path = "file:///" + os.path.abspath("A4_Student_Performance_Poster.html").replace("\\", "/")
        await page.goto(html_path)
        await page.wait_for_load_state("networkidle")
        
        # Take full page screenshot
        poster_elem = await page.query_selector(".a4-container")
        if poster_elem:
            await poster_elem.screenshot(path="poster_preview.png")
            print("Poster rendered successfully as poster_preview.png")
        else:
            await page.screenshot(path="poster_preview.png", full_page=True)
            print("Page screenshot saved as poster_preview.png")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
