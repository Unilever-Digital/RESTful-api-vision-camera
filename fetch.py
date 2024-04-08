import requests


def fetch_data():
    # Define the URL of the API endpoint
    url = 'https://unilever-api-app-vrcrf.appengine.bfcplatform.vn/qltdata/carton-bi'  # Adjust URL as needed
    data = {"key": "value"}  # Modify or remove this line as needed

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("Response from API:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.reason}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Call the function to fetch data from the API
if __name__ == "__main__":
    fetch_data()
