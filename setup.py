#
# (c) 2024, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
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
#


from os import path

from setuptools import setup, PEP420PackageFinder


NAME = 'fexps_api_client'
VERSION = '0.1'
DESCRIPTION = ''
URL = 'https://yegoryakubovich.com'
PACKAGE_ROOT = path.abspath(path.dirname(__file__))
README = open('README.md', 'r').read()

packages = [
    package
    for package in PEP420PackageFinder.find()
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    long_description=README,
    long_description_content_type='text/markdown',

    author='Yegor Yakubovich',
    author_email='personal@yegoryakubovich.com',
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',

    packages=packages,
    install_requires=['aiohttp', 'furl', 'addict'],
    include_package_data=True,
    zip_safe=False,
)
