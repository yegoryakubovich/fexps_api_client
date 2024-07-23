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


from typing import Optional

from fexps_api_client.utils import BaseRoute, RequestTypes
from .values import AdminCommissionPackValueRoute


class AdminCommissionPackRoute(BaseRoute):
    prefix = '/commissions/packs'

    values: AdminCommissionPackValueRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.values = AdminCommissionPackValueRoute(url=self.url, token=token, deviation=deviation)

    async def create(
            self,
            name: str,
            telegram_chat_id: Optional[int] = None,
            telegram_type: Optional[str] = None,
            is_default: bool = False,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'name': name,
                'telegram_chat_id': telegram_chat_id,
                'telegram_type': telegram_type,
                'is_default': is_default,
            },
            response_key='id',
        )

    async def get(self, id_: int):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/get',
            parameters={
                'id_': id_,
            },
            response_key='commission_pack',
        )

    async def get_list(self):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/list/get',
            response_key='commissions_packs',
        )

    async def update(
            self,
            id_: int,
            name: str,
            telegram_chat_id: Optional[int] = None,
            telegram_type: Optional[str] = None,
            is_default: bool = False,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/update',
            parameters={
                'id_': id_,
                'name': name,
                'telegram_chat_id': telegram_chat_id,
                'telegram_type': telegram_type,
                'is_default': is_default,
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
