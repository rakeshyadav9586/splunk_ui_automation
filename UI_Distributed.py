from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splunk_ui_automation.IP_Address import *
import time

print("Type c or f ")
browser = input("Do you want to open in Chrome or Firefox : ")

print("Type yes or no ")
user_value = input("Do you want to do _bump & debug/refresh : ")

if browser == "c":
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
if browser == "f":
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--private")
    driver = webdriver.Firefox(options=firefox_options)

driver.implicitly_wait(60)
driver.maximize_window()
driver.set_page_load_timeout(60)
uname = "admin"
pwd = "admin123"


def SH(IP):
    try:
        handles = driver.window_handles
        size = len(handles)
        driver.get("http://" + IP + ":8000")
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print(IP + " : " + driver.title)
        if user_value == "yes":
            driver.get("http://" + IP + ":8000" + ui["bump"])
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='Bump version']").click()
            time.sleep(2)
            print("Bump done for " + IP)
            driver.get("http://" + IP + ":8000" + ui["debug_refresh"])
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='Refresh']").click()
            driver.get("http://" + IP + ":8000")
            time.sleep(3)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Debug/Refresh done for " + IP + "\n")
    except Exception as e:
        print("----------------------------Something is wrong with IP " + IP, e)



def IDX(IP):
    handles = driver.window_handles
    size = len(handles)
    try:
        driver.execute_script("window.open('" "http://" + IP + ":8000" "');")
        driver.switch_to.window(driver.window_handles[size])
        time.sleep(2)
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print(IP + " : " + driver.title)
        if user_value == "yes":
            driver.get("http://" + IP + ":8000" + ui["bump"])
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='Bump version']").click()
            time.sleep(2)
            print("Bump done for " + IP)
            driver.get("http://" + IP + ":8000" + ui["debug_refresh"])
            time.sleep(1)
            driver.find_element_by_xpath("//input[@value='Refresh']").click()
            driver.get("http://" + IP + ":8000")
            time.sleep(3)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Debug/Refresh done for " + IP + "\n")
    except Exception as e:
        print("----------------------------Something is wrong with IP " + IP, e)


# Run below method
# SH(local_linux_ip["sh1"])
# IDX(local_linux_ip["idx1"])

# IDX(local_windows_ip["sh1"])
# IDX(local_windows_ip["idx1"])
