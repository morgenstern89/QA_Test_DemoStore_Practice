from qatest.src.pages.locators.MyAccountSignInLocator import MyAccountSignInLocator
from qatest.src.SeleniumExtended import SeleniumExtended


class MyAccountSignIn(MyAccountSignInLocator):

    def __init__(self, driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)


    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)


