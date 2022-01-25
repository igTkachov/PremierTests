from json import JSONDecodeError
from typing import Dict, List


class PaymentAPI:

    def api_payments_get(self, limit: int=None, expected_code=None) -> List[DatasetExtendedCardOut]:
        """
        Get Payments
        """
        url = f"/fact"
        method = "get"
        query = {"limit": limit}
        body_parameters = None
        file = None
        response = self.execute_request(url, method, query, body_parameters, files=file, expected_code=expected_code)
        try:
            result_object = response.json()
            result_object = [DatasetExtendedCardOut(**item) for item in result_object]
        except JSONDecodeError:
            result_object = response.content
        return result_object
