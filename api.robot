*** Settings ***
Library         tests/test_api.py
Library         Keys/TestApi.py
Variables       Vars/Urls.py
Force Tags  eno_qa


*** Test Cases ***
Challenge 1 without class
    [Tags]   challenge_1
    test_api_challenge


Challenge 2 without class
    [Tags]   challenge_2
    ${resp}=    get all available pets from swagger
    send pet name in uppercase   ${resp}

############## OR

Challenge 1_2 with class
    [Tags]   challenge_1_2
    ${Response}=    get response url api    ${challenge1_url}
    should be true  ${Response.status_code}==200
    validate json data is an array       ${Response}
    find and write company name from response   response=${Response}

Challenge 2_2 with class
    [Tags]   challenge_2_2
    ${resp}=    get all available pets
    send pet name in uppercase and assert  ${resp}