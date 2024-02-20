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
from .packs import ClientTextPackRoute
from .translations import ClientTextTranslationRoute


class ClientTextRoute(BaseRoute):
    prefix = '/texts'

    packs = ClientTextPackRoute()
    translations = ClientTextTranslationRoute()

    async def create(self, key: str, value_default: str):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'key': key,
                'value_default': value_default,
            },
            response_key='id',
        )

    async def get_list(self):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/list/get',
            response_key='methods',
        )

    async def update(
            self,
            key: int,
            new_key: str = None,
            value_default: str = None,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/update',
            parameters={
                'key': key,
                'new_key': new_key,
                'value_default': value_default,
            },
        )

    async def delete(self, id_: int):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/delete',
            parameters={
                'id_': id_,
            },
        )
