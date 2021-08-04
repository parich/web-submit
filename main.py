from selenium import webdriver
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

for x in range(200):

    driver = webdriver.Chrome(resource_path('/Users/parichsuriya/Downloads/chromedriver'))
    driver.get("https://survey.rmu.ac.th/services/index.php")
    #driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
    print(driver.current_url)
    print("รอบที่" + str(x))

    inputElementUser = driver.find_element_by_xpath(".//*[contains(text(), 'นักศึกษา')]").click()
    inputElementUser = driver.find_element_by_xpath(".//*[contains(text(), '19. ศูนย์คอมพิวเตอร์')]").click()
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star51"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star52"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star53"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star54"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star55"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star56"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star57"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star58"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star59"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star510"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star511"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star512"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star513"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star514"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star515"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star516"))
    inputElementUser = driver.execute_script("arguments[0].click();", driver.find_element_by_id("star517"))

    submit_button = driver.find_element_by_id("submitanswer").click()

    driver.quit()

driver.close()




