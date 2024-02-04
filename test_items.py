from selenium.webdriver.common.by import By
import time

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_search_backet(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'button not found'
