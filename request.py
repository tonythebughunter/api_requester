import argparse
import requests

def make_request(method, url):
    try:
        response = requests.request(method, url)
        print("Status code:", response.status_code)
        print("Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print("Error making request:", e)

def main():
    parser = argparse.ArgumentParser(description="Command line HTTP requester tool")
    parser.add_argument("method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"], help="HTTP method")
    parser.add_argument("url", nargs="?", help="URL of the resource")
    args = parser.parse_args()

    if not args.url:
        args.url = input("Enter URL: ")

    make_request(args.method, args.url)

if __name__ == "__main__":
    main()
