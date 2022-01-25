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
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    elif 'status1' in args:
        return jsonify({"message": "404 Not Found"}), 404
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
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    else:
        return jsonify({"message": "400 Bad Request"}), 400


@app.route('/payments', methods=['POST'])
def post_payments():
    return jsonify({"message": "405 Method Not Allowed"}), 405


@app.route('/payments1', methods=['GET'])
def init_payments1():
    return jsonify({"message": "400 Bad Request"}), 400


def import_json_from_file(file: str):
    f = open(file)
    valid_response = json.loads(f.read())
    f.close()
    return valid_response


# Run in HTTP
app.run(host='127.0.0.1', port='5000')
