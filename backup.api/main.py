from amadeus import Client, ResponseError
from envrions import API_KEY, API_SECRET
import requests

from datetime import datetime, timedelta, timezone


class AmadeusAPI:

    def set_auth_to_session(self):
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.token['access_token']}",
            }
        )

    @property
    def get_token(self):

        return {
            "type": "amadeusOAuth2Token",
            "username": "qmssoftlab@gmail.com",
            "application_name": "first app",
            "client_id": "ECnxgFlA8NG1rolz4kGnHAKKSEZKJOrA",
            "token_type": "Bearer",
            "access_token": "VNHl43bx6Dy1S9fGGMuTZx5NVk0h",
            "expires_in": 1799,
            "state": "approved",
            "scope": "",
        }

        """Amadeus API dan access token olish"""
        # access token uchun request chiqarish
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data=f"grant_type=client_credentials&client_id={self.API_KEY}&client_secret={self.API_SECRET}",
        )

        # sessiani tekshrish && reject bo'lsa Error yaratish
        if response.status_code != 200:
            print(response.text)
            print(response.content)
            print(response.status_code)
            print(
                f"API KEY: {self.API_KEY}\nAPI TOKEN: {self.API_SECRET}\nXatolik api tokenlarni xato"
            )
            return

        data = response.json()
        print("🚀 ~ file: main.py:35 ~ data:", data)

        self.set_auth_to_session()

        # success bo'lsa session qaytarish
        return data

    @staticmethod
    def auth(func):
        def wrapper(self, *args, **kwargs):
            # amal qilish tugagan bo'lsa tokeni yangiliash
            expiry_time = datetime.utcnow(timezone.utc) + timedelta(
                seconds=self.token["expires_in"]
            )
            current_time = datetime.utcnow(timezone.utc)

            if current_time > expiry_time:
                self.token = self.get_token
                self.set_auth_to_session(self.token["access_token"])

            return func(self, *args, **kwargs)

        return wrapper

    @auth
    def test(self):
        print("test fun is running")

    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.session = requests.Session()
        self.token = self.get_token


# 🔹 Obyekt yaratamiz va chipta narxlarini olamiz
amadeus = AmadeusAPI(API_KEY, API_SECRET)
amadeus.test()
