# -*- coding: utf-8 -*-

"""
    easybimehlanding

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from easybimehlanding.api_helper import APIHelper


class MotorcycleInsuranceControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MotorcycleInsuranceControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.motorcycle_insurance

