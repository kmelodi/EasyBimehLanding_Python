# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TravelInsurancePolicyExtend(object):

    """Implementation of the 'TravelInsurancePolicyExtend' model.

    TODO: type model description here.

    Attributes:
        insurance_policy_id (int): TODO: type description here.
        travel_duration_param (string): TODO: type description here.
        passengers_count (int): TODO: type description here.
        birth_date (string): TODO: type description here.
        birth_date_persian (string): TODO: type description here.
        risk_level_discount (int): TODO: type description here.
        base_premium (string): TODO: type description here.
        all_premium (string): TODO: type description here.
        insurance_company_discount_rate (int): TODO: type description here.
        insurance_company_discount (int): TODO: type description here.
        insurance_centre_discount (int): TODO: type description here.
        coupen_discount (int): TODO: type description here.
        all_discount (int): TODO: type description here.
        exchange_premium (int): TODO: type description here.
        travel_rate_plan_id (string): TODO: type description here.
        plan_title (string): TODO: type description here.
        travel_insurance_policy_extend_ages (string): TODO: type description
            here.
        travel_insurance_policy_extend_passengers (string): TODO: type
            description here.
        zone_ids (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "insurance_policy_id":'insurancePolicyId',
        "passengers_count":'passengersCount',
        "risk_level_discount":'riskLevelDiscount',
        "insurance_company_discount_rate":'insuranceCompanyDiscountRate',
        "insurance_company_discount":'insuranceCompanyDiscount',
        "insurance_centre_discount":'insuranceCentreDiscount',
        "coupen_discount":'coupenDiscount',
        "all_discount":'allDiscount',
        "exchange_premium":'exchangePremium',
        "travel_duration_param":'travelDurationParam',
        "birth_date":'birthDate',
        "birth_date_persian":'birthDatePersian',
        "base_premium":'basePremium',
        "all_premium":'allPremium',
        "travel_rate_plan_id":'travelRatePlanId',
        "plan_title":'planTitle',
        "travel_insurance_policy_extend_ages":'travelInsurancePolicyExtendAges',
        "travel_insurance_policy_extend_passengers":'travelInsurancePolicyExtendPassengers',
        "zone_ids":'zoneIds'
    }

    def __init__(self,
                 insurance_policy_id=None,
                 passengers_count=None,
                 risk_level_discount=None,
                 insurance_company_discount_rate=None,
                 insurance_company_discount=None,
                 insurance_centre_discount=None,
                 coupen_discount=None,
                 all_discount=None,
                 exchange_premium=None,
                 travel_duration_param=None,
                 birth_date=None,
                 birth_date_persian=None,
                 base_premium=None,
                 all_premium=None,
                 travel_rate_plan_id=None,
                 plan_title=None,
                 travel_insurance_policy_extend_ages=None,
                 travel_insurance_policy_extend_passengers=None,
                 zone_ids=None):
        """Constructor for the TravelInsurancePolicyExtend class"""

        # Initialize members of the class
        self.insurance_policy_id = insurance_policy_id
        self.travel_duration_param = travel_duration_param
        self.passengers_count = passengers_count
        self.birth_date = birth_date
        self.birth_date_persian = birth_date_persian
        self.risk_level_discount = risk_level_discount
        self.base_premium = base_premium
        self.all_premium = all_premium
        self.insurance_company_discount_rate = insurance_company_discount_rate
        self.insurance_company_discount = insurance_company_discount
        self.insurance_centre_discount = insurance_centre_discount
        self.coupen_discount = coupen_discount
        self.all_discount = all_discount
        self.exchange_premium = exchange_premium
        self.travel_rate_plan_id = travel_rate_plan_id
        self.plan_title = plan_title
        self.travel_insurance_policy_extend_ages = travel_insurance_policy_extend_ages
        self.travel_insurance_policy_extend_passengers = travel_insurance_policy_extend_passengers
        self.zone_ids = zone_ids


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
        insurance_policy_id = dictionary.get('insurancePolicyId')
        passengers_count = dictionary.get('passengersCount')
        risk_level_discount = dictionary.get('riskLevelDiscount')
        insurance_company_discount_rate = dictionary.get('insuranceCompanyDiscountRate')
        insurance_company_discount = dictionary.get('insuranceCompanyDiscount')
        insurance_centre_discount = dictionary.get('insuranceCentreDiscount')
        coupen_discount = dictionary.get('coupenDiscount')
        all_discount = dictionary.get('allDiscount')
        exchange_premium = dictionary.get('exchangePremium')
        travel_duration_param = dictionary.get('travelDurationParam')
        birth_date = dictionary.get('birthDate')
        birth_date_persian = dictionary.get('birthDatePersian')
        base_premium = dictionary.get('basePremium')
        all_premium = dictionary.get('allPremium')
        travel_rate_plan_id = dictionary.get('travelRatePlanId')
        plan_title = dictionary.get('planTitle')
        travel_insurance_policy_extend_ages = dictionary.get('travelInsurancePolicyExtendAges')
        travel_insurance_policy_extend_passengers = dictionary.get('travelInsurancePolicyExtendPassengers')
        zone_ids = dictionary.get('zoneIds')

        # Return an object of this model
        return cls(insurance_policy_id,
                   passengers_count,
                   risk_level_discount,
                   insurance_company_discount_rate,
                   insurance_company_discount,
                   insurance_centre_discount,
                   coupen_discount,
                   all_discount,
                   exchange_premium,
                   travel_duration_param,
                   birth_date,
                   birth_date_persian,
                   base_premium,
                   all_premium,
                   travel_rate_plan_id,
                   plan_title,
                   travel_insurance_policy_extend_ages,
                   travel_insurance_policy_extend_passengers,
                   zone_ids)

