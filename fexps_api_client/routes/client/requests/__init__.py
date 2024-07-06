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
from .updates import ClientRequestUpdateRoute


class ClientRequestRoute(BaseRoute):
    prefix = '/requests'

    updates: ClientRequestUpdateRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.updates = ClientRequestUpdateRoute(url=self.url, token=token, deviation=deviation)

    async def create(
            self,
            wallet_id: int,
            type_: str,
            name: str,
            input_method_id: int = None,
            output_requisite_data_id: int = None,
            input_value: int = None,
            output_value: int = None,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'wallet_id': wallet_id,
                'type_': type_,
                'name': name,
                'input_method_id': input_method_id,
                'output_requisite_data_id': output_requisite_data_id,
                'input_value': input_value,
                'output_value': output_value,
            },
            response_key='id',
        )

    async def calculate(
            self,
            wallet_id: int,
            type_: str,
            input_method_id: int = None,
            output_method_id: int = None,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/calculate',
            parameters={
                'wallet_id': wallet_id,
                'type_': type_,
                'input_method_id': input_method_id,
                'output_method_id': output_method_id,
            },
        )

    async def get(
            self,
            id_: int,
    ):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/get',
            parameters={
                'id_': id_,
            },
            response_key='request',
        )

    async def search(
            self,
            id_: Optional[str] = None,
            is_active: bool = False,
            is_completed: bool = False,
            is_canceled: bool = False,
            is_partner: bool = False,
            page: int = 1,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/search',
            parameters={
                'id_': id_,
                'is_active': is_active,
                'is_completed': is_completed,
                'is_canceled': is_canceled,
                'is_partner': is_partner,
                'page': page,
            },
        )
