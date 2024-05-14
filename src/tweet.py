import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Tweet:
    wait: WebDriverWait
    
    def __init__(self, wait: WebDriverWait) -> None:
        self.wait = wait


    def start(self, text: str):

        input = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, f"//*[@class='css-175oi2r r-184en5c']")))

        input.click()

        texts_inputs = self.wait.until(ec.presence_of_all_elements_located(
            (By.XPATH, f"//*[@data-offset-key]")))
        
        texts_inputs[0].send_keys(text)

        time.sleep(2)

        button = self.wait.until(ec.presence_of_element_located(
                    (By.XPATH, f"//*[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")))
                
        button.click()

        time.sleep(3)