# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DeviceBrandTypes(object):

    """Implementation of the 'DeviceBrandTypes' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        title (string): TODO: type description here.
        device_group (int): TODO: type description here.
        device_type_id (int): TODO: type description here.
        device_brand_id (string): TODO: type description here.
        create_on (string): TODO: type description here.
        update_on (string): TODO: type description here.
        created_by (string): TODO: type description here.
        updated_by (string): TODO: type description here.
        create_on_persian_date (string): TODO: type description here.
        update_on_persian_date (string): TODO: type description here.
        device_type_title (string): TODO: type description here.
        device_brand_title (string): TODO: type description here.
        device_type_brand_model_title (string): TODO: type description here.
        device_brand_ids (list of string): TODO: type description here.
        device_brands_title (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "title":'title',
        "device_group":'deviceGroup',
        "create_on":'createOn',
        "update_on":'updateOn',
        "created_by":'createdBy',
        "create_on_persian_date":'createOnPersianDate',
        "update_on_persian_date":'updateOnPersianDate',
        "device_type_brand_model_title":'deviceTypeBrandModelTitle',
        "device_brand_ids":'deviceBrandIds',
        "device_type_id":'deviceTypeId',
        "device_brand_id":'deviceBrandId',
        "updated_by":'updatedBy',
        "device_type_title":'deviceTypeTitle',
        "device_brand_title":'deviceBrandTitle',
        "device_brands_title":'deviceBrandsTitle'
    }

    def __init__(self,
                 id=None,
                 title=None,
                 device_group=None,
                 create_on=None,
                 update_on=None,
                 created_by=None,
                 create_on_persian_date=None,
                 update_on_persian_date=None,
                 device_type_brand_model_title=None,
                 device_brand_ids=None,
                 device_type_id=None,
                 device_brand_id=None,
                 updated_by=None,
                 device_type_title=None,
                 device_brand_title=None,
                 device_brands_title=None):
        """Constructor for the DeviceBrandTypes class"""

        # Initialize members of the class
        self.id = id
        self.title = title
        self.device_group = device_group
        self.device_type_id = device_type_id
        self.device_brand_id = device_brand_id
        self.create_on = create_on
        self.update_on = update_on
        self.created_by = created_by
        self.updated_by = updated_by
        self.create_on_persian_date = create_on_persian_date
        self.update_on_persian_date = update_on_persian_date
        self.device_type_title = device_type_title
        self.device_brand_title = device_brand_title
        self.device_type_brand_model_title = device_type_brand_model_title
        self.device_brand_ids = device_brand_ids
        self.device_brands_title = device_brands_title


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
        device_group = dictionary.get('deviceGroup')
        create_on = dictionary.get('createOn')
        update_on = dictionary.get('updateOn')
        created_by = dictionary.get('createdBy')
        create_on_persian_date = dictionary.get('createOnPersianDate')
        update_on_persian_date = dictionary.get('updateOnPersianDate')
        device_type_brand_model_title = dictionary.get('deviceTypeBrandModelTitle')
        device_brand_ids = dictionary.get('deviceBrandIds')
        device_type_id = dictionary.get('deviceTypeId')
        device_brand_id = dictionary.get('deviceBrandId')
        updated_by = dictionary.get('updatedBy')
        device_type_title = dictionary.get('deviceTypeTitle')
        device_brand_title = dictionary.get('deviceBrandTitle')
        device_brands_title = dictionary.get('deviceBrandsTitle')

        # Return an object of this model
        return cls(id,
                   title,
                   device_group,
                   create_on,
                   update_on,
                   created_by,
                   create_on_persian_date,
                   update_on_persian_date,
                   device_type_brand_model_title,
                   device_brand_ids,
                   device_type_id,
                   device_brand_id,
                   updated_by,
                   device_type_title,
                   device_brand_title,
                   device_brands_title)


