from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_search_backet(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'button not found'
