from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_login-password")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    OFFER_NAME = (By.CSS_SELECTOR, '.product_main h1')
    OFFER_NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRICE_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[3]//strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages')
