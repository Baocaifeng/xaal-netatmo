


ClientId="5a8104e4316480ec308b558c"
ClientSecret="NggoWVzGcJdJGRSaJMyp7f3gaMFGxDC4FM"
UserEmail="caifeng.bao@imt-atlantique.net"
UserPassword="Bcf18792478408"

#This code sample uses requests (HTTP library)
import requests

payload = {'grant_type': 'password',
           'username': UserEmail,
           'password': UserPassword,
           'client_id': ClientId,
           'client_secret': ClientSecret,
           'scope': 'read_station'}

try:
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
    print("Your access token is:", access_token)
    print("Your refresh token is:", refresh_token)
    print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)
