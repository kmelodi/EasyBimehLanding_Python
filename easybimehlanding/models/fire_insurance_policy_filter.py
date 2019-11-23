# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class FireInsurancePolicyFilter(object):

    """Implementation of the 'FireInsurancePolicyFilter' model.

    TODO: type model description here.

    Attributes:
        insurance_policy_type (string): TODO: type description here.
        insurance_extra_coverage_ids (string): TODO: type description here.
        value_per_square_meter_coverage_rate_id (string): TODO: type
            description here.
        value_of_appliances_furnishing (string): TODO: type description here.
        city_id (string): TODO: type description here.
        skeleton_type_id (string): TODO: type description here.
        building_type_id (int): TODO: type description here.
        building_area (string): TODO: type description here.
        only_appliances_furnishings (string): TODO: type description here.
        policy_term_id (string): TODO: type description here.
        insurance_centre_sub_domain_name (string): TODO: type description
            here.
        insurance_centre_id (string): TODO: type description here.
        insurance_company_id (string): TODO: type description here.
        gift_code (string): TODO: type description here.
        customer_user_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "building_type_id":'buildingTypeId',
        "insurance_policy_type":'insurancePolicyType',
        "insurance_extra_coverage_ids":'insuranceExtraCoverageIds',
        "value_per_square_meter_coverage_rate_id":'valuePerSquareMeterCoverageRateId',
        "value_of_appliances_furnishing":'valueOfAppliancesFurnishing',
        "city_id":'cityId',
        "skeleton_type_id":'skeletonTypeId',
        "building_area":'buildingArea',
        "only_appliances_furnishings":'onlyAppliancesFurnishings',
        "policy_term_id":'policyTermId',
        "insurance_centre_sub_domain_name":'insuranceCentreSubDomainName',
        "insurance_centre_id":'insuranceCentreId',
        "insurance_company_id":'insuranceCompanyId',
        "gift_code":'giftCode',
        "customer_user_id":'customerUserId'
    }

    def __init__(self,
                 building_type_id=None,
                 insurance_policy_type=None,
                 insurance_extra_coverage_ids=None,
                 value_per_square_meter_coverage_rate_id=None,
                 value_of_appliances_furnishing=None,
                 city_id=None,
                 skeleton_type_id=None,
                 building_area=None,
                 only_appliances_furnishings=None,
                 policy_term_id=None,
                 insurance_centre_sub_domain_name=None,
                 insurance_centre_id=None,
                 insurance_company_id=None,
                 gift_code=None,
                 customer_user_id=None):
        """Constructor for the FireInsurancePolicyFilter class"""

        # Initialize members of the class
        self.insurance_policy_type = insurance_policy_type
        self.insurance_extra_coverage_ids = insurance_extra_coverage_ids
        self.value_per_square_meter_coverage_rate_id = value_per_square_meter_coverage_rate_id
        self.value_of_appliances_furnishing = value_of_appliances_furnishing
        self.city_id = city_id
        self.skeleton_type_id = skeleton_type_id
        self.building_type_id = building_type_id
        self.building_area = building_area
        self.only_appliances_furnishings = only_appliances_furnishings
        self.policy_term_id = policy_term_id
        self.insurance_centre_sub_domain_name = insurance_centre_sub_domain_name
        self.insurance_centre_id = insurance_centre_id
        self.insurance_company_id = insurance_company_id
        self.gift_code = gift_code
        self.customer_user_id = customer_user_id


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
        building_type_id = dictionary.get('buildingTypeId')
        insurance_policy_type = dictionary.get('insurancePolicyType')
        insurance_extra_coverage_ids = dictionary.get('insuranceExtraCoverageIds')
        value_per_square_meter_coverage_rate_id = dictionary.get('valuePerSquareMeterCoverageRateId')
        value_of_appliances_furnishing = dictionary.get('valueOfAppliancesFurnishing')
        city_id = dictionary.get('cityId')
        skeleton_type_id = dictionary.get('skeletonTypeId')
        building_area = dictionary.get('buildingArea')
        only_appliances_furnishings = dictionary.get('onlyAppliancesFurnishings')
        policy_term_id = dictionary.get('policyTermId')
        insurance_centre_sub_domain_name = dictionary.get('insuranceCentreSubDomainName')
        insurance_centre_id = dictionary.get('insuranceCentreId')
        insurance_company_id = dictionary.get('insuranceCompanyId')
        gift_code = dictionary.get('giftCode')
        customer_user_id = dictionary.get('customerUserId')

        # Return an object of this model
        return cls(building_type_id,
                   insurance_policy_type,
                   insurance_extra_coverage_ids,
                   value_per_square_meter_coverage_rate_id,
                   value_of_appliances_furnishing,
                   city_id,
                   skeleton_type_id,
                   building_area,
                   only_appliances_furnishings,
                   policy_term_id,
                   insurance_centre_sub_domain_name,
                   insurance_centre_id,
                   insurance_company_id,
                   gift_code,
                   customer_user_id)


