# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
import uuid


class ChannelTests(ScenarioTest):

    def create_bot(self, resource_group):
        self.kwargs.update({
            'botname': self.create_random_name(prefix='cli', length=10),
            'endpoint': 'https://www.google.com/api/messages',
            'app_id': str(uuid.uuid4()),
            'setting_name': self.create_random_name(prefix='auth', length=10),
            'clientid': 'clientid',
            'secret': 'secret'
        })

        self.cmd('az bot create -k registration -g {rg} -n {botname} -e {endpoint} --appid {app_id}', checks=[
            self.check('name', '{botname}'),
            self.check('resourceGroup', '{rg}'),
            self.check('location', 'global')
        ])

    @ResourceGroupPreparer(random_name_length=20)
    def test_webchat_channel(self, resource_group):
        self.create_bot(resource_group)

        self.cmd('az bot webchat show -g {rg} -n {botname}', checks=[
            self.check('properties.properties.sites.length(@)', 0),
        ])

        self.cmd('az bot webchat show -g {rg} -n {botname} --with-secrets', checks=[
            self.check('properties.properties.sites.length(@)', 1),
            self.check('properties.properties.sites[0].isEnabled', True),
        ])

    @ResourceGroupPreparer(random_name_length=20)
    def test_skype_channel(self, resource_group):
        self.create_bot(resource_group)
        self.cmd('az bot skype create -g {rg} -n {botname} --enable-calling true --enable-media-cards true --enable-messaging true --enable-video true --calling-web-hook https://www.google.com', checks=[
            self.check('properties.properties.enableMessaging', True),
            self.check('properties.properties.enableMediaCards', True),
            self.check('properties.properties.enableVideo', True)
        ])

        self.cmd('az bot skype show -g {rg} -n {botname}', checks=[
            self.check('properties.properties.enableMessaging', True),
            self.check('properties.properties.enableMediaCards', True),
            self.check('properties.properties.enableVideo', True)
        ])

        self.cmd('az bot skype show -g {rg} -n {botname} --with-secrets', checks=[
            self.check('properties.properties.enableMessaging', True),
            self.check('properties.properties.enableMediaCards', True),
            self.check('properties.properties.enableVideo', True)
        ])

        self.cmd('az bot skype delete -g {rg} -n {botname}')

    @ResourceGroupPreparer(random_name_length=20)
    def test_msteams_channel(self, resource_group):
        self.create_bot(resource_group)
        self.cmd('az bot msteams create -g {rg} -n {botname} --enable-calling true --calling-web-hook https://www.google.com', checks=[
            self.check('properties.properties.enableCalling', True),
            self.check('properties.properties.isEnabled', True)
        ])

        self.cmd('az bot msteams show -g {rg} -n {botname}', checks=[
            self.check('properties.properties.enableCalling', True),
            self.check('properties.properties.isEnabled', True)
        ])

        self.cmd('az bot msteams show -g {rg} -n {botname} --with-secrets', checks=[
            self.check('properties.properties.enableCalling', True),
            self.check('properties.properties.isEnabled', True)
        ])

        self.cmd('az bot msteams delete -g {rg} -n {botname}')

    @ResourceGroupPreparer(random_name_length=20)
    def test_directline_channel(self, resource_group):
        self.create_bot(resource_group)
        self.cmd('az bot directline create -g {rg} -n {botname}', checks=[
            self.check('properties.properties.sites[0].siteName', 'Default Site'),
            self.check('properties.properties.sites[0].isEnabled', True)
        ])

        self.cmd('az bot directline show -g {rg} -n {botname}', checks=[
            self.check('properties.properties.sites[0].siteName', 'Default Site'),
            self.check('properties.properties.sites[0].isEnabled', True),
            self.check('properties.properties.sites[0].key', '')
        ])

        self.cmd('az bot directline show -g {rg} -n {botname} --with-secrets', checks=[
            self.check('properties.properties.sites[0].siteName', 'Default Site'),
            self.check('properties.properties.sites[0].isEnabled', True)
        ])

        self.cmd('az bot directline delete -g {rg} -n {botname}')
