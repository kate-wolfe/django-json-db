import requests
import time as time
import environ

env = environ.Env()
environ.Env.read_env()


def authenticate_session(session):
    session.headers = {"accept": "application/json", "Authorization": ""}

    session.cookies["expires_at"] = "0"

    if session.headers["Authorization"] == "" or float(
        session.cookies["expires_at"] < time.time()
    ):
        auth = requests.auth.HTTPBasicAuth(
            username=env("CLIENT_ID"), password=env("CLIENT_SECRET")
        )
        token_url = env("TOKEN_URL")
        data = {"grant_type": "client_credentials"}

        response = session.post(
            url=token_url,
            auth=auth,
            data=data,
        )

        if response.status_code == 200:
            session.headers["Authorization"] = (
                "Bearer " + response.json()["access_token"]
            )

            session.cookies["expires_at"] = str(
                time.time() + response.json()["expires_in"] - 60
            )
            return session
        else:
            raise Exception("Failed to obtain access token: " + response.text)
    else:
        return session


'''
token_url = env("TOKEN_URL")

session = requests.Session()

sessionauth = authenticate_session(session)

response = sessionauth.get(token_url)

print(
    f"""
      response status code:{response.status_code}
      session expires at (UNIX Epoch):{sessionauth.cookies['expires_at']}
      time now:{time.time()}
      seconds left:{float(sessionauth.cookies["expires_at"]) - time.time()}
      """
)
'''
