# coding: utf-8
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from infra_validation_engine.components.bolt import BoltInstallationTest, BoltConfigurationDirectoryTest, \
    BoltConfigurationFileTest, BoltNetworkConfigurationTest
from infra_validation_engine.components.docker import DockerInstallationTest, DockerServiceTest, DockerImageTest, \
    DockerContainerStatusTest
from infra_validation_engine.components.swarm import *
from infra_validation_engine.components.puppet import *
from infra_validation_engine.components.ccm import *
from infra_validation_engine.core import Stage, StageType


class Test(Stage):
    __metaclass__ = StageType

    def __init__(self, config_master_host, lightweight_component_hosts):
        Stage.__init__(self, "Test", config_master_host, lightweight_component_hosts)

    def register_tests(self):
        # self.infra_tests.extend([
        #     BoltInstallationTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     BoltConfigurationDirectoryTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     BoltConfigurationFileTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     BoltNetworkConfigurationTest(self.config_master_host['host'], self.config_master_host['fqdn'],
        #                                  self.lightweight_component_hosts),
        # ])

        # self.infra_tests.extend([
        #     DockerInstallationTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     DockerServiceTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     DockerImageTest(self.config_master_host['host'], self.config_master_host['fqdn'], image="maany/*"),
        #     DockerContainerStatusTest(self.config_master_host['host'], self.config_master_host['fqdn'],
        #                               container="condor_cm"),
        # ])

        # self.infra_tests.extend([
        #     SwarmDNSFileTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        #     SwarmOverlayNetworkTest(self.config_master_host['host'], self.config_master_host['fqdn'])
        # ])

        self.infra_tests.extend([
            PuppetAgentInstalledTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            PuppetAgentActiveTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            PuppetServerInstalledTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            PuppetServerActiveTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            PuppetModuleTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            PuppetSimpleDirTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            FileServerConfTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        ])

        for lc in self.lightweight_component_hosts:
            self.infra_tests.extend([
                PuppetConfTest(lc['host'], lc['fqdn'], self.config_master_host['host']),
                PuppetAgentInstalledTest(lc['host'], lc['fqdn']),
                PuppetAgentActiveTest(lc['host'], lc['fqdn']),
                PuppetModuleTest(lc['host'], lc['fqdn']),
            ])

        self.infra_tests.extend([
            SimpleConfDirTest(self.config_master_host['host'], self.config_master_host['fqdn']),
            AugSiteConfTest(self.config_master_host['host'], self.config_master_host['fqdn']),
        ])