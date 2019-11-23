# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import easybimehlanding.models.electronic_equipment_insurance_policy_extend_view
import easybimehlanding.models.electronic_equipment_insurance_policy_filter

class InsuranceData(object):

    """Implementation of the 'InsuranceData' model.

    TODO: type model description here.

    Attributes:
        electronic_equipment_insurance_policy_extend_view
            (ElectronicEquipmentInsurancePolicyExtendView): TODO: type
            description here.
        electronic_equipment_insurance_policy_filter
            (ElectronicEquipmentInsurancePolicyFilter): TODO: type description
            here.
        id (int): TODO: type description here.
        selected_insurance_policy_has_been_changed (bool): TODO: type
            description here.
        is_paymented (bool): TODO: type description here.
        payable (string): TODO: type description here.
        paymented (string): TODO: type description here.
        conflict (string): TODO: type description here.
        has_conflict_document (bool): TODO: type description here.
        initial_price (string): TODO: type description here.
        final_price (string): TODO: type description here.
        insurance_company_name (string): TODO: type description here.
        insurance_centre_name (string): TODO: type description here.
        is_insurance_centre_admin (bool): TODO: type description here.
        insurance_policy_payment_documents (list of string): TODO: type
            description here.
        insurance_policy_conflict (string): TODO: type description here.
        insurance_policy_condition (string): TODO: type description here.
        person (string): TODO: type description here.
        insurance_policy (string): TODO: type description here.
        shopping_card (string): TODO: type description here.
        shopping_card_postal_packet (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "electronic_equipment_insurance_policy_extend_view":'electronicEquipmentInsurancePolicyExtendView',
        "electronic_equipment_insurance_policy_filter":'electronicEquipmentInsurancePolicyFilter',
        "id":'id',
        "selected_insurance_policy_has_been_changed":'selectedInsurancePolicyHasBeenChanged',
        "is_paymented":'isPaymented',
        "has_conflict_document":'hasConflictDocument',
        "is_insurance_centre_admin":'isInsuranceCentreAdmin',
        "insurance_policy_payment_documents":'insurancePolicyPaymentDocuments',
        "payable":'payable',
        "paymented":'paymented',
        "conflict":'conflict',
        "initial_price":'initialPrice',
        "final_price":'finalPrice',
        "insurance_company_name":'insuranceCompanyName',
        "insurance_centre_name":'insuranceCentreName',
        "insurance_policy_conflict":'insurancePolicyConflict',
        "insurance_policy_condition":'insurancePolicyCondition',
        "person":'person',
        "insurance_policy":'insurancePolicy',
        "shopping_card":'shoppingCard',
        "shopping_card_postal_packet":'shoppingCardPostalPacket'
    }

    def __init__(self,
                 electronic_equipment_insurance_policy_extend_view=None,
                 electronic_equipment_insurance_policy_filter=None,
                 id=None,
                 selected_insurance_policy_has_been_changed=None,
                 is_paymented=None,
                 has_conflict_document=None,
                 is_insurance_centre_admin=None,
                 insurance_policy_payment_documents=None,
                 payable=None,
                 paymented=None,
                 conflict=None,
                 initial_price=None,
                 final_price=None,
                 insurance_company_name=None,
                 insurance_centre_name=None,
                 insurance_policy_conflict=None,
                 insurance_policy_condition=None,
                 person=None,
                 insurance_policy=None,
                 shopping_card=None,
                 shopping_card_postal_packet=None):
        """Constructor for the InsuranceData class"""

        # Initialize members of the class
        self.electronic_equipment_insurance_policy_extend_view = electronic_equipment_insurance_policy_extend_view
        self.electronic_equipment_insurance_policy_filter = electronic_equipment_insurance_policy_filter
        self.id = id
        self.selected_insurance_policy_has_been_changed = selected_insurance_policy_has_been_changed
        self.is_paymented = is_paymented
        self.payable = payable
        self.paymented = paymented
        self.conflict = conflict
        self.has_conflict_document = has_conflict_document
        self.initial_price = initial_price
        self.final_price = final_price
        self.insurance_company_name = insurance_company_name
        self.insurance_centre_name = insurance_centre_name
        self.is_insurance_centre_admin = is_insurance_centre_admin
        self.insurance_policy_payment_documents = insurance_policy_payment_documents
        self.insurance_policy_conflict = insurance_policy_conflict
        self.insurance_policy_condition = insurance_policy_condition
        self.person = person
        self.insurance_policy = insurance_policy
        self.shopping_card = shopping_card
        self.shopping_card_postal_packet = shopping_card_postal_packet


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
        electronic_equipment_insurance_policy_extend_view = easybimehlanding.models.electronic_equipment_insurance_policy_extend_view.ElectronicEquipmentInsurancePolicyExtendView.from_dictionary(dictionary.get('electronicEquipmentInsurancePolicyExtendView')) if dictionary.get('electronicEquipmentInsurancePolicyExtendView') else None
        electronic_equipment_insurance_policy_filter = easybimehlanding.models.electronic_equipment_insurance_policy_filter.ElectronicEquipmentInsurancePolicyFilter.from_dictionary(dictionary.get('electronicEquipmentInsurancePolicyFilter')) if dictionary.get('electronicEquipmentInsurancePolicyFilter') else None
        id = dictionary.get('id')
        selected_insurance_policy_has_been_changed = dictionary.get('selectedInsurancePolicyHasBeenChanged')
        is_paymented = dictionary.get('isPaymented')
        has_conflict_document = dictionary.get('hasConflictDocument')
        is_insurance_centre_admin = dictionary.get('isInsuranceCentreAdmin')
        insurance_policy_payment_documents = dictionary.get('insurancePolicyPaymentDocuments')
        payable = dictionary.get('payable')
        paymented = dictionary.get('paymented')
        conflict = dictionary.get('conflict')
        initial_price = dictionary.get('initialPrice')
        final_price = dictionary.get('finalPrice')
        insurance_company_name = dictionary.get('insuranceCompanyName')
        insurance_centre_name = dictionary.get('insuranceCentreName')
        insurance_policy_conflict = dictionary.get('insurancePolicyConflict')
        insurance_policy_condition = dictionary.get('insurancePolicyCondition')
        person = dictionary.get('person')
        insurance_policy = dictionary.get('insurancePolicy')
        shopping_card = dictionary.get('shoppingCard')
        shopping_card_postal_packet = dictionary.get('shoppingCardPostalPacket')

        # Return an object of this model
        return cls(electronic_equipment_insurance_policy_extend_view,
                   electronic_equipment_insurance_policy_filter,
                   id,
                   selected_insurance_policy_has_been_changed,
                   is_paymented,
                   has_conflict_document,
                   is_insurance_centre_admin,
                   insurance_policy_payment_documents,
                   payable,
                   paymented,
                   conflict,
                   initial_price,
                   final_price,
                   insurance_company_name,
                   insurance_centre_name,
                   insurance_policy_conflict,
                   insurance_policy_condition,
                   person,
                   insurance_policy,
                   shopping_card,
                   shopping_card_postal_packet)

