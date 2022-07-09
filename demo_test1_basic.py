import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoBlogPost():
    def open_blog(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("https://www.bejoygm.com")
        time.sleep(2)
        driver.maximize_window()
        print(driver.title)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "On Gita").click()
        time.sleep(4)

run = DemoBlogPost()
run.open_blog()
