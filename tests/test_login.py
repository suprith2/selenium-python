# tests/test_login.py
from pages.login_page import LoginPage

def test_login(driver, logger):
    logger.info('## Test login ##')
    
    login_page = LoginPage(driver)
    login_page.load('https://demo.nopcommerce.com/login')
    login_page.login('suppitest19@gmail.com', 'Testing@19')
    
    logger.info('## Test login Completed ##')


    