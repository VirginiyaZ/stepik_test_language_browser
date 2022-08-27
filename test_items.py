from selenium.webdriver.common.by import By
import time



def test_guest_should_see_basket_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)

    time.sleep(15)
    
    assert browser.find_elements(By.CLASS_NAME,'btn-add-to-basket'),'No basket btn!'