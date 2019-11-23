# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.insurance_centre_data
import easybimehlanding.models.insurance_centre_portal

class PortalLandingContactAbout(object):

    """Implementation of the 'PortalLandingContactAbout' model.

    TODO: type model description here.

    Attributes:
        licensed (bool): TODO: type description here.
        insurance_group (list of string): TODO: type description here.
        insurance_type (list of string): TODO: type description here.
        summary_cards (list of string): TODO: type description here.
        summary_notics (list of string): TODO: type description here.
        image_albums (list of string): TODO: type description here.
        video_galleries (list of string): TODO: type description here.
        insurance_centre (InsuranceCentreData): TODO: type description here.
        insurance_centre_portal (InsuranceCentrePortal): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "licensed":'licensed',
        "insurance_group":'insuranceGroup',
        "insurance_type":'insuranceType',
        "summary_cards":'summaryCards',
        "summary_notics":'summaryNotics',
        "image_albums":'imageAlbums',
        "video_galleries":'videoGalleries',
        "insurance_centre":'insuranceCentre',
        "insurance_centre_portal":'insuranceCentrePortal'
    }

    def __init__(self,
                 licensed=None,
                 insurance_group=None,
                 insurance_type=None,
                 summary_cards=None,
                 summary_notics=None,
                 image_albums=None,
                 video_galleries=None,
                 insurance_centre=None,
                 insurance_centre_portal=None):
        """Constructor for the PortalLandingContactAbout class"""

        # Initialize members of the class
        self.licensed = licensed
        self.insurance_group = insurance_group
        self.insurance_type = insurance_type
        self.summary_cards = summary_cards
        self.summary_notics = summary_notics
        self.image_albums = image_albums
        self.video_galleries = video_galleries
        self.insurance_centre = insurance_centre
        self.insurance_centre_portal = insurance_centre_portal


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
        licensed = dictionary.get('licensed')
        insurance_group = dictionary.get('insuranceGroup')
        insurance_type = dictionary.get('insuranceType')
        summary_cards = dictionary.get('summaryCards')
        summary_notics = dictionary.get('summaryNotics')
        image_albums = dictionary.get('imageAlbums')
        video_galleries = dictionary.get('videoGalleries')
        insurance_centre = easybimehlanding.models.insurance_centre_data.InsuranceCentreData.from_dictionary(dictionary.get('insuranceCentre')) if dictionary.get('insuranceCentre') else None
        insurance_centre_portal = easybimehlanding.models.insurance_centre_portal.InsuranceCentrePortal.from_dictionary(dictionary.get('insuranceCentrePortal')) if dictionary.get('insuranceCentrePortal') else None

        # Return an object of this model
        return cls(licensed,
                   insurance_group,
                   insurance_type,
                   summary_cards,
                   summary_notics,
                   image_albums,
                   video_galleries,
                   insurance_centre,
                   insurance_centre_portal)

