# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.insurance_centre_policy_types
import easybimehlanding.models.extra_data_base_model_insurance_centre_policy_types

class BaseModelInsuranceCentrePolicyTypes(object):

    """Implementation of the 'Base Model InsuranceCentrePolicyTypes' model.

    TODO: type model description here.

    Attributes:
        is_success (bool): TODO: type description here.
        status (int): TODO: type description here.
        message (list of InsuranceCentrePolicyTypes): TODO: type description
            here.
        extra_data (ExtraDataBaseModelInsuranceCentrePolicyTypes): TODO: type
            description here.
        exception (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_success":'isSuccess',
        "status":'status',
        "message":'message',
        "extra_data":'extraData',
        "exception":'exception'
    }

    def __init__(self,
                 is_success=None,
                 status=None,
                 message=None,
                 extra_data=None,
                 exception=None):
        """Constructor for the BaseModelInsuranceCentrePolicyTypes class"""

        # Initialize members of the class
        self.is_success = is_success
        self.status = status
        self.message = message
        self.extra_data = extra_data
        self.exception = exception


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
        is_success = dictionary.get('isSuccess')
        status = dictionary.get('status')
        message = None
        if dictionary.get('message') != None:
            message = list()
            for structure in dictionary.get('message'):
                message.append(easybimehlanding.models.insurance_centre_policy_types.InsuranceCentrePolicyTypes.from_dictionary(structure))
        extra_data = easybimehlanding.models.extra_data_base_model_insurance_centre_policy_types.ExtraDataBaseModelInsuranceCentrePolicyTypes.from_dictionary(dictionary.get('extraData')) if dictionary.get('extraData') else None
        exception = dictionary.get('exception')

        # Return an object of this model
        return cls(is_success,
                   status,
                   message,
                   extra_data,
                   exception)


