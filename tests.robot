 *** Settings ***   |
| Documentation      | Example using the pipe separated format.
| Library            | OperatingSystem

| *** Variables ***  |
| ${MESSAGE}         | Hello, world!

| *** Test Cases *** |                 |               |
| My Test            | [Documentation] | Example test. |
|                    | Log             | ${MESSAGE}    | 
|                    | #My Keyword      | ${CURDIR}     |
| Another Test       | Should Be Equal | ${MESSAGE}    | encripted text 

#| #*** Keywords ***   |                        |         |
#| #My Keyword         | [Arguments]            | ${path} |
#|                     | #Directory Should Exist | ${path} | home/victoralonsogarcia8/