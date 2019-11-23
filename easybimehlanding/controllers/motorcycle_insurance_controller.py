# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from easybimehlanding.api_helper import APIHelper
from easybimehlanding.configuration import Configuration
from easybimehlanding.controllers.base_controller import BaseController
from easybimehlanding.models.car_brands import CarBrands
from easybimehlanding.models.car_brand_tips import CarBrandTips
from easybimehlanding.models.has_plan import HasPlan

class MotorcycleInsuranceController(BaseController):

    """A Controller to access Endpoints in the easybimehlanding API."""


    def get_car_brands(self,
                       car_type_group,
                       x_api_key):
        """Does a GET request to /ComboData/CarBrands.

        دریافت لیست برند موتور سیکلت

        Args:
            car_type_group (int): شناسه ی گروه خودرویی، موتور سیکلت =>0
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            CarBrands: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ComboData/CarBrands'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'carTypeGroup': car_type_group
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
        return APIHelper.json_deserialize(_context.response.raw_body, CarBrands.from_dictionary)

    def get_car_brand_tips(self,
                           car_brand_id,
                           x_api_key):
        """Does a GET request to /ComboData/CarBrandTips.

        دریافت لیست تیپ موتور سیکلت

        Args:
            car_brand_id (int): شناسه ی برند موتور سیکلت
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            CarBrandTips: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ComboData/CarBrandTips'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'carBrandId': car_brand_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, CarBrandTips.from_dictionary)

    def get_has_plan(self,
                     sub_domain,
                     insurance_policy_type,
                     x_api_key):
        """Does a GET request to /InsurancePolicyPlan/HasPlan.

        آیا این نوع بیمه نامه، طرح بیمه ای دارد؟

        Args:
            sub_domain (string): دامنه یا زیر دامنه ی مرکز بیمه
            insurance_policy_type (int): شناسه ی نوع بیمه نامه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            HasPlan: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/InsurancePolicyPlan/HasPlan'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'subDomain': sub_domain,
            'insurancePolicyType': insurance_policy_type
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
        return APIHelper.json_deserialize(_context.response.raw_body, HasPlan.from_dictionary)
