#!/usr/bin/python3
""" fetch 'http://0.0.0.0:5050/status' """
import urllib.request

if __name__ == "__main__":
    # Corrected URL with 'status' instead of 'statu'
    url = "http://0.0.0.0:5050/status"
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        print(f"Failed to fetch the URL: {e}")

