import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[contains(@class, 'demo-frame')]"))
        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")
        achains = ActionChains(driver)
        achains.drag_and_drop(elem1, elem2).perform()
        time.sleep(2)


run = DragDrop()
run.drag_drop()
