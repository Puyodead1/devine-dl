import json

from requests import Request

from devine.BamSDK.services import Service


# noinspection PyPep8Naming
class DRM(Service):
    def widevineCertificate(self):
        endpoint = self.client.endpoints["widevineCertificate"]
        req = Request(
            method=endpoint.method, url=endpoint.href, headers=endpoint.headers
        ).prepare()
        res = self.session.send(req)
        return res.content

    def widevineLicense(self, licence, access_token):
        endpoint = self.client.endpoints["widevineLicense"]
        req = Request(
            method=endpoint.method,
            url=endpoint.href,
            headers=endpoint.get_headers(accessToken=access_token),
            data=licence,
        ).prepare()
        res = self.session.send(req)
        try:
            # if it's json content, then an error occurred
            res = json.loads(res.text)
            raise Exception(f"Failed to obtain license: {res}")
        except json.JSONDecodeError:
            return res.content

    def playreadyLicense(self, licence, access_token):
        endpoint = self.client.endpoints["playReadyLicense"]
        req = Request(
            method=endpoint.method,
            url=endpoint.href,
            headers=endpoint.get_headers(accessToken=access_token),
            data=licence,
        ).prepare()
        res = self.session.send(req)
        try:
            # if it's json content, then an error occurred
            res = json.loads(res.text)
            raise Exception(f"Failed to obtain license: {res}")
        except json.JSONDecodeError:
            return res.content
