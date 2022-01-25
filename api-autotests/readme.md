# UI Autotests
## Setup

Require python 3.

`pip install allure`
`pip install requests`
`pip install json`

cd PremierTests/api-autotests/tests

###Run mock server
`python ../lib/mock_get_payments.py` 

###Run tests with reporting listener to collect reports
`pytest --alluredir=allure_results`

###To see the actual report after your tests have finished
`allure serve allure_results`