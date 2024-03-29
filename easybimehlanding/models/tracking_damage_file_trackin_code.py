# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TrackingDamageFileTrackinCode(object):

    """Implementation of the 'TrackingDamageFile TrackinCode' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        tracking_damage_status_id (int): TODO: type description here.
        file_name (string): TODO: type description here.
        title (string): TODO: type description here.
        url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "tracking_damage_status_id":'trackingDamageStatusId',
        "file_name":'fileName',
        "title":'title',
        "url":'url'
    }

    def __init__(self,
                 id=None,
                 tracking_damage_status_id=None,
                 file_name=None,
                 title=None,
                 url=None):
        """Constructor for the TrackingDamageFileTrackinCode class"""

        # Initialize members of the class
        self.id = id
        self.tracking_damage_status_id = tracking_damage_status_id
        self.file_name = file_name
        self.title = title
        self.url = url


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
        tracking_damage_status_id = dictionary.get('trackingDamageStatusId')
        file_name = dictionary.get('fileName')
        title = dictionary.get('title')
        url = dictionary.get('url')

        # Return an object of this model
        return cls(id,
                   tracking_damage_status_id,
                   file_name,
                   title,
                   url)


