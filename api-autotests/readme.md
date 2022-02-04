# UI Autotests
## Setup

Require python 3.

`pip install allure`
`pip install requests`
`pip install json`

git clone https://github.com/igTkachov/PremierTests.git
cd PremierTests/api-autotests/tests

###Run api server for get responses
`python ../lib/mock_get_payments.py` 

###Run tests with reporting listener to collect reports
`pytest --alluredir=allure_results`

###To see the actual report after your tests have finished run
`allure serve allure_results`
go to Behaviors folder