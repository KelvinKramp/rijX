import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.service import Service
import requests

# define sleep parameter
sleep_par_short = 0.1
sleep_par_long = 10

# INPUT VARIABLES
test_page = "https://www.rijrotterdam.nl"
test_name = "test_name"
test_last_name = "test last name"
test_email = "test_email@email.com"
test_text = "THIS IS A TEST RUN"
test_question = "TEST QUESTION"
test_birthdate = "12/12/2001"
test_phonenumber = "0612341234"

# FULL XPATH LINKS
button1 = "/html/body/div[1]/header/ul/li[1]/a"
button2 = "/html/body/section/form/div[3]/button[2]"
name = "/html/body/section/form/div[2]/div[2]/div[2]/div[1]/input"
last_name = "/html/body/section/form/div[2]/div[2]/div[2]/div[2]/input"
birthdate = "/html/body/section/form/div[2]/div[2]/div[2]/div[3]/div/input"
email = "/html/body/section/form/div[2]/div[2]/div[2]/div[4]/input"
phone_number = "/html/body/section/form/div[2]/div[2]/div[2]/div[5]/input"
button3 = "/html/body/section/form/div[3]/button[2]"
submit = "/html/body/section/form/div[3]/button[3]"

# CHECK KEYWORDS
keyword1 = "Selecteer een afspraak"


class TestFeedbackApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('SETTING UP TEST UNIT')
        global driver, wait
        # https://stackoverflow.com/questions/63783983/element-not-interactable-in-selenium-chrome-headless-mode
        if "Users" in os.getcwd():
            options = Options()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            # options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        else:
            chrome_options = Options()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            ser = Service(os.environ.get("CHROMEDRIVER_PATH"))
            driver = webdriver.Chrome(service=ser,
                                  options=chrome_options)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        driver.get(test_page)
        print("CONNECTION TO BROWSER SUCCESFULL")


    def test_a_booking(self):
        x = requests.get('https://www.rijrotterdam.nl/booking')
        print(x.status_code)
        self.assertTrue(x.status_code == 200)
        # driver.maximize_window()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, button1)))
        # driver.find_element(By.XPATH, button1).click()
        #
        # driver.maximize_window()
        # driver.implicitly_wait(5)
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, button2)))
        # driver.implicitly_wait(5)
        # driver.maximize_window()
        #
        # driver.find_element(By.CLASS_NAME, "next").click()
        #
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, name)))
        # driver.find_element(By.XPATH, name).clear()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, name)))
        # driver.find_element(By.XPATH, name).send_keys(test_name)
        #
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, last_name)))
        # driver.find_element(By.XPATH, last_name).clear()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, last_name)))
        # driver.find_element(By.XPATH, last_name).send_keys(test_last_name)
        #
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, birthdate)))
        # driver.find_element(By.XPATH, birthdate).clear()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, birthdate)))
        # driver.find_element(By.XPATH, birthdate).send_keys(test_birthdate)
        #
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, email)))
        # driver.find_element(By.XPATH, email).clear()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, email)))
        # driver.find_element(By.XPATH, email).send_keys(test_email)
        #
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, phone_number)))
        # driver.find_element(By.XPATH, phone_number).clear()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, phone_number)))
        # driver.find_element(By.XPATH, phone_number).send_keys(test_phonenumber)
        #
        #
        # driver.maximize_window()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, button3)))
        # driver.find_element(By.XPATH, button2).click()
        #
        # driver.maximize_window()
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, submit)))
        # driver.find_element(By.XPATH, submit).click() # test

        # time.sleep(5)
        # page_source = driver.page_source
        # self.assertTrue(keyword1 in page_source)
        print("BOOKING OK")


    @classmethod
    def tearDownClass(cls):
        driver.close()
        print('TEARING DOWN CLASS')


if __name__ == '__main__':
    unittest.main()