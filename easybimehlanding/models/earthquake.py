# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.combo_data_model
import easybimehlanding.models.insurance_policy_term
import easybimehlanding.models.every_square_meter_coverage
import easybimehlanding.models.province
import easybimehlanding.models.shipping_type
import easybimehlanding.models.post_type
import easybimehlanding.models.insurance_policy_condition
import easybimehlanding.models.insurance_data_fire_insurance

class Earthquake(object):

    """Implementation of the 'Earthquake' model.

    TODO: type model description here.

    Attributes:
        has_plan (bool): TODO: type description here.
        insurance_centre_province_id (int): TODO: type description here.
        insurance_centre_city_id (int): TODO: type description here.
        insurance_centre_cities (list of ComboDataModel): TODO: type
            description here.
        building_types (list of ComboDataModel): TODO: type description here.
        skeleton_type_buildings (list of ComboDataModel): TODO: type
            description here.
        building_use_types (list of ComboDataModel): TODO: type description
            here.
        insurance_policy_terms (list of InsurancePolicyTerm): TODO: type
            description here.
        insurance_extra_coverage (list of string): TODO: type description
            here.
        every_square_meter_coverage (list of EverySquareMeterCoverage): TODO:
            type description here.
        provinces (list of Province): TODO: type description here.
        cities (list of string): TODO: type description here.
        city_regions (list of string): TODO: type description here.
        shipping_types (list of ShippingType): TODO: type description here.
        post_types (list of PostType): TODO: type description here.
        insurance_policy_condition (InsurancePolicyCondition): TODO: type
            description here.
        insurance_data (InsuranceDataFireInsurance): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_plan":'hasPlan',
        "insurance_centre_province_id":'insuranceCentreProvinceId',
        "insurance_centre_city_id":'insuranceCentreCityId',
        "insurance_centre_cities":'insuranceCentreCities',
        "building_types":'buildingTypes',
        "skeleton_type_buildings":'skeletonTypeBuildings',
        "building_use_types":'buildingUseTypes',
        "insurance_policy_terms":'insurancePolicyTerms',
        "insurance_extra_coverage":'insuranceExtraCoverage',
        "every_square_meter_coverage":'everySquareMeterCoverage',
        "provinces":'provinces',
        "cities":'cities',
        "city_regions":'cityRegions',
        "shipping_types":'shippingTypes',
        "post_types":'postTypes',
        "insurance_policy_condition":'insurancePolicyCondition',
        "insurance_data":'insuranceData'
    }

    def __init__(self,
                 has_plan=None,
                 insurance_centre_province_id=None,
                 insurance_centre_city_id=None,
                 insurance_centre_cities=None,
                 building_types=None,
                 skeleton_type_buildings=None,
                 building_use_types=None,
                 insurance_policy_terms=None,
                 insurance_extra_coverage=None,
                 every_square_meter_coverage=None,
                 provinces=None,
                 cities=None,
                 city_regions=None,
                 shipping_types=None,
                 post_types=None,
                 insurance_policy_condition=None,
                 insurance_data=None):
        """Constructor for the Earthquake class"""

        # Initialize members of the class
        self.has_plan = has_plan
        self.insurance_centre_province_id = insurance_centre_province_id
        self.insurance_centre_city_id = insurance_centre_city_id
        self.insurance_centre_cities = insurance_centre_cities
        self.building_types = building_types
        self.skeleton_type_buildings = skeleton_type_buildings
        self.building_use_types = building_use_types
        self.insurance_policy_terms = insurance_policy_terms
        self.insurance_extra_coverage = insurance_extra_coverage
        self.every_square_meter_coverage = every_square_meter_coverage
        self.provinces = provinces
        self.cities = cities
        self.city_regions = city_regions
        self.shipping_types = shipping_types
        self.post_types = post_types
        self.insurance_policy_condition = insurance_policy_condition
        self.insurance_data = insurance_data


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
        has_plan = dictionary.get('hasPlan')
        insurance_centre_province_id = dictionary.get('insuranceCentreProvinceId')
        insurance_centre_city_id = dictionary.get('insuranceCentreCityId')
        insurance_centre_cities = None
        if dictionary.get('insuranceCentreCities') != None:
            insurance_centre_cities = list()
            for structure in dictionary.get('insuranceCentreCities'):
                insurance_centre_cities.append(easybimehlanding.models.combo_data_model.ComboDataModel.from_dictionary(structure))
        building_types = None
        if dictionary.get('buildingTypes') != None:
            building_types = list()
            for structure in dictionary.get('buildingTypes'):
                building_types.append(easybimehlanding.models.combo_data_model.ComboDataModel.from_dictionary(structure))
        skeleton_type_buildings = None
        if dictionary.get('skeletonTypeBuildings') != None:
            skeleton_type_buildings = list()
            for structure in dictionary.get('skeletonTypeBuildings'):
                skeleton_type_buildings.append(easybimehlanding.models.combo_data_model.ComboDataModel.from_dictionary(structure))
        building_use_types = None
        if dictionary.get('buildingUseTypes') != None:
            building_use_types = list()
            for structure in dictionary.get('buildingUseTypes'):
                building_use_types.append(easybimehlanding.models.combo_data_model.ComboDataModel.from_dictionary(structure))
        insurance_policy_terms = None
        if dictionary.get('insurancePolicyTerms') != None:
            insurance_policy_terms = list()
            for structure in dictionary.get('insurancePolicyTerms'):
                insurance_policy_terms.append(easybimehlanding.models.insurance_policy_term.InsurancePolicyTerm.from_dictionary(structure))
        insurance_extra_coverage = dictionary.get('insuranceExtraCoverage')
        every_square_meter_coverage = None
        if dictionary.get('everySquareMeterCoverage') != None:
            every_square_meter_coverage = list()
            for structure in dictionary.get('everySquareMeterCoverage'):
                every_square_meter_coverage.append(easybimehlanding.models.every_square_meter_coverage.EverySquareMeterCoverage.from_dictionary(structure))
        provinces = None
        if dictionary.get('provinces') != None:
            provinces = list()
            for structure in dictionary.get('provinces'):
                provinces.append(easybimehlanding.models.province.Province.from_dictionary(structure))
        cities = dictionary.get('cities')
        city_regions = dictionary.get('cityRegions')
        shipping_types = None
        if dictionary.get('shippingTypes') != None:
            shipping_types = list()
            for structure in dictionary.get('shippingTypes'):
                shipping_types.append(easybimehlanding.models.shipping_type.ShippingType.from_dictionary(structure))
        post_types = None
        if dictionary.get('postTypes') != None:
            post_types = list()
            for structure in dictionary.get('postTypes'):
                post_types.append(easybimehlanding.models.post_type.PostType.from_dictionary(structure))
        insurance_policy_condition = easybimehlanding.models.insurance_policy_condition.InsurancePolicyCondition.from_dictionary(dictionary.get('insurancePolicyCondition')) if dictionary.get('insurancePolicyCondition') else None
        insurance_data = easybimehlanding.models.insurance_data_fire_insurance.InsuranceDataFireInsurance.from_dictionary(dictionary.get('insuranceData')) if dictionary.get('insuranceData') else None

        # Return an object of this model
        return cls(has_plan,
                   insurance_centre_province_id,
                   insurance_centre_city_id,
                   insurance_centre_cities,
                   building_types,
                   skeleton_type_buildings,
                   building_use_types,
                   insurance_policy_terms,
                   insurance_extra_coverage,
                   every_square_meter_coverage,
                   provinces,
                   cities,
                   city_regions,
                   shipping_types,
                   post_types,
                   insurance_policy_condition,
                   insurance_data)


