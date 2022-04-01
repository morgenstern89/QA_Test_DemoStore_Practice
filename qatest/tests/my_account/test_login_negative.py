import pytest
from qatest.src.pages.MyAccountSignOut import MyAccountSignOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        print("************")
        print("TEST LOGIN NON EXISTING")
        print("************")
        my_account = MyAccountSignOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('asfgwlekj')
        my_account.input_login_password('asdvwger')
        my_account.click_login_button()

        # verify error message
        expected_err = 'Unknown username. Check again or try your email address.'
        my_account.wait_until_error_is_displayed(expected_err)
