import allure
import json


class ApiUtil:

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
