# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ElectronicEquipmentInsurancePolicyExtendView(object):

    """Implementation of the 'ElectronicEquipmentInsurancePolicyExtendView' model.

    TODO: type model description here.

    Attributes:
        device_type_id (int): شناسه ی نوع دستگاه
        device_brand_id (int): شناسه ی برند دستگاه
        device_model_id (int): شناسه ی مدل دستگاه
        device_serial (string): سریال دستگاه
        build_year (string): سال ساخت دستگاه
        device_value (int): TODO: type description here.
        franchisee (int): TODO: type description here.
        has_warranty (bool): TODO: type description here.
        warranty_company (string): TODO: type description here.
        serial_insurance_card (string): TODO: type description here.
        meta_media_behind_device_id (long|int): TODO: type description here.
        meta_media_behind_device_url (string): TODO: type description here.
        meta_media_on_device_id (long|int): TODO: type description here.
        meta_media_on_device_url (string): TODO: type description here.
        meta_media_device_box_id (long|int): TODO: type description here.
        meta_media_device_box_url (string): TODO: type description here.
        insurance_coverage_ids (string): TODO: type description here.
        insurance_coverage_price (string): TODO: type description here.
        base_premium (string): TODO: type description here.
        all_premium (string): TODO: type description here.
        insurance_company_discount_rate (string): TODO: type description
            here.
        insurance_company_discount (int): TODO: type description here.
        insurance_centre_discount (int): TODO: type description here.
        coupen_discount (int): TODO: type description here.
        all_discount (int): TODO: type description here.
        exchange_premium (int): TODO: type description here.
        device_type_title (string): TODO: type description here.
        device_brand_title (string): TODO: type description here.
        device_model_title (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "insurance_company_discount_rate":'insuranceCompanyDiscountRate',
        "insurance_company_discount":'insuranceCompanyDiscount',
        "insurance_centre_discount":'insuranceCentreDiscount',
        "coupen_discount":'coupenDiscount',
        "all_discount":'allDiscount',
        "exchange_premium":'exchangePremium',
        "device_type_id":'deviceTypeId',
        "device_brand_id":'deviceBrandId',
        "device_model_id":'deviceModelId',
        "device_serial":'deviceSerial',
        "build_year":'buildYear',
        "device_value":'deviceValue',
        "franchisee":'franchisee',
        "has_warranty":'hasWarranty',
        "warranty_company":'warrantyCompany',
        "serial_insurance_card":'serialInsuranceCard',
        "meta_media_behind_device_id":'metaMediaBehindDeviceId',
        "meta_media_behind_device_url":'metaMediaBehindDeviceUrl',
        "meta_media_on_device_id":'metaMediaOnDeviceId',
        "meta_media_on_device_url":'metaMediaOnDeviceUrl',
        "meta_media_device_box_id":'metaMediaDeviceBoxId',
        "meta_media_device_box_url":'metaMediaDeviceBoxUrl',
        "insurance_coverage_ids":'_InsuranceCoverageIds',
        "insurance_coverage_price":'insuranceCoveragePrice',
        "base_premium":'basePremium',
        "all_premium":'allPremium',
        "device_type_title":'deviceTypeTitle',
        "device_brand_title":'deviceBrandTitle',
        "device_model_title":'deviceModelTitle'
    }

    def __init__(self,
                 insurance_company_discount_rate=None,
                 insurance_company_discount=None,
                 insurance_centre_discount=None,
                 coupen_discount=None,
                 all_discount=None,
                 exchange_premium=None,
                 device_type_id=None,
                 device_brand_id=None,
                 device_model_id=None,
                 device_serial=None,
                 build_year=None,
                 device_value=None,
                 franchisee=None,
                 has_warranty=None,
                 warranty_company=None,
                 serial_insurance_card=None,
                 meta_media_behind_device_id=None,
                 meta_media_behind_device_url=None,
                 meta_media_on_device_id=None,
                 meta_media_on_device_url=None,
                 meta_media_device_box_id=None,
                 meta_media_device_box_url=None,
                 insurance_coverage_ids=None,
                 insurance_coverage_price=None,
                 base_premium=None,
                 all_premium=None,
                 device_type_title=None,
                 device_brand_title=None,
                 device_model_title=None):
        """Constructor for the ElectronicEquipmentInsurancePolicyExtendView class"""

        # Initialize members of the class
        self.device_type_id = device_type_id
        self.device_brand_id = device_brand_id
        self.device_model_id = device_model_id
        self.device_serial = device_serial
        self.build_year = build_year
        self.device_value = device_value
        self.franchisee = franchisee
        self.has_warranty = has_warranty
        self.warranty_company = warranty_company
        self.serial_insurance_card = serial_insurance_card
        self.meta_media_behind_device_id = meta_media_behind_device_id
        self.meta_media_behind_device_url = meta_media_behind_device_url
        self.meta_media_on_device_id = meta_media_on_device_id
        self.meta_media_on_device_url = meta_media_on_device_url
        self.meta_media_device_box_id = meta_media_device_box_id
        self.meta_media_device_box_url = meta_media_device_box_url
        self.insurance_coverage_ids = insurance_coverage_ids
        self.insurance_coverage_price = insurance_coverage_price
        self.base_premium = base_premium
        self.all_premium = all_premium
        self.insurance_company_discount_rate = insurance_company_discount_rate
        self.insurance_company_discount = insurance_company_discount
        self.insurance_centre_discount = insurance_centre_discount
        self.coupen_discount = coupen_discount
        self.all_discount = all_discount
        self.exchange_premium = exchange_premium
        self.device_type_title = device_type_title
        self.device_brand_title = device_brand_title
        self.device_model_title = device_model_title


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        insurance_company_discount_rate = dictionary.get('insuranceCompanyDiscountRate')
        insurance_company_discount = dictionary.get('insuranceCompanyDiscount')
        insurance_centre_discount = dictionary.get('insuranceCentreDiscount')
        coupen_discount = dictionary.get('coupenDiscount')
        all_discount = dictionary.get('allDiscount')
        exchange_premium = dictionary.get('exchangePremium')
        device_type_id = dictionary.get('deviceTypeId')
        device_brand_id = dictionary.get('deviceBrandId')
        device_model_id = dictionary.get('deviceModelId')
        device_serial = dictionary.get('deviceSerial')
        build_year = dictionary.get('buildYear')
        device_value = dictionary.get('deviceValue')
        franchisee = dictionary.get('franchisee')
        has_warranty = dictionary.get('hasWarranty')
        warranty_company = dictionary.get('warrantyCompany')
        serial_insurance_card = dictionary.get('serialInsuranceCard')
        meta_media_behind_device_id = dictionary.get('metaMediaBehindDeviceId')
        meta_media_behind_device_url = dictionary.get('metaMediaBehindDeviceUrl')
        meta_media_on_device_id = dictionary.get('metaMediaOnDeviceId')
        meta_media_on_device_url = dictionary.get('metaMediaOnDeviceUrl')
        meta_media_device_box_id = dictionary.get('metaMediaDeviceBoxId')
        meta_media_device_box_url = dictionary.get('metaMediaDeviceBoxUrl')
        insurance_coverage_ids = dictionary.get('_InsuranceCoverageIds')
        insurance_coverage_price = dictionary.get('insuranceCoveragePrice')
        base_premium = dictionary.get('basePremium')
        all_premium = dictionary.get('allPremium')
        device_type_title = dictionary.get('deviceTypeTitle')
        device_brand_title = dictionary.get('deviceBrandTitle')
        device_model_title = dictionary.get('deviceModelTitle')

        # Return an object of this model
        return cls(insurance_company_discount_rate,
                   insurance_company_discount,
                   insurance_centre_discount,
                   coupen_discount,
                   all_discount,
                   exchange_premium,
                   device_type_id,
                   device_brand_id,
                   device_model_id,
                   device_serial,
                   build_year,
                   device_value,
                   franchisee,
                   has_warranty,
                   warranty_company,
                   serial_insurance_card,
                   meta_media_behind_device_id,
                   meta_media_behind_device_url,
                   meta_media_on_device_id,
                   meta_media_on_device_url,
                   meta_media_device_box_id,
                   meta_media_device_box_url,
                   insurance_coverage_ids,
                   insurance_coverage_price,
                   base_premium,
                   all_premium,
                   device_type_title,
                   device_brand_title,
                   device_model_title)

