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
from .updates import ClientRequisiteUpdateRoute


class ClientRequisiteRoute(BaseRoute):
    prefix = '/requisites'

    updates: ClientRequisiteUpdateRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.updates = ClientRequisiteUpdateRoute(url=self.url, token=token, deviation=deviation)

    async def create(
            self,
            wallet_id: int,
            type_: str,
            output_requisite_data_id: int = None,
            input_method_id: int = None,
            currency_value: int = None,
            currency_value_min: int = None,
            currency_value_max: int = None,
            rate: int = None,
            value: int = None,
            is_flex: bool = False,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'wallet_id': wallet_id,
                'type_': type_,
                'output_requisite_data_id': output_requisite_data_id,
                'input_method_id': input_method_id,
                'currency_value': currency_value,
                'currency_value_min': currency_value_min,
                'currency_value_max': currency_value_max,
                'rate': rate,
                'value': value,
                'is_flex': is_flex,
            },
            response_key='id',
        )

    async def get(self, id_):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/get',
            parameters={
                'id_': id_,
            },
            response_key='requisite',
        )

    async def search(
            self,
            is_type_input: bool = True,
            is_type_output: bool = True,
            is_state_enable: bool = True,
            is_state_stop: bool = False,
            is_state_disable: bool = False,
            page: int = 1,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/search',
            parameters={
                'is_type_input': is_type_input,
                'is_type_output': is_type_output,
                'is_state_enable': is_state_enable,
                'is_state_stop': is_state_stop,
                'is_state_disable': is_state_disable,
                'page': page,
            },
        )
