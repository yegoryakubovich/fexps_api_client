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


from .base import ApiException


class TelegramImagePathNotFound(ApiException):
    code = 13000
    message = 'CommissionPack #{commission_pack_id} not found file {filename}'


class TelegramMessageNotFound(ApiException):
    code = 13001
    message = 'CommissionPack #{commission_pack_id} message not found'


class TelegramPostNotFound(ApiException):
    code = 13002
    message = 'CommissionPack #{commission_pack_id} not found post #{message_id}'
