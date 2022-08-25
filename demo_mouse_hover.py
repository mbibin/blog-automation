import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MouseHover():
    def mouse_hover(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        myaccountbutton = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        morebutton = driver.find_element(By.CLASS_NAME, "more-arr")
        achains = ActionChains(driver)
        achains.move_to_element(myaccountbutton).perform()
        time.sleep(2)
        achains.move_to_element(morebutton).perform()
        time.sleep(2)
        driver.find_element(By.ID, "booking_engine_adventures").click()
        time.sleep(2)


run = MouseHover()
run.mouse_hover()
