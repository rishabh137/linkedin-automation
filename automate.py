from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time

class ApplyLinkedin:
    def __init__(self, data):
        self.email = data['email']
        self.password = data['password']
        self.keyword = data['keyword']
        self.location = data['location']
        self.driver = webdriver.Chrome()


    def login_linkedin(self):
        self.driver.get("https://www.linkedin.com/login")
        
        # Email
        email = self.driver.find_element(By.ID, "username")
        email.clear()
        email.send_keys(self.email)

        # Password
        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys(self.password)
        time.sleep(10)

        # Sign in button
        button = self.driver.find_element(By.CLASS_NAME, "btn__primary--large")
        button.send_keys(Keys.RETURN)
        time.sleep(10)




if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = ApplyLinkedin(data)
    bot.login_linkedin()