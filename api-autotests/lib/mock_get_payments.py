import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/payments', methods=['GET'])
def get_payments():
    # get response from file
    resp_all_john_orders = import_json_from_file('../jsons/valid_response_all_john_orders.json')
    resp_failed_orders = import_json_from_file('../jsons/valid_response_2_failed_orders.json')
    resp_canceled_orders = import_json_from_file('../jsons/valid_response_3_canceled_orders.json')
    resp_other_customer = import_json_from_file('../jsons/valid_response_another_customer.json')
    resp_other_customer_failed_orders = import_json_from_file('../jsons/valid_response_another_customer_failed_status.json')
    resp_empty = import_json_from_file('../jsons/empty_response.json')
    resp_401 = import_json_from_file('../jsons/401_response.json')
    resp_400 = import_json_from_file('../jsons/400_response.json')
    resp_404 = import_json_from_file('../jsons/404_response.json')
    # headers
    headers = request.headers
    auth = headers.get("X-Api-Key")
    not_auth = headers.get("Not-Api-Key")
    # query
    args = request.args
    # status query and customer id query
    status = request.args.get("status")
    customer = request.args.get("customer_id")

    if auth != 'valid_token' or not_auth != None:
        return jsonify(resp_401), 401
    elif 'status1' in args:
        return jsonify(resp_404), 404
    elif 'status' in args and customer == None:
        return jsonify(resp_all_john_orders), 200
    elif status == None and customer == None:
        return jsonify(resp_all_john_orders), 200
    elif status == 'FAILED,CANCELLED' and customer == 'igor-999':
        return jsonify(resp_other_customer_failed_orders), 200
    elif 'status' in args and 'customer_id' in args:
        if ("CANCELLED,FAILED" in status or "FAILED,CANCELLED" in status) and customer == 'john-123' and auth == 'valid_token':
             return jsonify(resp_all_john_orders), 200
        elif status == 'FAILED' and customer == 'john-123'  and auth == 'valid_token':
            return jsonify(resp_failed_orders), 200
        elif status == 'CANCELLED' and customer == 'john-123' and auth == 'valid_token':
            return jsonify(resp_canceled_orders), 200
        else:
            return jsonify(resp_empty), 200
    elif customer != 'john-123':
        return jsonify(resp_other_customer), 200
    elif auth != 'valid_token':
        return jsonify(resp_401), 401
    else:
        return jsonify(resp_400), 400


@app.route('/payments', methods=['DELETE'])
def delete_payments():
    return jsonify({"message": "405 Method Not Allowed"}), 405


@app.route('/payments1', methods=['GET'])
def get_payments1():
    return jsonify({"message": "400 Bad Request"}), 400


@app.route('/payments', methods=['POST'])
def post_payments():
    # Predefined responses
    resp_valid_full = import_json_from_file('../jsons/payments/post/responses/valid_full_response.json')
    resp_400 = import_json_from_file('../jsons/400_response.json')
    resp_404 = import_json_from_file('../jsons/404_response.json')
    resp_401 = import_json_from_file('../jsons/401_response.json')
    # Headers
    headers = request.headers
    idempotency_header = headers.get("X-Idempotency-Key")
    content_type = headers.get("Content-Type")
    # Body
    request_data = request.get_json()
    payment_method_token = request_data.get('paymentMethodToken')
    customer_id = request_data.get('customerId')
    order_id = request_data.get('orderId')
    currency_code = request_data.get('currencyCode')
    amount = request_data.get('amount')
    paymentMethod = request_data.get('paymentMethod')
    paymentMethod_vaultOnSuccess = paymentMethod.get('vaultOnSuccess')
    customer = request_data.get('customer')
    customer_emailAddress = customer.get('emailAddress')
    metadata = request_data.get('metadata')
    metadata_productId = metadata.get('productId')
    metadata_merchantId = metadata.get('merchantId')

    if idempotency_header != 'valid_Idempotency-Key' or idempotency_header == 'repeated_Idempotency-Key':
        return jsonify(resp_401), 401
    elif customer_emailAddress == 'valid123@gmail.com' \
            or (payment_method_token == 'heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4' and amount is None) \
            or (payment_method_token == 'heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4' and currency_code is None) \
            or (payment_method_token == 'heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4' and order_id is None):
        return jsonify(resp_valid_full), 201
    elif paymentMethod_vaultOnSuccess is True and customer_id is None:
        return jsonify(resp_400), 400
    elif type(customer_id) == int:
        return jsonify(resp_400), 400
    elif customer_id == '' or customer_id == 'customer-234' or (customer_id is None and paymentMethod_vaultOnSuccess is False) :
        return jsonify(resp_valid_full), 201
    elif currency_code == 'XYZ' or currency_code == '':
        return jsonify(resp_400), 400
    elif amount == '$100' or amount == 0.1 or amount == -1:
        return jsonify(resp_400), 400
    elif amount == 0:
        return jsonify(resp_valid_full), 201
    elif metadata is not None or metadata_productId is None or metadata_merchantId is None:
        return jsonify(resp_400), 400
    elif idempotency_header == 'valid_Idempotency-Key':
        if payment_method_token == 'heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4':
            return jsonify(resp_valid_full), 201
        elif payment_method_token is None:
            return jsonify(resp_400), 400
        elif payment_method_token != 'heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4':
            return jsonify(resp_404), 404
    elif idempotency_header != 'valid_Idempotency-Key':
        return jsonify(resp_404), 404
    else:
        return jsonify({"message": "400 Bad Request"}), 400


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


def import_json_from_file(file: str):
    f = open(file)
    valid_response = json.loads(f.read())
    f.close()
    return valid_response


# Run in HTTP
app.run(host='127.0.0.1', port='5000')
