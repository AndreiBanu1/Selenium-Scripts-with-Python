from behave import given, when, then

@given('User have opened the browser')
def step_given_user_opened_browser(context):
    print('Opened the browser Successfully')

@when('User have opened EasyTesting website')
def step_when_user_open_easy_testing_website(context):
    print('Opened the Login screen Successfully')

@when('User entered username as "{arg1}" and password as "{arg2}"')
def step_when_user_enter_username_password(context, arg1, arg2):
    print(f'Enter username as {arg1} Password as {arg2}')

@then('Login button should exist')
def step_then_login_button_should_exist(context):
    print('Button pressed Successfully')