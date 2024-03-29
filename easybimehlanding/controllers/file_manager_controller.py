# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from easybimehlanding.api_helper import APIHelper
from easybimehlanding.configuration import Configuration
from easybimehlanding.controllers.base_controller import BaseController
from easybimehlanding.models.base_model_upload import BaseModelUpload

class FileManagerController(BaseController):

    """A Controller to access Endpoints in the easybimehlanding API."""


    def upload(self,
                sub_domain,
                x_api_key,
                file):
        """Does a POST request to /FileManager/Upload.

        آپلود فایل در ایزی بیمه
        بعد از آپلود، ادرس فایل باید در api های بعدی ارسال شود.

        Args:
            sub_domain (string): دامنه یا زیر دامنه ی مرکز بیمه
            x_api_key (string): کلید اختصاصی ارتباط با سرور
            file (string): فایل ارسالی

        Returns:
            BaseModelUpload: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/FileManager/Upload'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'subDomain': sub_domain
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'x-api-key': x_api_key
        }

        # Prepare form parameters
        _form_parameters = {
            'file': file
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelUpload.from_dictionary)
