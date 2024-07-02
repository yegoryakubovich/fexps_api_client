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


from fexps_api_client.utils import BaseRoute
from .files import TaskRateRoute
from .requests import TaskRequestRoute
from .telegrams import TaskTelegramRoute


class TaskRoute(BaseRoute):
    prefix = '/task'

    files: TaskRateRoute
    requests: TaskRequestRoute
    telegrams: TaskTelegramRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.files = TaskRateRoute(url=self.url, token=token, deviation=deviation)
        self.requests = TaskRequestRoute(url=self.url, token=token, deviation=deviation)
        self.telegrams = TaskTelegramRoute(url=self.url, token=token, deviation=deviation)
