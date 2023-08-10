"""
import the module for request
"""
import urllib.request

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as requests:
    html = requests.read()