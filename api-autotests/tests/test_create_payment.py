import uuid
import pytest
import allure
import requests
import json
from lib.util import ApiUtil as util


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Create payment with full valid payload")
def test_full_valid_payload():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


# Tests for Required field in request
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body without paymentMethodToken")
def test_request_without_paymentMethodToken():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/without_paymentMethodToken_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty paymentMethodToken")
def test_request_with_empty_paymentMethodToken():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/with_empty_paymentMethodToken_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with wrong format of paymentMethodToken")
def test_request_with_wrong_format_of_paymentMethodToken():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/with_wrong_format_paymentMethodToken_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body paymentMethodToken and without amount")
def test_paymentMethodToken_without_amount():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_amount_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body paymentMethodToken and without currencyCode")
def test_paymentMethodToken_without_currencyCode():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_currencyCode_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body paymentMethodToken and without orderId")
def test_paymentMethodToken_without_orderId():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_orderId_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body paymentMethodToken and without amount, currencyCode, orderId")
def test_paymentMethodToken_without_amount_currencyCode_orderId():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_amount_currencyCode_orderId.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


# Tests for CustomerId
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with customerId and paymentMethod.vaultOnSuccess as true")
def test_customerId_vaultOnSuccess_is_true():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_customerId_vaultOnSuccess_true.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body without customerId and paymentMethod.vaultOnSuccess as false")
def test_without_customerId_vaultOnSuccess_is_false():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/without_customerId_vaultOnSuccess_false.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty customerId and paymentMethod.vaultOnSuccess as true")
def test_empty_customerId_vaultOnSuccess_is_true():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_customId_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body without customerId and paymentMethod.vaultOnSuccess as true")
def test_without_customerId_vaultOnSuccess_is_true():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/without_customerId_vaultOnSuccess_true.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request customerId as number")
def test_customerId_as_number():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_customer_id_number_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


# Tests for OrderId
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty orderId")
def test_empty_orderId():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_orderId_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


# Tests for CurrencyCode
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty CurrencyCode")
def test_empty_currencyCode():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_currencyCode.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with wrong ISO format of currencyCode")
def test_wrong_currencyCode():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_wrong_currencyCode_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


# Tests for amount
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty amount")
def test_empty_amount():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_amount_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with amount as string")
def test_amount_as_string():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_amount_as_string_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with amount as 0")
def test_amount_as_zero():
    exp_resp = util.import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_amount_as_zero_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with amount as decimal")
def test_amount_as_decimal():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_amount_as_decimal_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with amount as minus number")
def test_amount_as_minus_number():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_amount_as_long_number_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


# Tests for metadata
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty metadata")
def test_empty_metadata():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_metadata_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with empty metadata")
def test_empty_metadata():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_empty_metadata_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body without merchantId")
def test_without_merchantId():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_merchantId_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body without productId")
def test_without_productId():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_without_productId_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body productId isn't a number value")
def test_productId_is_not_number():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_productId_not_number_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body merchantId isn't a string value")
def test_merchantId_is_not_str():
    exp_resp = util.import_json_from_file('../jsons/400_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_merchantId_not_str_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


# Tests for customer
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with customer")
def test_with_customer():
    '''TODO Should be added a huge amount of tests for 8 inner fields'''


# Tests for order
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with order")
def test_with_customer():
    '''TODO Should be added a huge amount of tests for 4 inner fields'''


# Tests for paymentMethod
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Request body with order")
def test_with_customer():
    '''TODO Should be added a huge amount of tests for 3 inner fields'''


# Tests for idempotency key
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Empty Idempotency-Key")
def test_empty_idempotency_key():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': ''
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Repeated Idempotency-Key. It should be Unique")
def test_repeated_idempotency_key():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'repeated_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Wrong format Idempotency-Key")
def test_wrong_format_idempotency_key():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': '**************'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Without Idempotency-Key")
def test_without_idempotency_key():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Wrong Idempotency-Key header name")
def test_wrong_idempotency_key_header_name():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'wrong-X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Two different Idempotency-Key headers")
def test_two_different_idempotency_key_headers():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'repeated_Idempotency-Key',
        'X-Idempotency-Key': 'repeated2_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Two same Idempotency-Key headers")
def test_two_same_idempotency_key_headers():
    exp_resp = util.import_json_from_file('../jsons/401_response.json')
    payload = util.import_json_from_file('../jsons/payments/post/requests/valid_full_payload.json')

    url = 'http://127.0.0.1:5000/payments'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'repeated_Idempotency-Key',
        'X-Idempotency-Key': 'repeated_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    util.pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    util.pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


# Tests for Content Type
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("Without application/json header")
def test_without_application_json_header():
    ''''''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("With empty application/json header")
def test_with_empty_application_json_header():
    ''' '''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Create payments mock")
@allure.title("With not supported application/xml header")
def test_with_empty_application_xml_header():
    ''''''
