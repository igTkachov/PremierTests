import requests
from typing import Union, Dict, Tuple, List, Any

from pydantic import BaseModel


class CommonService:

    def __init__(self, service_endpoint: str, token: Union[Any, None]):
        """
        Constructor for communication with services
        :param service_endpoint: endpoint for requests. Example: https://someservice/v2/api
        :param token: object for working with authorization system. Can be None.
         If it is object, it must have field token
        """
        self.host = service_endpoint
        self.token = token
        self.last_response = None
        self.allow_redirects = True

    def execute_request(self, url: str, method: str, query_params: dict = None,
                        body_parameters: Union[Dict, Tuple, List] = None,
                        path_parameters: dict = None, headers: dict = None,
                        files: dict = None, expected_code: Union[str, int] = None,
                        check_code=True) -> requests.Response:
        """
        Execute request to remote service. It is wrapper around requests library
        :param url: relative URL to remote resource.
        :param method: HTTP method
        :param query_params: query parameters of request
        :param body_parameters: body parameters
        :param path_parameters: path parameters
        :param headers: additional headers that should be added to request
        :param files: files for uploading. Body parameters will be ignored
        :param expected_code: expected response code
        :type expected_code: str | int
        :param check_code: check response code. Default is true
        :return: response from service
        """

        full_url = "{}{}".format(self.host, url)
        normalized_method = method.lower()
        if path_parameters is not None:
            full_url.format(**path_parameters)
        response = None
        if self.token is None:
            request_headers = headers
        else:
            request_headers = {"Authorization": self.token.token}
            if headers:
                request_headers.update(headers)
        request_parameters = {'url': full_url,
                              'params': query_params,
                              'headers': request_headers,
                              'allow_redirects': self.allow_redirects
                              }
        if files:
            request_parameters['files'] = files
        else:
            if isinstance(body_parameters, BaseModel):
                request_parameters['json'] = body_parameters.dict(by_alias=True)
            else:
                request_parameters['json'] = body_parameters
        if normalized_method == 'get':
            response = requests.get(**request_parameters)
        if normalized_method == 'post':
            response = requests.post(**request_parameters)
        if normalized_method == 'put':
            response = requests.put(**request_parameters)
        if normalized_method == 'delete':
            response = requests.delete(**request_parameters)
        self.last_response = response
        if check_code:
            if expected_code is not None:
                assert response.status_code == expected_code, f"Response code is not expected: " \
                    f"{response.status_code} != {expected_code}"
            else:
                assert response.status_code == requests.codes.ok, f"Response code is not expected: " \
                    f"{response.status_code} != {requests.codes.ok}"
        return response
