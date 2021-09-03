from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json
import time

options = Options()
options.headless = True # Hide browser

driver = webdriver.Firefox(options=options ,executable_path=r'C:\FirefoxDriverGecko\geckodriver.exe')
driver.get("https://ortus.lv")
time.sleep(2)
driver.find_element_by_id("IDToken1").send_keys("LOGIN") # Enter your Login from Ortus
driver.find_element_by_id("IDToken2").send_keys("PASSWORD") #Enter your Password from Ortus
driver.find_element_by_name("Login.Submit").click()
time.sleep(2)
try:
    driver.find_element_by_id("portalNavigationTabGroupsList").find_elements_by_tag_name("li")[1].click()
    time.sleep(1)
    Grafiki = driver.find_element_by_id("portalNavigation_u108l1s329").click()
    tables = driver.find_element_by_class_name("Pluto_59_u108l1n352_114018_days").find_element_by_tag_name("tbody").find_elements_by_xpath("./tr")

    weekShift = {}
    day = ""
    StartLesson = ""
    lessons = []
    tmpDict = {} 
    for index, table in enumerate(tables):
        row = table.find_elements_by_tag_name("td")
        day = row[0].text
        for para in row[1].find_elements_by_tag_name("tr"):
            StartLesson = para.find_elements_by_tag_name("td")[0]
            for less in para.find_elements_by_tag_name("td")[1].find_elements_by_tag_name("div"):
                lessons.append(less.text)
            tmpDict[StartLesson.text] = lessons
            lessons = []
        weekShift[day] = tmpDict
        tmpDict = {}
    driver.close()

    with open("weekShift.json", "w") as js:
        json.dump(weekShift,js,indent=2)
except Exception:
    print("Error")
    driver.close()