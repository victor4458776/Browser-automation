*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Login with correct Username and Password
    Open Browser    url=https://the-internet.herokuapp.com/login    browser=chrome
    Input Text    username    tomsmith
    Input Text    password    SuperSecretPassword!
    Click Button     class:radius
    # Element Should Contain    id=flash    You logged into a secure area!
    Click Link    Logout 
    Close Browser

*** Keywords ***
Get Session Id
    Input Password @username
Get cookie
    Add Cookie
    value = "2qdjjqj29jd0qjdq2rf"
    name = "diane"
    httponly
Alert should be present
     text = "accept"
     action  ACCEPT "accept"
     timeout = None

Print Profile
   [Arguments]  ${firstName}  ${lastName}  ${title}  ${twitterHandle}
   Log to Console   \n__Profile__
   Log to Console   First Name: "${firstName}"
   Log to Console   Last Name: "${lastName}"
   Log to Console   Title: "${title}"

Capture Element Screenshot
    [Arguments]  ${locator} ${filename=selenium-element-screenshot-{index}.png} 
     

Add Tasks And Set To Complete
    # Open Browser    url=https://todomvc.com/examples/angularjs/#/    browser=chrome
    Input Text    class:new-todo    Complete Robot Framework Training
    Press Keys    class:new-todo    RETURN
    Input Text    class:new-todo    Write Automated Tests
    Press Keys    class:new-todo    RETURN
    Input Text    class:new-todo    Take a nap
    Press Keys    class:new-todo    RETURN
    Element Text Should Be    class:todo-count    3 items left
    Click Element    xpath: //*[contains(text(), "Complete Robot Framework Training")]/../input
    Element Text Should Be    class:todo-count    2 items left
    Click Element    xpath: //*[contains(text(), "Write Automated Tests")]/../input
    Element Text Should Be    class:todo-count    1 item left
    Click Element    xpath: //*[contains(text(), "Take a nap")]/../input
    Element Text Should Be    class:todo-count    0 items left
Input Password @username
    # TODO: implement keyword "Input Password @username".
    Fail    Not Implemented


value
    # TODO: implement keyword "value".
    Fail    Not Implemented


name
    # TODO: implement keyword "name".
    Fail    Not Implemented


httponly
    # TODO: implement keyword "httponly".
    Fail    Not Implemented

QTA-1


text = "accept"
    # TODO: implement keyword "text = "accept"".
    Fail    Not Implemented

