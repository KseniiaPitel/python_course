import requests

def get_location_info():
    return requests.get("https://ipstack.com/ipstack_api.php?ip=194.105.145.116").json()

if __name__ == "__main__":
    print(get_location_info())


