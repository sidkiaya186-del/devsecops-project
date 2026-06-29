*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Création d'un utilisateur
    Create Session    api    ${BASE_URL}

    ${body}=    Create Dictionary
    ...    username=testuser
    ...    password=password123

    ${response}=    POST On Session
    ...    api
    ...    /register
    ...    json=${body}

    Should Be Equal As Integers    ${response.status_code}    201


Connexion utilisateur
    Create Session    api    ${BASE_URL}

    ${body}=    Create Dictionary
    ...    username=testuser
    ...    password=password123

    ${response}=    POST On Session
    ...    api
    ...    /login
    ...    json=${body}

    Should Be Equal As Integers    ${response.status_code}    200