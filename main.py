from requests import get
# installed requests
base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    print(response.text)