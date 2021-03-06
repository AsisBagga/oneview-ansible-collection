#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Copyright (2016-2019) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from ansible_collections.hpe.oneview.tests.unit.utils.hpe_test_utils import OneViewBaseFactsTest
from ansible_collections.hpe.oneview.tests.unit.utils.oneview_module_loader import InterconnectTypeFactsModule

ERROR_MSG = 'Fake message error'

PARAMS_GET_ALL = dict(
    config='config.json',
    name=None
)

PARAMS_GET_BY_NAME = dict(
    config='config.json',
    name="HP VC Flex-10 Enet Module"
)

PRESENT_TYPES = [{
    "name": "HP VC Flex-10 Enet Module",
    "uri": "/rest/interconnect-types/e6d938ac-0588-44c9-95f2-610f3da4a941"
}]


@pytest.mark.resource(TestInterconnectTypeFactsModule='interconnect_types')
class TestInterconnectTypeFactsModule(OneViewBaseFactsTest):
    def test_should_get_all_interconnect_types(self):
        self.resource.get_all.return_value = PRESENT_TYPES

        self.mock_ansible_module.params = PARAMS_GET_ALL

        InterconnectTypeFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(interconnect_types=(PRESENT_TYPES))
        )

    def test_should_get_interconnect_type_by_name(self):
        self.resource.get_by.return_value = PRESENT_TYPES

        self.mock_ansible_module.params = PARAMS_GET_BY_NAME

        InterconnectTypeFactsModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=False,
            ansible_facts=dict(interconnect_types=(PRESENT_TYPES))
        )


if __name__ == '__main__':
    pytest.main([__file__])
