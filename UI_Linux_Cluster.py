from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from splunk_ui_automation.IP_Address import *
import time

print("Type yes or no ")
user_value = input("Do you want to do _bump & debug/refresh : ")
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(60)
uname = "admin"
pwd = "admin123"


def Master(IP):
    try:
        driver.get("http://" + IP + ":8000")
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        print(driver.title)
        driver.get("http://" + IP + ":8000/en-US/manager/system/clustering")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except Exception as e:

        print("Something is wrong... " + IP, e)


def Deployer(IP):
    try:
        handles = driver.window_handles
        size = len(handles)
        driver.execute_script("window.open('" "http://" + IP + ":8000" "');")
        driver.switch_to.window(driver.window_handles[size])
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print(driver.title)
    except Exception as e:
        print("Something is wrong... " + IP, e)


def IDX(IP):
    try:
        handles = driver.window_handles
        size = len(handles)
        driver.execute_script("window.open('" "http://" + IP + ":8000" "');")
        driver.switch_to.window(driver.window_handles[size])
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        print(driver.title)
        time.sleep(2)
        driver.get("http://" + IP + ":8000/en-US/manager/system/clustering")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

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
            time.sleep(4)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Debug/Refresh done for " + IP + "\n")
        print("Successfully Done.")
    except Exception as e:
        print("Something is wrong........................ " + IP, e)


def SH(IP):
    try:
        handles = driver.window_handles
        size = len(handles)
        driver.execute_script("window.open('" "http://" + IP + ":8000" "');")
        driver.switch_to.window(driver.window_handles[size])
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        print(driver.title)
        driver.get("http://" + IP + ":8000/en-US/manager/system/search_head_clustering")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

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
            time.sleep(4)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Debug/Refresh done for " + IP + "\n")
        print("Successfully Done.")
    except Exception as e:
        print("Something is wrong........................ " + IP, e)


# Local Cluster Master before setup
# Master(local_linux_cluster_ip["mstr"])
# IDX(local_linux_cluster_ip["idx1"])
# IDX(local_linux_cluster_ip["sh1"])


# Local Cluster Master after setup done
# Master(local_linux_cluster_ip["mstr"])
# IDX(local_linux_cluster_ip["idx1"])
# SH(local_linux_cluster_ip["sh1"])
