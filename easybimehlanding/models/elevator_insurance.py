# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.combo_data_model
import easybimehlanding.models.elevator_type
import easybimehlanding.models.defect_organ_coverage
import easybimehlanding.models.death_capital_coverage
import easybimehlanding.models.financial_coverage
import easybimehlanding.models.medical_cost_coverage
import easybimehlanding.models.insurance_risk_level
import easybimehlanding.models.insurance_policy_term
import easybimehlanding.models.insurance_company
import easybimehlanding.models.province
import easybimehlanding.models.shipping_type
import easybimehlanding.models.post_type
import easybimehlanding.models.insurance_policy_condition
import easybimehlanding.models.insurance_data_elevator_insurance

class ElevatorInsurance(object):

    """Implementation of the 'ElevatorInsurance' model.

    TODO: type model description here.

    Attributes:
        has_plan (bool): TODO: type description here.
        building_use_types (list of ComboDataModel): TODO: type description
            here.
        elevator_types (list of ElevatorType): TODO: type description here.
        defect_organ_coverage (list of DefectOrganCoverage): TODO: type
            description here.
        death_capital_coverage (list of DeathCapitalCoverage): TODO: type
            description here.
        financial_coverage (list of FinancialCoverage): TODO: type description
            here.
        medical_cost_coverage (list of MedicalCostCoverage): TODO: type
            description here.
        insurance_risk_levels (list of InsuranceRiskLevel): TODO: type
            description here.
        insurance_policy_terms (list of InsurancePolicyTerm): TODO: type
            description here.
        insurance_companies (list of InsuranceCompany): TODO: type description
            here.
        provinces (list of Province): TODO: type description here.
        cities (list of string): TODO: type description here.
        city_regions (list of string): TODO: type description here.
        shipping_types (list of ShippingType): TODO: type description here.
        post_types (list of PostType): TODO: type description here.
        insurance_policy_condition (InsurancePolicyCondition): TODO: type
            description here.
        insurance_data (InsuranceDataElevatorInsurance): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_plan":'hasPlan',
        "building_use_types":'buildingUseTypes',
        "elevator_types":'elevatorTypes',
        "defect_organ_coverage":'defectOrganCoverage',
        "death_capital_coverage":'deathCapitalCoverage',
        "financial_coverage":'financialCoverage',
        "medical_cost_coverage":'medicalCostCoverage',
        "insurance_risk_levels":'insuranceRiskLevels',
        "insurance_policy_terms":'insurancePolicyTerms',
        "insurance_companies":'insuranceCompanies',
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
                 building_use_types=None,
                 elevator_types=None,
                 defect_organ_coverage=None,
                 death_capital_coverage=None,
                 financial_coverage=None,
                 medical_cost_coverage=None,
                 insurance_risk_levels=None,
                 insurance_policy_terms=None,
                 insurance_companies=None,
                 provinces=None,
                 cities=None,
                 city_regions=None,
                 shipping_types=None,
                 post_types=None,
                 insurance_policy_condition=None,
                 insurance_data=None):
        """Constructor for the ElevatorInsurance class"""

        # Initialize members of the class
        self.has_plan = has_plan
        self.building_use_types = building_use_types
        self.elevator_types = elevator_types
        self.defect_organ_coverage = defect_organ_coverage
        self.death_capital_coverage = death_capital_coverage
        self.financial_coverage = financial_coverage
        self.medical_cost_coverage = medical_cost_coverage
        self.insurance_risk_levels = insurance_risk_levels
        self.insurance_policy_terms = insurance_policy_terms
        self.insurance_companies = insurance_companies
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
        building_use_types = None
        if dictionary.get('buildingUseTypes') != None:
            building_use_types = list()
            for structure in dictionary.get('buildingUseTypes'):
                building_use_types.append(easybimehlanding.models.combo_data_model.ComboDataModel.from_dictionary(structure))
        elevator_types = None
        if dictionary.get('elevatorTypes') != None:
            elevator_types = list()
            for structure in dictionary.get('elevatorTypes'):
                elevator_types.append(easybimehlanding.models.elevator_type.ElevatorType.from_dictionary(structure))
        defect_organ_coverage = None
        if dictionary.get('defectOrganCoverage') != None:
            defect_organ_coverage = list()
            for structure in dictionary.get('defectOrganCoverage'):
                defect_organ_coverage.append(easybimehlanding.models.defect_organ_coverage.DefectOrganCoverage.from_dictionary(structure))
        death_capital_coverage = None
        if dictionary.get('deathCapitalCoverage') != None:
            death_capital_coverage = list()
            for structure in dictionary.get('deathCapitalCoverage'):
                death_capital_coverage.append(easybimehlanding.models.death_capital_coverage.DeathCapitalCoverage.from_dictionary(structure))
        financial_coverage = None
        if dictionary.get('financialCoverage') != None:
            financial_coverage = list()
            for structure in dictionary.get('financialCoverage'):
                financial_coverage.append(easybimehlanding.models.financial_coverage.FinancialCoverage.from_dictionary(structure))
        medical_cost_coverage = None
        if dictionary.get('medicalCostCoverage') != None:
            medical_cost_coverage = list()
            for structure in dictionary.get('medicalCostCoverage'):
                medical_cost_coverage.append(easybimehlanding.models.medical_cost_coverage.MedicalCostCoverage.from_dictionary(structure))
        insurance_risk_levels = None
        if dictionary.get('insuranceRiskLevels') != None:
            insurance_risk_levels = list()
            for structure in dictionary.get('insuranceRiskLevels'):
                insurance_risk_levels.append(easybimehlanding.models.insurance_risk_level.InsuranceRiskLevel.from_dictionary(structure))
        insurance_policy_terms = None
        if dictionary.get('insurancePolicyTerms') != None:
            insurance_policy_terms = list()
            for structure in dictionary.get('insurancePolicyTerms'):
                insurance_policy_terms.append(easybimehlanding.models.insurance_policy_term.InsurancePolicyTerm.from_dictionary(structure))
        insurance_companies = None
        if dictionary.get('insuranceCompanies') != None:
            insurance_companies = list()
            for structure in dictionary.get('insuranceCompanies'):
                insurance_companies.append(easybimehlanding.models.insurance_company.InsuranceCompany.from_dictionary(structure))
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
        insurance_data = easybimehlanding.models.insurance_data_elevator_insurance.InsuranceDataElevatorInsurance.from_dictionary(dictionary.get('insuranceData')) if dictionary.get('insuranceData') else None

        # Return an object of this model
        return cls(has_plan,
                   building_use_types,
                   elevator_types,
                   defect_organ_coverage,
                   death_capital_coverage,
                   financial_coverage,
                   medical_cost_coverage,
                   insurance_risk_levels,
                   insurance_policy_terms,
                   insurance_companies,
                   provinces,
                   cities,
                   city_regions,
                   shipping_types,
                   post_types,
                   insurance_policy_condition,
                   insurance_data)


