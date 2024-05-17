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


class AdminMethodRoute(BaseRoute):
    prefix = '/methods'

    async def create(
            self,
            currency: str,
            name: str,
            fields: list[dict],
            input_fields: list[dict],
            rate_input_default: int,
            rate_output_default: int,
            rate_input_percent: int,
            rate_output_percent: int,
            color: str,
            bgcolor: str,
            is_rate_default: bool,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            parameters={
                'currency': currency,
                'name': name,
                'fields': fields,
                'input_fields': input_fields,
                'rate_input_default': rate_input_default,
                'rate_output_default': rate_output_default,
                'rate_input_percent': rate_input_percent,
                'rate_output_percent': rate_output_percent,
                'color': color,
                'bgcolor': bgcolor,
                'is_rate_default': is_rate_default,
            },
            response_key='id',
        )

    async def update(
            self,
            id_: int,
            currency_id_str: str = None,
            fields: list = None,
            input_fields: list = None,
            rate_input_default: int = None,
            rate_output_default: int = None,
            rate_input_percent: int = None,
            rate_output_percent: int = None,
            color: str = None,
            bgcolor: str = None,
            is_rate_default: bool = None,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/update',
            parameters={
                'id_': id_,
                'currency_id_str': currency_id_str,
                'fields': fields,
                'input_fields': input_fields,
                'rate_input_default': rate_input_default,
                'rate_output_default': rate_output_default,
                'rate_input_percent': rate_input_percent,
                'rate_output_percent': rate_output_percent,
                'color': color,
                'bgcolor': bgcolor,
                'is_rate_default': is_rate_default,
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
