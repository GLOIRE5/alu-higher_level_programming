#!/usr/bin/python3
""" Fetch 'http://0.0.0.0:5050/status' instead of 'https://intranet.hbtn.io/status' """
import urllib.request


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # Corrected URL to 'http://0.0.0.0:5050/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        print(f"Failed to fetch the URL: {e}")


