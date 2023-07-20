import time

from selenium.webdriver.common.by import By

def test_search_example(driver):
    driver.get('https://google.com')
    time.sleep(10)
    search_input = driver.find_element(By.NAME, 'q')
    search_input.clear()
    search_input.send_keys('first test')
    time.sleep(10)
    search_button = driver.find_element(By.NAME, "btnK")
    search_button.click()
    time.sleep(10)
    driver.save_screenshot('result.png')
