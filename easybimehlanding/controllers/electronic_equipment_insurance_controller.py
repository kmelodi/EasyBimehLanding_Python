# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from easybimehlanding.api_helper import APIHelper
from easybimehlanding.configuration import Configuration
from easybimehlanding.controllers.base_controller import BaseController
from easybimehlanding.models.base_model_electronic_equipment_insurance import BaseModelElectronicEquipmentInsurance
from easybimehlanding.models.base_model_device_brand_types import BaseModelDeviceBrandTypes
from easybimehlanding.models.base_model_divice_franchisee import BaseModelDiviceFranchisee

class ElectronicEquipmentInsuranceController(BaseController):

    """A Controller to access Endpoints in the easybimehlanding API."""


    def get_electronic_equipment_insurance(self,
                                           sub_domain,
                                           x_api_key):
        """Does a GET request to /ElectronicEquipmentInsurance/Initialize.

        دریافت اطلاعات اولیه استعلام بیمه نامه ی تجهیزات الکترونیک

        Args:
            sub_domain (string): دامنه یا زیر دامنه ی مرکز بیمه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelElectronicEquipmentInsurance: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ElectronicEquipmentInsurance/Initialize'
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
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelElectronicEquipmentInsurance.from_dictionary)

    def get_device_brand_types(self,
                               device_group,
                               device_type_id,
                               x_api_key):
        """Does a GET request to /ComboData/DeviceBrandTypes.

        دریافت لیست نوع برند دستگاه

        Args:
            device_group (int): شناسه ی گروه دستگاه
            device_type_id (int): شناسه ی نوع دستگاه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelDeviceBrandTypes: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ComboData/DeviceBrandTypes'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'deviceGroup': device_group,
            'deviceTypeId': device_type_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelDeviceBrandTypes.from_dictionary)

    def get_divice_franchisee(self,
                              device_model_id,
                              x_api_key):
        """Does a GET request to /ElectronicEquipmentInsurance/DiviceFranchisee.

        دریافت لیست فرانشیر استعلام بیمه نامه ی تجهیزات الکترونیک

        Args:
            device_model_id (int): شناسه ی مدل دستگاه
            x_api_key (string): کلید اختصاصی ارتباط با سرور

        Returns:
            BaseModelDiviceFranchisee: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ElectronicEquipmentInsurance/DiviceFranchisee'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'deviceModelId': device_model_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, BaseModelDiviceFranchisee.from_dictionary)
