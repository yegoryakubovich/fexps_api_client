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
from .accounts import AdminAccountRoute
from .clients_texts import AdminClientTextRoute
from .commissions_packs import AdminCommissionPackRoute
from .contacts import AdminContactRoute
from .countries import AdminCountryRoute
from .currencies import AdminCurrencyRoute
from .files import AdminFileRoute
from .languages import AdminLanguageRoute
from .methods import AdminMethodRoute
from .orders import AdminOrderRoute
from .permissions import AdminPermissionRoute
from .roles import AdminRoleRoute
from .texts import AdminTextRoute
from .timezones import AdminTimezoneRoute
from .wallets import AdminWalletRoute


class AdminRoute(BaseRoute):
    prefix = '/admin'

    accounts: AdminAccountRoute
    clients_texts: AdminClientTextRoute
    commissions_packs: AdminCommissionPackRoute
    contacts: AdminContactRoute
    countries: AdminCountryRoute
    currencies: AdminCurrencyRoute
    files: AdminFileRoute
    languages: AdminLanguageRoute
    methods: AdminMethodRoute
    orders: AdminOrderRoute
    permissions: AdminPermissionRoute
    roles: AdminRoleRoute
    texts: AdminTextRoute
    timezones: AdminTimezoneRoute
    wallets: AdminWalletRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.accounts = AdminAccountRoute(url=self.url, token=token, deviation=deviation)
        self.clients_texts = AdminClientTextRoute(url=self.url, token=token, deviation=deviation)
        self.commissions_packs = AdminCommissionPackRoute(url=self.url, token=token, deviation=deviation)
        self.contacts = AdminContactRoute(url=self.url, token=token, deviation=deviation)
        self.countries = AdminCountryRoute(url=self.url, token=token, deviation=deviation)
        self.currencies = AdminCurrencyRoute(url=self.url, token=token, deviation=deviation)
        self.files = AdminFileRoute(url=self.url, token=token, deviation=deviation)
        self.languages = AdminLanguageRoute(url=self.url, token=token, deviation=deviation)
        self.methods = AdminMethodRoute(url=self.url, token=token, deviation=deviation)
        self.orders = AdminOrderRoute(url=self.url, token=token, deviation=deviation)
        self.permissions = AdminPermissionRoute(url=self.url, token=token, deviation=deviation)
        self.roles = AdminRoleRoute(url=self.url, token=token, deviation=deviation)
        self.texts = AdminTextRoute(url=self.url, token=token, deviation=deviation)
        self.timezones = AdminTimezoneRoute(url=self.url, token=token, deviation=deviation)
        self.wallets = AdminWalletRoute(url=self.url, token=token, deviation=deviation)
