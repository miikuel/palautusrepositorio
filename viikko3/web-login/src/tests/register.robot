*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville12345
    Set Password Confirmation  ville12345
    Submit Credentials

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville12345
    Set Password Confirmation  ville12345
    Submit Credentials
    # Register Should Fail With Message  Username has to be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  12345
    Set Password Confirmation  12345
    Submit Credentials
    # Register Should Fail With Message  Password has to be at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  abcabcabc
    Set Password Confirmation  abcabcabc
    Submit Credentials
    # Register Should Fail With Message  Password cannot consist only of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  abcabcabc
    Set Password Confirmation  cbacbacba
    Submit Credentials
    # Register Should Fail With Message  Password and confirmation don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    # Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
    # Register Should Fail With Message  Username and password are required

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

# Register Should Fail With Message
#     [Arguments]  ${message}
#     Register Page Should Be Open
#     Page Should Contain  ${message}