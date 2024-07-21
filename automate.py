from selenium import webdriver
import json

class ApplyLinkedin:
    def __init__(self, data):
        self.email = data['email']
        self.password = data['password']
        self.keyword = data['keyword']
        self.location = data['location']
        self.driver = webdriver.Chrome()



if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = ApplyLinkedin(data)