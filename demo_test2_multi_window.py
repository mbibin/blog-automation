import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoMultiWindow():
    def demo_multi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        parent_window = driver.current_window_handle
        driver.find_element(By.XPATH, "//a[@class='VueCarousel-slide slide package super-offer eventTrackable js-prodSpecEvtCat']//img").click()
        time.sleep(2)
        all_handle = driver.window_handles
        for handle in all_handle:
            if handle != parent_window:
                driver.switch_to.window(handle)
        driver.find_element(By.ID, 'booking_engine_hotels').click()
        time.sleep(4)


mw = DemoMultiWindow()
mw.demo_multi()



