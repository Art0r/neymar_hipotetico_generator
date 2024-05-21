from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from src.classes import EmailLoginStep, PasswordLoginStep, UsernameLoginStep, LoginStep
from selenium.webdriver.common.keys import Keys
import time


class Login():
    wait: WebDriverWait
    
    def __init__(self, wait: WebDriverWait) -> None:
        self.wait = wait

    def start(self):
        self.run_step(EmailLoginStep)

        time.sleep(1)

        self.run_step(UsernameLoginStep)

        time.sleep(1)

        self.run_step(PasswordLoginStep)

        time.sleep(1)


    def run_step(self, step: LoginStep):
        input = self.wait.until(ec.presence_of_element_located(
        (By.XPATH, f"{step.INPUT_CLASS}")))

        input.send_keys(step.VALUE())

        input.send_keys(Keys.ENTER)
