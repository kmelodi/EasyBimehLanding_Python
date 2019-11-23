# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from easybimehlanding.api_helper import APIHelper
from easybimehlanding.configuration import Configuration
from easybimehlanding.controllers.base_controller import BaseController
from easybimehlanding.models.base_model_portal_landing_page import BaseModelPortalLandingPage
from easybimehlanding.models.base_model_insurance_centre_policy_types import BaseModelInsuranceCentrePolicyTypes

class MainController(BaseController):

    """A Controller to access Endpoints in the easybimehlanding API."""


    def get_portal_landing_page(self,
                                id,
                                x_api_key):
        """Does a GET request to /InsuranceCentre/PortalLandingPage.

        در یافت اطلاعات لندینگ مراکز بیمه

        Args:
            id (string): دامنه یا زیر دامنه ی مرکز بیمه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelPortalLandingPage: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/InsuranceCentre/PortalLandingPage'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'x-api-key': x_api_key
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelPortalLandingPage.from_dictionary)

    def get_insurance_centre_policy_types(self,
                                          sub_domain,
                                          x_api_key):
        """Does a GET request to /ComboData/InsuranceCentrePolicyTypes.

        دریافت لیست بیمه ی های ارائه شده توسط مرکز بیمه

        Args:
            sub_domain (string): دامنه یا زیر دامنه ی مرکز بیمه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelInsuranceCentrePolicyTypes: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ComboData/InsuranceCentrePolicyTypes'
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

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelInsuranceCentrePolicyTypes.from_dictionary)
