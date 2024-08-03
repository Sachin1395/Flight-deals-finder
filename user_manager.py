import requests
url="xxxx"
def post_new_row(first_name, last_name, email):
    body = {
        "sheet3": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=url, json=body)
    response.raise_for_status()
    print(response.text)

post_new_row("sc","hin","sac123")