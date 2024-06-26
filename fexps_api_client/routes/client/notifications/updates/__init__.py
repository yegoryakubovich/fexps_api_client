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


class ClientNotificationUpdateRoute(BaseRoute):
    prefix = '/updates'

    async def code(self):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/code',
        )

    async def settings(
            self,
            is_request: bool,
            is_requisite: bool,
            is_order: bool,
            is_chat: bool,
            is_transfer: bool,
            is_global: bool,
            is_active: bool,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/settings',
            parameters={
                'is_request': is_request,
                'is_requisite': is_requisite,
                'is_order': is_order,
                'is_chat': is_chat,
                'is_transfer': is_transfer,
                'is_global': is_global,
                'is_active': is_active,
            }
        )
