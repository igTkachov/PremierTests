# UI Autotests
## Setup

Require python 3.
### Install packages
`pip3 install -r requirements.txt`

or install packages separately

`pip3 install allure`
`pip3 install requests`
`pip3 install flask`
`pip3 install pytest`
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