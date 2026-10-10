
def test_login(customer_login):

    customer_login.open_page()
    customer_login.login_form(login='sfaffd@sfd.com', password='asdfaf')
    customer_login.check_error("Invalid email or password")

def test_corr_email_with_incorr_pass(customer_login):

    customer_login.open_page()
    customer_login.login_form(login='valid@email.com', password='incorrect')
    customer_login.check_error("Invalid email or password")
