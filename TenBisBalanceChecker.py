import requests

BASE_URL = "https://www.10bis.co.il/NextApi/UserTransactionsReport?userToken={token}&culture=he-IL&uiCulture=he&timestamp=1576487144328&dateBias=0"


class TenBisBalanceChecker:
    def __init__(self, token):
        self.token = token
        self.get_ten_bis_balance_url = BASE_URL.format(token=self.token)

    def check_balance(self):
        get_balance_request = requests.get(url=self.get_ten_bis_balance_url)
        request_data = get_balance_request.json()["Data"]
        daily_balance = request_data["moneycards"][0]["balance"]["daily"]
        return daily_balance


ten_bis_balance_checker = TenBisBalanceChecker("ghiRE83P%2BsninB00A5Glow%3D%3D")
ten_bis_balance_checker.check_balance()