from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def setup_selenium() -> WebDriverWait:
    options = Options()

    # This option will make chrome to execute without appearing
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--verbose")

    website: str = "https://twitter.com/i/flow/login"
    
    service: Service = Service(executable_path=ChromeDriverManager().install())
    driver = Chrome(service=service, options=options)

    driver.get(website)

    wait = WebDriverWait(driver, 60)

    return wait