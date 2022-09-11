from random_username.generate import generate_username
import requests
import random


class Duolinguo:
    def __init__(self, invitation_code="BDHTZTB5CWWKT6DUXOFYXLVSRU"):
        self.proxies = self._read_proxies()
        self.base_api = "https://duolingo.com"
        self.signup_url = "https://www.duolingo.com/2017-06-30/users?fields=id"
        self.invitation_code = invitation_code

    def _generate_psw(self, length):
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

    def _read_proxies(self):
        with open("proxies.txt", "r") as proxies:
            proxies = proxies.read().splitlines()

        return proxies

    def create_account(self):
        while True:
            try:
                with requests.session() as session:
                    uname = generate_username(1)[0]
                    rand_proxy = random.choice(self.proxies)
                    proxy = {'http': rand_proxy, 'https': rand_proxy}
                    uuid = session.get(self.base_api, proxies=proxy).cookies["wuuid"]

                    print(f"[+] Got uuid {uuid}")
                    payload = {"distinctId": uuid,
                               "timezone": "America/Los_Angeles",
                               "fromLanguage": "en",
                               "age": "20",
                               "name": uname,
                               "email": f"{uname}@gmail.com",
                               "password": self._generate_psw(20),
                               "landingUrl": "https://www.duolingo.com/",
                               "initialReferrer": "$direct",
                               "inviteCode": self.invitation_code}

                    r = session.post(self.signup_url, json=payload, proxies=proxy)

                    if r.status_code == 200:
                        print(f"[+] Created account | Id: {r.json()['id']} | Username: {uname}")
                    else:
                        print(f"[-] Failed to create account")
            except:
                pass
