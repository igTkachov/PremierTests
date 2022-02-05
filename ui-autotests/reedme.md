# UI Autotests
## Setup

Require python 3.
### Install packages
`pip3 install -r requirements.txt`

or install packages separately 

`pip3 install selenium`
`pip3 install webdriver-manager`
`pip3 install pytest`
`pip3 install allure`

git clone https://github.com/igTkachov/PremierTests.git
cd PremierTests/ui-autotests

### Run tests with reporting listener to collect reports with default browser as Chrome
`pytest --alluredir=allure_results`

### Run tests with browsers Chrome and Firefox
`pytest --alluredir=allure_results log_in.py --browser=chrome --browser=firefox`

###To see the actual report after your tests have finished run
`allure serve allure_results`
go to Behaviors folder