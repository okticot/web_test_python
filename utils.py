from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_webdriver():
    chromedriver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\Win10\Desktop\test_automation_project\chromedriver\chromedriver.exe'))
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    return driver


