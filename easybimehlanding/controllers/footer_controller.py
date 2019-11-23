# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from easybimehlanding.api_helper import APIHelper
from easybimehlanding.configuration import Configuration
from easybimehlanding.controllers.base_controller import BaseController
from easybimehlanding.models.base_model_portal_landing_contact_about import BaseModelPortalLandingContactAbout
from easybimehlanding.models.base_model_faq_insurance_centre import BaseModelFaqInsuranceCentre
from easybimehlanding.models.base_model_insurance_policy_tracking import BaseModelInsurancePolicyTracking
from easybimehlanding.exceptions.internal_server_error_exception import InternalServerErrorException

class FooterController(BaseController):

    """A Controller to access Endpoints in the easybimehlanding API."""


    def get_portal_landing_contact_about(self,
                                         x_api_key):
        """Does a GET request to /InsuranceCentre/PortalLandingContactAbout/hfz1.

        دریافت اطلاعات درباره ی ما

        Args:
            x_api_key (string): TODO: type description here. Example: 

        Returns:
            BaseModelPortalLandingContactAbout: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/InsuranceCentre/PortalLandingContactAbout/hfz1'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelPortalLandingContactAbout.from_dictionary)

    def get_faq_insurance_centre(self,
                                 x_api_key):
        """Does a GET request to /Faq/InsuranceCentre/hfz1.

        دریافت لیست سوالات متداول

        Args:
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelFaqInsuranceCentre: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Faq/InsuranceCentre/hfz1'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelFaqInsuranceCentre.from_dictionary)

    def get_insurance_policy_tracking(self,
                                      tracking_code,
                                      national_code,
                                      x_api_key):
        """Does a GET request to /InsurancePolicy/Tracking.

        پیگیری وضعیت بیمه نامه

        Args:
            tracking_code (int): شماره ی پیگیری بیمه نامه
            national_code (long|int): کد ملی کاربر
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelInsurancePolicyTracking: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/InsurancePolicy/Tracking'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'trackingCode': tracking_code,
            'nationalCode': national_code
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 500:
            raise InternalServerErrorException('Internal Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelInsurancePolicyTracking.from_dictionary)
