from distutils.command.config import config
import requests
from django.conf import settings

def resolve_account_name(**query):
    headers = {"Authorization": "Bearer sk_test_7dd23004a473e3317521b2cc4f57ac259805be58"}
    url = "https://api.paystack.co/bank/resolve"
    response = requests.get(url, headers=headers, params=query, timeout=10, verify=True)
    if not response.ok:
        raise Exception()
    return response.json().get('data').get('account_name')