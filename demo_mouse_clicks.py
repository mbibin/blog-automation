import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MouseClicks():
    def mouse_clicks(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(2)
        achains = ActionChains(driver)
        # Right Click
        rightclickbutton = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")
        achains.context_click(rightclickbutton).perform()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".context-menu-icon-copy").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        # Double Clicks
        morebutton = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
        achains.double_click(morebutton).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

run = MouseClicks()
run.mouse_clicks()
