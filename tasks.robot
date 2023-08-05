*** Settings ***
Library builtln
Suite Setup
Test Setup

*** Test Cases ***

should Be True   Run Keyword And Expect Error
#Run Keyword If   Set Test Message
Run Keyword If   '${KEYWORD STATUS == 'PASS'}  Log  Passed
IF    '${item}' == '${element}'    RETURN    ${index}

*** Tasks ***
Example
    ${index} =    Find Index    baz    @{LIST}
    Should Be Equal    ${index}    ${1}
    ${index} =    Find Index    non existing    @{LIST}
    Should Be Equal    ${index}    ${-1}


#*** Comments ***
#*** Variables ***
#Should Be Equal    ${x}    ${y}    Custom error    values=True         # Strings are generally true.
