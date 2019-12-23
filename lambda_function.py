from selenium import webdriver

class Chrome:
    def headless_lambda(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "./layers/python3-selenium-headless/headless/python/bin/headless-chromium"
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--single-process")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-infobars")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--log-level=0")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--homedir=/tmp")

        driver = webdriver.Chrome(
            executable_path="./layers/python3-selenium-headless/headless/python/bin/chromedriver",
            chrome_options=options
        )
        return driver



def lambda_handler(event, context):
    chrome = Chrome()
    driver = chrome.headless_lambda()

    try:
        driver.get('https://example.com')

    except Exception as e:
        print(e)

