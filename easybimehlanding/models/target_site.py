# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TargetSite(object):

    """Implementation of the 'TargetSite' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        assembly_name (string): TODO: type description here.
        class_name (string): TODO: type description here.
        signature (string): TODO: type description here.
        signature_2 (string): TODO: type description here.
        member_type (int): TODO: type description here.
        generic_arguments (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "assembly_name":'AssemblyName',
        "class_name":'ClassName',
        "signature":'Signature',
        "signature_2":'Signature2',
        "member_type":'MemberType',
        "generic_arguments":'GenericArguments'
    }

    def __init__(self,
                 name=None,
                 assembly_name=None,
                 class_name=None,
                 signature=None,
                 signature_2=None,
                 member_type=None,
                 generic_arguments=None):
        """Constructor for the TargetSite class"""

        # Initialize members of the class
        self.name = name
        self.assembly_name = assembly_name
        self.class_name = class_name
        self.signature = signature
        self.signature_2 = signature_2
        self.member_type = member_type
        self.generic_arguments = generic_arguments


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
        name = dictionary.get('Name')
        assembly_name = dictionary.get('AssemblyName')
        class_name = dictionary.get('ClassName')
        signature = dictionary.get('Signature')
        signature_2 = dictionary.get('Signature2')
        member_type = dictionary.get('MemberType')
        generic_arguments = dictionary.get('GenericArguments')

        # Return an object of this model
        return cls(name,
                   assembly_name,
                   class_name,
                   signature,
                   signature_2,
                   member_type,
                   generic_arguments)


