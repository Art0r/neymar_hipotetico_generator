import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from classes import EmailLoginStep, PasswordLoginStep, UsernameLoginStep, LoginStep
from config import EMAIL, PASSWORD, USERNAME


class Login():
    wait: WebDriverWait
    
    def __init__(self, wait: WebDriverWait) -> None:
        self.wait = wait

    def start(self):
        self.run_step(EmailLoginStep)

        time.sleep(2)

        self.run_step(UsernameLoginStep)

        time.sleep(2)

        self.run_step(PasswordLoginStep)

        time.sleep(2)


    def run_step(self, step: LoginStep):
        input = self.wait.until(ec.presence_of_element_located(
        (By.XPATH, f"//*[@class='{step.INPUT_CLASS}']")))

        if step is EmailLoginStep: input.send_keys(EMAIL)
        elif step is UsernameLoginStep: input.send_keys(USERNAME)
        elif step is PasswordLoginStep: input.send_keys(PASSWORD)

        foward_button = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, f"//*[@class='{step.BUTTON_CLASS}']")))

        foward_button.click()