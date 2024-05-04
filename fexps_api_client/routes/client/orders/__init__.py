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
from .get_list import ClientOrderListGetRoute
from .requests import ClientOrderRequestRoute
from .updates import ClientOrderUpdateRoute


class ClientOrderRoute(BaseRoute):
    prefix = '/orders'

    list_get: ClientOrderListGetRoute
    updates: ClientOrderUpdateRoute
    requests: ClientOrderRequestRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.list_get = ClientOrderListGetRoute(url=self.url, token=token, deviation=deviation)
        self.updates = ClientOrderUpdateRoute(url=self.url, token=token, deviation=deviation)
        self.requests = ClientOrderRequestRoute(url=self.url, token=token, deviation=deviation)

    async def get(self, id_):
        return await self.request(
            type_=RequestTypes.GET,
            prefix='/get',
            parameters={
                'id_': id_,
            },
            response_key='order',
        )
