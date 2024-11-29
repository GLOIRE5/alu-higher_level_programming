#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':

    res = requests.get("https://intranet.hbtn.io/status")
    
    # Print the response details
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))  # Type of the response
    print("\t- content: {}".format(res.text))    # Content of the response
    print("\t- utf8 content: {}".format(res.text))  # UTF-8 content (same as text)
