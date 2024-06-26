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


from fexps_api_client.utils import BaseRoute, RequestTypes


class ClientRequisiteUpdateRoute(BaseRoute):
    prefix = '/updates'

    async def enable(self, id_: int):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/enable',
            parameters={
                'id_': id_,
            },
        )

    async def stop(self, id_: int):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/stop',
            parameters={
                'id_': id_,
            },
        )

    async def disable(self, id_: int):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/disable',
            parameters={
                'id_': id_,
            },
        )

    async def value(self, id_: int, currency_value: int, ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/value',
            parameters={
                'id_': id_,
                'currency_value': currency_value,
            },
        )
