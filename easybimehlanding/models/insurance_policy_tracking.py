# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class InsurancePolicyTracking(object):

    """Implementation of the 'InsurancePolicy/Tracking' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        alias_name (string): TODO: type description here.
        status (string): TODO: type description here.
        create_on_persian_date (string): TODO: type description here.
        center_name (string): TODO: type description here.
        insurance_policy_type (int): TODO: type description here.
        insurance_type (string): TODO: type description here.
        price (int): TODO: type description here.
        paymented (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "alias_name":'aliasName',
        "status":'status',
        "create_on_persian_date":'createOnPersianDate',
        "center_name":'centerName',
        "insurance_policy_type":'insurancePolicyType',
        "insurance_type":'insuranceType',
        "price":'price',
        "paymented":'paymented'
    }

    def __init__(self,
                 id=None,
                 alias_name=None,
                 status=None,
                 create_on_persian_date=None,
                 center_name=None,
                 insurance_policy_type=None,
                 insurance_type=None,
                 price=None,
                 paymented=None):
        """Constructor for the InsurancePolicyTracking class"""

        # Initialize members of the class
        self.id = id
        self.alias_name = alias_name
        self.status = status
        self.create_on_persian_date = create_on_persian_date
        self.center_name = center_name
        self.insurance_policy_type = insurance_policy_type
        self.insurance_type = insurance_type
        self.price = price
        self.paymented = paymented


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
        id = dictionary.get('id')
        alias_name = dictionary.get('aliasName')
        status = dictionary.get('status')
        create_on_persian_date = dictionary.get('createOnPersianDate')
        center_name = dictionary.get('centerName')
        insurance_policy_type = dictionary.get('insurancePolicyType')
        insurance_type = dictionary.get('insuranceType')
        price = dictionary.get('price')
        paymented = dictionary.get('paymented')

        # Return an object of this model
        return cls(id,
                   alias_name,
                   status,
                   create_on_persian_date,
                   center_name,
                   insurance_policy_type,
                   insurance_type,
                   price,
                   paymented)


