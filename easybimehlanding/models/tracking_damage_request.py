# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.tracking_damage_status

class TrackingDamageRequest(object):

    """Implementation of the 'TrackingDamageRequest' model.

    TODO: type model description here.

    Attributes:
        personality_type (int): TODO: type description here.
        tracking_damage_status (list of TrackingDamageStatus): TODO: type
            description here.
        description (string): TODO: type description here.
        insurance_type_id (int): TODO: type description here.
        insurance_company_id (int): TODO: type description here.
        insurance_policy_number (string): TODO: type description here.
        damage_type (string): TODO: type description here.
        name (string): TODO: type description here.
        national_code (string): TODO: type description here.
        mobile (string): TODO: type description here.
        insured_profile (string): TODO: type description here.
        sub_domain (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "personality_type":'personalityType',
        "tracking_damage_status":'trackingDamageStatus',
        "description":'description',
        "insurance_type_id":'insuranceTypeId',
        "insurance_company_id":'insuranceCompanyId',
        "insurance_policy_number":'insurancePolicyNumber',
        "damage_type":'damageType',
        "name":'name',
        "national_code":'nationalCode',
        "mobile":'mobile',
        "insured_profile":'insuredProfile',
        "sub_domain":'subDomain'
    }

    def __init__(self,
                 personality_type=None,
                 tracking_damage_status=None,
                 description=None,
                 insurance_type_id=None,
                 insurance_company_id=None,
                 insurance_policy_number=None,
                 damage_type=None,
                 name=None,
                 national_code=None,
                 mobile=None,
                 insured_profile=None,
                 sub_domain=None):
        """Constructor for the TrackingDamageRequest class"""

        # Initialize members of the class
        self.personality_type = personality_type
        self.tracking_damage_status = tracking_damage_status
        self.description = description
        self.insurance_type_id = insurance_type_id
        self.insurance_company_id = insurance_company_id
        self.insurance_policy_number = insurance_policy_number
        self.damage_type = damage_type
        self.name = name
        self.national_code = national_code
        self.mobile = mobile
        self.insured_profile = insured_profile
        self.sub_domain = sub_domain


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
        personality_type = dictionary.get('personalityType')
        tracking_damage_status = None
        if dictionary.get('trackingDamageStatus') != None:
            tracking_damage_status = list()
            for structure in dictionary.get('trackingDamageStatus'):
                tracking_damage_status.append(easybimehlanding.models.tracking_damage_status.TrackingDamageStatus.from_dictionary(structure))
        description = dictionary.get('description')
        insurance_type_id = dictionary.get('insuranceTypeId')
        insurance_company_id = dictionary.get('insuranceCompanyId')
        insurance_policy_number = dictionary.get('insurancePolicyNumber')
        damage_type = dictionary.get('damageType')
        name = dictionary.get('name')
        national_code = dictionary.get('nationalCode')
        mobile = dictionary.get('mobile')
        insured_profile = dictionary.get('insuredProfile')
        sub_domain = dictionary.get('subDomain')

        # Return an object of this model
        return cls(personality_type,
                   tracking_damage_status,
                   description,
                   insurance_type_id,
                   insurance_company_id,
                   insurance_policy_number,
                   damage_type,
                   name,
                   national_code,
                   mobile,
                   insured_profile,
                   sub_domain)


