import requests

from devine.BamSDK.services.account import Account
from devine.BamSDK.services.bamIdentity import BamIdentity
from devine.BamSDK.services.content import Content
from devine.BamSDK.services.device import Device
from devine.BamSDK.services.drm import DRM
from devine.BamSDK.services.media import Media
from devine.BamSDK.services.session import Session
from devine.BamSDK.services.token import Token


class BamSdk:
    def __init__(self, endpoint, session_=None):
        self._session = session_ or requests.Session()

        self.config = self._session.get(endpoint).json()
        self.application = self.config["application"]
        self.commonHeaders = self.config["commonHeaders"]

        self.account = Account(self.config["services"]["account"], self._session)
        self.bamIdentity = BamIdentity(
            self.config["services"]["bamIdentity"], self._session
        )
        self.content = Content(self.config["services"]["content"], self._session)
        self.device = Device(self.config["services"]["device"], self._session)
        self.drm = DRM(self.config["services"]["drm"], self._session)
        self.media = Media(self.config["services"]["media"], self._session)
        self.session = Session(self.config["services"]["session"], self._session)
        self.token = Token(self.config["services"]["token"], self._session)
