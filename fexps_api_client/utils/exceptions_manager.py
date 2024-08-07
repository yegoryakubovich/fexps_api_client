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


from inspect import isclass

from fexps_api_client.utils.exceptions import ApiException
from fexps_api_client.utils.exceptions import account, commission_pack, main, method, notification, order, request, \
    requisite, role, telegram, text, wallet

groups = [account, commission_pack, main, method, notification, order, request, requisite, role, telegram, text, wallet]
exceptions = {}

for module in groups:
    for e in [e for e in [eval(f'module.{exception}') for exception in dir(module)] if isclass(e)]:
        if not issubclass(e, ApiException):
            pass
        exceptions[e.code] = e
