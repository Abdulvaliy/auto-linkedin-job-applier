import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=103644278&keywords=python%20developer&location=United%20States"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=2650563877&f_AL=true&f_WRA=true&geoId=102257491&keywords=digital%20marketing&location=London%2C%20England%2C%20United%20Kingdom"
USERNAME = "your_any_mail"
PASSWORD = "and_password"
PHONE_NUMBER = "your phone number"

chrome_driver_path = "/..../chromedriver" #location for chrome driver
driver = webdriver.Chrome(chrome_driver_path)
driver.get(URL)

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

time.sleep(2)  # Wait for the next page to load.


login = driver.find_element_by_name("session_key")
login.send_keys(USERNAME)

password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)
time.sleep(1)

log_in = driver.find_element_by_class_name("btn__primary--large")
log_in.click()
time.sleep(2)

all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in all_jobs:
    print("called")
    job.click()
    time.sleep(1)

    try:
        apply_button = driver.find_element_by_class_name("jobs-apply-button")
        apply_button.click()
        time.sleep(5)

        phone_num = driver.find_element_by_class_name("fb-single-line-text__input")
        print(phone_num.get_attribute("value"))
        if phone_num.get_attribute("value") == "":
            phone_num.send_keys(PHONE_NUMBER)
        print(phone_num.get_attribute("value"))
        next_button = driver.find_element_by_css_selector("footer button")
        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if next_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            next_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

