# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class InsuranceRiskLevel(object):

    """Implementation of the 'InsuranceRiskLevel' model.

    میزان تخفیف عدم خسارت

    Attributes:
        id (int): TODO: type description here.
        title (string): TODO: type description here.
        extra_data (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "title":'title',
        "extra_data":'extraData'
    }

    def __init__(self,
                 id=None,
                 title=None,
                 extra_data=None):
        """Constructor for the InsuranceRiskLevel class"""

        # Initialize members of the class
        self.id = id
        self.title = title
        self.extra_data = extra_data


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
        title = dictionary.get('title')
        extra_data = dictionary.get('extraData')

        # Return an object of this model
        return cls(id,
                   title,
                   extra_data)


