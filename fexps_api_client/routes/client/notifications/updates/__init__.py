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


class ClientNotificationUpdateRoute(BaseRoute):
    prefix = '/updates'

    async def code(self):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/code',
        )

    async def settings(
            self,
            is_active: Optional[bool] = None,
            is_system: Optional[bool] = None,
            is_system_email: Optional[bool] = None,
            is_system_telegram: Optional[bool] = None,
            is_system_push: Optional[bool] = None,
            is_request: Optional[bool] = None,
            is_request_email: Optional[bool] = None,
            is_request_telegram: Optional[bool] = None,
            is_request_push: Optional[bool] = None,
            is_requisite: Optional[bool] = None,
            is_requisite_email: Optional[bool] = None,
            is_requisite_telegram: Optional[bool] = None,
            is_requisite_push: Optional[bool] = None,
            is_chat: Optional[bool] = None,
            is_chat_email: Optional[bool] = None,
            is_chat_telegram: Optional[bool] = None,
            is_chat_push: Optional[bool] = None,
            is_transfer: Optional[bool] = None,
            is_transfer_email: Optional[bool] = None,
            is_transfer_telegram: Optional[bool] = None,
            is_transfer_push: Optional[bool] = None,
    ):
        return await self.request(
            type_=RequestTypes.POST,
            prefix='/settings',
            parameters={
                'is_active': is_active,
                'is_system': is_system,
                'is_system_email': is_system_email,
                'is_system_telegram': is_system_telegram,
                'is_system_push': is_system_push,
                'is_request': is_request,
                'is_request_email': is_request_email,
                'is_request_telegram': is_request_telegram,
                'is_request_push': is_request_push,
                'is_requisite': is_requisite,
                'is_requisite_email': is_requisite_email,
                'is_requisite_telegram': is_requisite_telegram,
                'is_requisite_push': is_requisite_push,
                'is_chat': is_chat,
                'is_chat_email': is_chat_email,
                'is_chat_telegram': is_chat_telegram,
                'is_chat_push': is_chat_push,
                'is_transfer': is_transfer,
                'is_transfer_email': is_transfer_email,
                'is_transfer_telegram': is_transfer_telegram,
                'is_transfer_push': is_transfer_push,
            }
        )
