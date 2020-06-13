from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splunk_ui_automation.IP_Address import *
import os
import time


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(120)
driver.maximize_window()
driver.set_page_load_timeout(120)
uname = "admin"
pwd = "admin123"


def SH(IP):
    try:
        driver.get("http://" + IP + ":8000")
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.get("http://" + IP + ":8000/en-US/manager/launcher/apps/local")
        driver.find_element_by_xpath(
            '//span[contains(text(),"Install app from file")]'
        ).click()
        upload_element = driver.find_element_by_id("appfile")

        dir_path = "C:\\Rakesh\\Latest_Build\\"

        for build_name in os.listdir(dir_path):
            if ".spl" in build_name:
                if os.path.isfile(os.path.join(dir_path, build_name)):
                    build_path = str(dir_path) + str(build_name)
                    print(build_path)
        upload_element.send_keys(build_path)
        time.sleep(1)
        driver.find_element_by_id("force").click()
        driver.find_element_by_xpath('//button[@type="submit"]').click()

        wait_element = driver.find_element_by_class_name("splButton-primary")
        if wait_element.is_displayed():
            wait_element.click()
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()
        print("Installed on....................-...................... " + IP)
    except Exception as e:
        print(".................................Something is wrong... " + IP, e)


def IDX(IP):
    try:
        handles = driver.window_handles
        size = len(handles)
        driver.execute_script("window.open('" "http://" + IP + ":8000" "');")
        driver.switch_to.window(driver.window_handles[size])
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.get("http://" + IP + ":8000/en-US/manager/launcher/apps/local")
        driver.find_element_by_xpath(
            '//span[contains(text(),"Install app from file")]'
        ).click()
        upload_element = driver.find_element_by_id("appfile")
        dir_path = "C:\\Rakesh\\Latest_Build\\"

        for build_name in os.listdir(dir_path):
            if ".spl" in build_name:
                if os.path.isfile(os.path.join(dir_path, build_name)):
                    build_path = str(dir_path) + str(build_name)
                    print(build_path)
        upload_element.send_keys(build_path)
        time.sleep(1)
        driver.find_element_by_id("force").click()
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        wait_element = driver.find_element_by_class_name("splButton-primary")
        if wait_element.is_displayed():
            wait_element.click()
        else:
            driver.get("http://" + IP + ":8000/en-US/manager/search/control")
            driver.find_element_by_id("restart-splunk-button").click()
        alert_popup = driver.switch_to_alert()
        time.sleep(1)
        alert_popup.accept()
        print("Installed on........................................... " + IP)
    except Exception as e:
        print("................................-Something is wrong... " + IP, e)


# Run the below method
# All local Linux VMs
# IDX(local_linux_ip["sh1"])
# IDX(local_linux_ip["idx1"])

# All local Windows VMs
# SH(local_windows_ip["sh1"])
# IDX(local_windows_ip["idx1"])


driver.close()
driver.quit()
