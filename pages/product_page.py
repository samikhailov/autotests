from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Add to chart button not found'


    def click_to_add_button(self):
        self.should_be_add_button()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()


    def should_be_alerts(self):
        assert self.is_elements_present(*ProductPageLocators.ALERTS), 'Alerts form not found'


    def get_price_from_description(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text


    def get_price_from_alert(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text


    def get_offer_name_from_description(self):
        return self.browser.find_element(*ProductPageLocators.OFFER_NAME).text


    def get_offer_name_from_alert(self):
        return self.browser.find_element(*ProductPageLocators.OFFER_NAME_IN_ALERT).text
