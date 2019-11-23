# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class GalleryDetail(object):

    """Implementation of the 'GalleryDetail' model.

    TODO: type model description here.

    Attributes:
        gallery_id (int): TODO: type description here.
        meta_media_file_id (int): TODO: type description here.
        meta_media_file_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gallery_id":'galleryId',
        "meta_media_file_id":'metaMediaFileId',
        "meta_media_file_url":'metaMediaFileUrl'
    }

    def __init__(self,
                 gallery_id=None,
                 meta_media_file_id=None,
                 meta_media_file_url=None):
        """Constructor for the GalleryDetail class"""

        # Initialize members of the class
        self.gallery_id = gallery_id
        self.meta_media_file_id = meta_media_file_id
        self.meta_media_file_url = meta_media_file_url


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
        gallery_id = dictionary.get('galleryId')
        meta_media_file_id = dictionary.get('metaMediaFileId')
        meta_media_file_url = dictionary.get('metaMediaFileUrl')

        # Return an object of this model
        return cls(gallery_id,
                   meta_media_file_id,
                   meta_media_file_url)


