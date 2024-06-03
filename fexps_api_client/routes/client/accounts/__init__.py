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
from .contacts import ClientAccountContactRoute


class ClientAccountRoute(BaseRoute):
    prefix = '/accounts'

    contacts: ClientAccountContactRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.contacts = ClientAccountContactRoute(url=self.url, token=token, deviation=deviation)

    async def create(
            self,
            username: str,
            password: str,
            firstname: str,
            lastname: str,
            country: str,
            language: str,
            timezone: str,
            currency: str,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/create',
            token_required=False,
            parameters={
                'username': username,
                'password': password,
                'firstname': firstname,
                'lastname': lastname,
                'country': country,
                'language': language,
                'timezone': timezone,
                'currency': currency,
            },
            response_key='id',
        )

    async def get(self):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/get',
            response_key='account',
        )

    async def change_password(
            self,
            account_id: int,
            current_password: str,
            new_password: str,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/password/change',
            parameters={
                'account_id': account_id,
                'current_password': current_password,
                'new_password': new_password,
            },
        )

    async def check_username(self, username: str):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/username/check',
            token_required=False,
            parameters={
                'username': username,
            },
        )

    async def check_password(self, password: str):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/password/check',
            token_required=False,
            parameters={
                'password': password,
            },
        )
