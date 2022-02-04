# UI Autotests
## Setup

Require python 3.

`pip install selenium`
`pip install webdriver-manager`
`pip install pytest-bdd`

git clone https://github.com/igTkachov/PremierTests.git
cd PremierTests/ui-autotests

###Run tests with reporting listener to collect reports with default browser as Chrome
`pytest --alluredir=allure_results`

###Run tests with browser as Firefox
`pytest --alluredir=allure_results --browser=firefox`

###To see the actual report after your tests have finished run
`allure serve allure_results`
go to Behaviors folder