import os
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


# %%
def create_driver(proxy):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--enable-precise-memory-info")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument('--disable-dev-shm-usage')
    if proxy:
        chrome_options.add_argument(f"--proxy-server={proxy}")

    driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return driver


def homepage_screenshot(driver, url, output_dir):
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot(os.path.join(output_dir, 'index.png'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--website-url", help="The website URL.", required=True,
    )
    parser.add_argument(
        "--output-dir", help="Folder where to save the URL results.", required=True,
    )
    parser.add_argument("--proxy-server", help="If we are behind a proxy (without authentication)")

    args = parser.parse_args()

    driver = create_driver(proxy=args.proxy_server)
    homepage_screenshot(driver, args.website_url, args.output_dir)
    driver.close()


if __name__ == "__main__":
    main()