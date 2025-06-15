from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    options = Options()
    options.headless = False

    driver = webdriver.Firefox(options=options)
    driver.get("https://duckduckgo.com/")

    # Aceptar cookies si aparece el cartel
    try:
        time.sleep(1)
        accept_button = driver.find_element(By.XPATH, "//button[.='Aceptar todo'] | //button[.='Aceptar'] | //div[text()='Aceptar todo']")
        accept_button.click()
    except:
        pass

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("ISTQB TAE certification")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)
    assert "ISTQB" in driver.page_source

    driver.quit()

