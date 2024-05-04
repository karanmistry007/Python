import requests


def main():
    url = "https://jsonplaceholder.typicode.com/users"
    head = {
        "Content-Type": "application-json",
    }
    response = requests.get(url, head)

    print("Hello")
    print(response.json())


main()
