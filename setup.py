from setuptools import setup

# Copyright 2013-present Barefoot Networks, Inc. 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

setup(
    name = 'p4c_dot',
    version = '0.9.1',
    packages=['p4c_dot',],
    package_data = {},
    entry_points = {
        'console_scripts': ['p4c-dot=p4c_dot.shell:main'],
        'console_scripts': ['p4c-graphs=p4c_dot.shell:main'],
    },
    author = 'Antonin BAS',
    author_email = 'antonin@barefootnetworks.com',
    description = 'p4c_dot: P4 compiler for the dot target',
    license = '',
    url = 'http://www.barefootnetworks.com/',
)
