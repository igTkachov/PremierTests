import uuid
import pytest
import allure
import requests
import json


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get all Failed and Canceled orders with valid customer id")
def test_failed_and_canceled_orders():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_all_john_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED,CANCELLED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get only Failed orders with valid customer id")
def test_failed_orders():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_2_failed_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get only Canceled orders with valid customer id")
def test_canceled_orders():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_3_canceled_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'CANCELLED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders with Failed status and without customer id")
def test_failed_no_cust_id():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_all_john_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders with Cancelled status and without customer id")
def test_cancelled_no_cust_id():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_all_john_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'CANCELLED'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders with Failed and Cancelled status and without customer id")
def test_cancelled_no_cust_id():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_all_john_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED,CANCELLED'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders without query params")
def test_orders_without_query_param():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_all_john_orders.json')

    url = 'http://127.0.0.1:5000/payments'

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders with other customer id and without status")
def test_other_customer_no_status():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_another_customer.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'customer_id': 'igor-999'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Get orders with other customer id and some status")
def test_other_customer_some_status():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_another_customer_failed_status.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED,CANCELLED', 'customer_id': 'igor-999'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp



# Negative test cases
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not exist path param")
def test_not_exist_path_param():
    exp_resp = import_json_from_file('../jsons/400_response.json')

    url = 'http://127.0.0.1:5000/payments1'
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not exist query param")
def test_not_exist_query_param():
    exp_resp = import_json_from_file('../jsons/404_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status1': 'FAILED'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 404
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not exist value of status param")
def test_not_exist_value_of_status_param():
    exp_resp = import_json_from_file('../jsons/empty_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'null', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Empty value of status param")
def test_empty_value_of_status_param():
    exp_resp = import_json_from_file('../jsons/empty_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': '', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not exist value of customer id param")
def test_not_exist_value_of_customer_id_param():
    exp_resp = import_json_from_file('../jsons/empty_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'None'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Empty value of customer id param")
def test_empty_value_of_customer_id_param():
    exp_resp = import_json_from_file('../jsons/empty_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': ''}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not valid token")
def test_not_valid_token():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'not_valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Not valid token header name")
def test_not_valid_token_header():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'Not-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("Unknown additional header")
def test_unknown_additional_header():
    exp_resp = import_json_from_file('../jsons/payments/get/valid_response_2_failed_orders.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'valid_token'
    }
    resp = requests.get(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Post payments mock")
@allure.title("Not valid http method")
def test_not_valid_method():
    exp_resp = import_json_from_file('../jsons/405_response.json')

    url = 'http://127.0.0.1:5000/payments'
    params = {'status': 'FAILED', 'customer_id': 'john-123'}
    headers = {
        'Content-Type': 'application/json',
        'Not-Api-Key': 'valid_token'
    }
    resp = requests.delete(url, params=params, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 405
    assert exp_resp == act_resp



# I've added it just for store test cases. For implementation I need more time, but I'm not sure that it should be implemented with mock data
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("nextCursor less total amount of orders")
def test_nextCursor_less():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("nextCursor equal total amount of orders")
def test_nextCursor_equal():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("nextCursor one more of total amount of orders")
def test_nextCursor_one_more():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor one less of total amount of orders")
def test_prevCursor_one_less():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor less total amount of orders")
def test_prevCursor_less():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor equal total amount of orders")
def test_prevCursor_equal():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor one more of total amount of orders")
def test_prevCursor_one_more():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor one less of total amount of orders")
def test_prevCursor_one_less():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("prevCursor one less of total amount of orders")
def test_prevCursor_one_less():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Get payments mock")
@allure.title("add unsupported header")
def test_additional_unsupported_header():
    ''' Will be implemented later because need to create additional amount of data'''


@allure.step("Request")
def pretty_print_request(method: str, url: str, headers: dict, body: str):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        method + ' ' + url,
        '\n'.join('{}: {}'.format(k, v) for k, v in headers),
        body)
    )


@allure.step("Response")
def pretty_print_response(status_code: str, headers: dict, body: str):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in headers),
        body)
    )


def import_json_from_file(file: str):
    f = open(file)
    valid_response = json.loads(f.read())
    f.close()
    return valid_response
