import allure
import requests
import json


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel payment without payload")
def test_cancel_without_payload():
    exp_resp = import_json_from_file('../jsons/payments/post/responses/create_payload_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel payment with payload")
def test_cancel_with_payload():
    exp_resp = import_json_from_file('../jsons/payments/post/responses/create_payload_response.json')
    payload = import_json_from_file('../jsons/payments/post/requests/create_payload.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, json=payload, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel payment when id as int")
def test_cancel_id_as_int():
    exp_resp = import_json_from_file('../jsons/400_response.json')

    url = 'http://127.0.0.1:5000/payments/777/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel payment when id as int")
def test_cancel_id_as_int():
    exp_resp = import_json_from_file('../jsons/400_response.json')

    url = 'http://127.0.0.1:5000/payments/777/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 400
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response only required fields")
def test_cancel_only_required_fields():
    exp_resp = import_json_from_file('../jsons/payments/post/responses/create_payload_response_only_req_fields.json')

    url = 'http://127.0.0.1:5000/payments/ord-req/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response required fields plus one not required field")
def test_cancel_only_req_fields_plus_one_not_req():
    exp_resp = import_json_from_file('../jsons/payments/post/responses/create_payload_response_plus_id.json')

    url = 'http://127.0.0.1:5000/payments/ord-req-id/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert exp_resp == act_resp


# Check orderId field
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response orderId as string")
def test_cancel_orderId_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    ord_field = act_resp.get('orderId')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(ord_field, str) is True


# Check amount field
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response amount as string")
def test_cancel_amount_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    amount_field = act_resp.get('amount')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(amount_field, int) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response amount is zero")
def test_cancel_amount_is_zero():
    url = 'http://127.0.0.1:5000/payments/amount-zero/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    amount_field = act_resp.get('amount')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert amount_field == 0


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response amount field is positive number")
def test_cancel_amount_is_positive():
    url = 'http://127.0.0.1:5000/payments/amount-pos/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    amount_field = act_resp.get('amount')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert amount_field > 0


# Check currencyCode
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response currencyCode as string")
def test_cancel_currencyCode_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    currency_code_field = act_resp.get('currencyCode')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(currency_code_field, str) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response currencyCode as 3 digit")
def test_cancel_currencyCode_is_three_digit():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    currency_code_field = act_resp.get('currencyCode')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert len(currency_code_field) == 3


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response currencyCode is ISO format")
def test_cancel_currencyCode_is_iso_format():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    iso_list = ['EUR', 'USD', 'GBP']
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    currency_code_field = act_resp.get('currencyCode')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert currency_code_field in iso_list


# Check id
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response id as string")
def test_cancel_id_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    id_field = act_resp.get('id')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(id_field, str) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response id is unique")
def test_cancel_id_is_unique():
    '''To be implemented.'''


# Check date
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response date as string")
def test_cancel_date_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    date_field = act_resp.get('date')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(date_field, str) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response date as UTC format")
def test_cancel_sata_is_uts():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    date_field = act_resp.get('date')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert date_field == '2021-02-21T15:36:16.367687'


# Check status
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response status as string")
def test_cancel_status_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    status_field = act_resp.get('status')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(status_field, str) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response status belong to Status table")
def test_cancel_status_belong_to_table():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    list = ["PENDING", "FAILED", "AUTHORIZED", "SETTLING", "PARTIALLY_SETTLED", "SETTLED", "DECLINED", "CANCELLED"]
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    status_field = act_resp.get('status')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert status_field in list


# Check customerId
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response customerId as string")
def test_cancel_customerId_is_str():
    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    customer_id_field = act_resp.get('customerId')
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == requests.codes.ok
    assert isinstance(customer_id_field, str) is True


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response customerId unique")
def test_cancel_customerId_unique():
    '''To be implemented.'''


# Check metadata
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response metadata valid payment metadata object")
def test_cancel_metadata_object():
    '''To be implemented.'''


# Check metadata
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response customer valid customer object")
def test_cancel_customer_object():
    '''To be implemented.'''


# Check order
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response order valid order object")
def test_cancel_order_object():
    '''To be implemented.'''


# Check paymentMethod
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response payment method valid payment method object")
def test_cancel_payment_method_object():
    '''To be implemented.'''


# Check processor
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response processor method valid processor method object")
def test_cancel_processor_object():
    '''To be implemented.'''


# Check redirectAction
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response redirectAction valid processor redirect action object")
def test_cancel_redirect_action_object():
    '''To be implemented.'''


# Check statusReason
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response Status Reason valid processor Status Reason object")
def test_cancel_status_reason_object():
    '''To be implemented.'''


# Check Transactions
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Cancel response Transactions valid processor Transactions object")
def test_cancel_transactions_object():
    '''To be implemented.'''


# Tests for idempotency key
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Empty Idempotency-Key")
def test_empty_idempotency_key():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': ''
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Repeated Idempotency-Key. It should be Unique")
def test_repeated_idempotency_key():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'repeated_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Wrong format Idempotency-Key")
def test_wrong_format_idempotency_key():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': '**************'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Without Idempotency-Key")
def test_without_idempotency_key():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Wrong Idempotency-Key header name")
def test_wrong_idempotency_key_header_name():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'wrong-X-Idempotency-Key': 'valid_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock")
@allure.title("Two different Idempotency-Key headers")
def test_two_different_idempotency_key_headers():
    exp_resp = import_json_from_file('../jsons/401_response.json')

    url = 'http://127.0.0.1:5000/payments/ord-123/cancel'
    headers = {
        'Content-Type': 'application/json',
        'X-Idempotency-Key': 'repeated_Idempotency-Key',
        'X-Idempotency-Key': 'repeated2_Idempotency-Key'
    }
    resp = requests.post(url, headers=headers)
    act_resp = resp.json()
    pretty_print_request(resp.request.method, resp.request.url, resp.request.headers.items(), resp.request.body)
    pretty_print_response(resp.status_code, resp.headers.items(), resp.text)

    assert resp.status_code == 401
    assert exp_resp == act_resp


# Tests for Content Type
@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock :: application/json header")
@allure.title("Without application/json header")
def test_without_application_json_header():
    ''''''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock :: application/json header")
@allure.title("With empty application/json header")
def test_with_empty_application_json_header():
    ''' '''


@allure.epic("Autotests-API")
@allure.feature("Payments")
@allure.story("Cancel payments mock :: application/json header")
@allure.title("With not supported application/xml header")
def test_with_empty_application_xml_header():
    ''''''


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
