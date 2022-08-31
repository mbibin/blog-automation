import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MouseHover():
    def mouse_hover(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com//")
        driver.maximize_window()
        time.sleep(2)
        mobileaccebutton = driver.find_element(By.XPATH, "//li[contains(@navindex, '7')]")
        achains = ActionChains(driver)
        achains.move_to_element(mobileaccebutton).perform()
        time.sleep(2)
        # First Method
        driver.find_element(By.LINK_TEXT, "Printed Back Covers").click()
        slider1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        achains.drag_and_drop_by_offset(slider1, 60, 0).perform()
        time.sleep(2)
        # Second Method
        achains.click_and_hold(slider1).pause(1).move_by_offset(-60, 0).release().perform()
        time.sleep(2)
        # Third Method (Recommended)
        achains.move_to_element(slider1).pause(1).click_and_hold(slider1).move_by_offset(80, 0).release().perform()
        time.sleep(2)


run = MouseHover()
run.mouse_hover()
