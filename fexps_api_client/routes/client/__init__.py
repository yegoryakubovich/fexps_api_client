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
from .accounts import ClientAccountRoute
from .contacts import ClientContactRoute
from .countries import ClientCountryRoute
from .currencies import ClientCurrencyRoute
from .files import ClientFileRoute
from .languages import ClientLanguageRoute
from .messages import ClientMessageRoute
from .methods import ClientMethodRoute
from .notifications import ClientNotificationRoute
from .orders import ClientOrderRoute
from .requests import ClientRequestRoute
from .requisites import ClientRequisiteRoute
from .requisites_datas import ClientRequisiteDataRoute
from .roles import ClientRoleRoute
from .sessions import ClientSessionRoute
from .texts import ClientTextRoute
from .timezones import ClientTimezoneRoute
from .transfers import ClientTransfersRoute
from .wallets import ClientWalletRoute


class ClientRoute(BaseRoute):
    accounts: ClientAccountRoute
    contacts: ClientContactRoute
    countries: ClientCountryRoute
    currencies: ClientCurrencyRoute
    files: ClientFileRoute
    languages: ClientLanguageRoute
    messages: ClientMessageRoute
    methods: ClientMethodRoute
    notifications: ClientNotificationRoute
    orders: ClientOrderRoute
    requests: ClientRequestRoute
    requisites: ClientRequisiteRoute
    requisites_datas: ClientRequisiteDataRoute
    roles: ClientRoleRoute
    sessions: ClientSessionRoute
    texts: ClientTextRoute
    timezones: ClientTimezoneRoute
    transfers: ClientTransfersRoute
    wallets: ClientWalletRoute

    def __init__(self, url: str, token: str = None, deviation: int = 0):
        super().__init__(url=url, token=token, deviation=deviation)
        self.accounts = ClientAccountRoute(url=self.url, token=token, deviation=deviation)
        self.contacts = ClientContactRoute(url=self.url, token=token, deviation=deviation)
        self.countries = ClientCountryRoute(url=self.url, token=token, deviation=deviation)
        self.currencies = ClientCurrencyRoute(url=self.url, token=token, deviation=deviation)
        self.files = ClientFileRoute(url=self.url, token=token, deviation=deviation)
        self.languages = ClientLanguageRoute(url=self.url, token=token, deviation=deviation)
        self.messages = ClientMessageRoute(url=self.url, token=token, deviation=deviation)
        self.methods = ClientMethodRoute(url=self.url, token=token, deviation=deviation)
        self.notifications = ClientNotificationRoute(url=self.url, token=token, deviation=deviation)
        self.orders = ClientOrderRoute(url=self.url, token=token, deviation=deviation)
        self.requests = ClientRequestRoute(url=self.url, token=token, deviation=deviation)
        self.requisites = ClientRequisiteRoute(url=self.url, token=token, deviation=deviation)
        self.requisites_datas = ClientRequisiteDataRoute(url=self.url, token=token, deviation=deviation)
        self.roles = ClientRoleRoute(url=self.url, token=token, deviation=deviation)
        self.sessions = ClientSessionRoute(url=self.url, token=token, deviation=deviation)
        self.texts = ClientTextRoute(url=self.url, token=token, deviation=deviation)
        self.timezones = ClientTimezoneRoute(url=self.url, token=token, deviation=deviation)
        self.transfers = ClientTransfersRoute(url=self.url, token=token, deviation=deviation)
        self.wallets = ClientWalletRoute(url=self.url, token=token, deviation=deviation)
