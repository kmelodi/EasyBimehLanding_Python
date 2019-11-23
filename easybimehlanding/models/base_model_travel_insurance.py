# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.travel_insurance

class BaseModelTravelInsurance(object):

    """Implementation of the 'Base Model TravelInsurance' model.

    TODO: type model description here.

    Attributes:
        is_success (bool): TODO: type description here.
        status (int): TODO: type description here.
        message (TravelInsurance): TODO: type description here.
        extra_data (string): TODO: type description here.
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
        """Constructor for the BaseModelTravelInsurance class"""

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
        message = easybimehlanding.models.travel_insurance.TravelInsurance.from_dictionary(dictionary.get('message')) if dictionary.get('message') else None
        extra_data = dictionary.get('extraData')
        exception = dictionary.get('exception')

        # Return an object of this model
        return cls(is_success,
                   status,
                   message,
                   extra_data,
                   exception)


