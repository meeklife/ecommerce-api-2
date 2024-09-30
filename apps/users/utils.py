import requests


def query_community_endpoint(email):
    url = f"https://crm-api.fly.dev/api/v1/users/user_info?email={email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None
