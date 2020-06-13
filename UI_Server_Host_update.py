from selenium import webdriver
from splunk_ui_automation.IP_Address import *
import time


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(60)
driver.maximize_window()
driver.set_page_load_timeout(60)
uname = "admin"
pwd = "admin123"



def Server_Host(IP):
    try:
        driver.get("http://" + IP + ":8000")
        driver.find_element_by_id("username").send_keys(uname)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(2)
        driver.refresh()
        raw_ip = IP
        raw_ip = str(raw_ip).split(".")
        final_ip = raw_ip[2] + "." + (raw_ip[3])
        raw_splunk_version = driver.title
        raw_splunk_version = str(raw_splunk_version).split(" ")
        raw_splunk_version = raw_splunk_version[3]
        splunk_version = raw_splunk_version.split(".")
        splunk_version = splunk_version[0] + "." + splunk_version[1]
        server_host = final_ip + "_" + raw_splunk_version
        print(server_host)
        driver.get(
            "http://"
            + IP
            + ":8000/en-US/manager/launcher/server/settings/settings?action=edit"
        )
        server_name = driver.find_element_by_xpath('//input[@id="serverName_id"]')
        server_name.clear()
        server_name.send_keys(server_host)

        host_name = driver.find_element_by_xpath('//input[@id="host_id"]')
        host_name.clear()
        host_name.send_keys(server_host)

        driver.find_element_by_xpath('//span[contains(.,"Save")]').click()
        time.sleep(2)
        driver.get("http://" + IP + ":8000/en-US/manager/launcher/control")
        driver.find_element_by_xpath('//span[contains(.,"Restart Splunk")]').click()
        restart = driver.switch_to_alert()
        restart.accept()
        time.sleep(2)
        print("Server name & Host Name updated on..................... " + IP)

    except Exception as e:
        print(".................................Something is wrong... " + IP, e)


# All local Linux VMs
# Server_Host(local_linux_ip["sh1"])
# Server_Host(local_linux_ip["idx1"])


# All local Windows VMs
# Server_Host(local_windows_ip["sh1"])
# Server_Host(local_windows_ip["idx1"])

# All local Windows Cluster VMs
# Server_Host(local_windows_cluster_ip["mstr"])
# Server_Host(local_windows_cluster_ip["dplr"])
# Server_Host(local_windows_cluster_ip["idx1"])
# Server_Host(local_windows_cluster_ip["idx2"])
# Server_Host(local_windows_cluster_ip["idx3"])
# Server_Host(local_windows_cluster_ip["sh1"])
# Server_Host(local_windows_cluster_ip["sh2"])
# Server_Host(local_windows_cluster_ip["sh3"])


driver.close()
driver.quit()
