import re

def remove(ip):
    result = re.sub(r'\b0+(\d)', r'\1', ip)
    print("Updated IP:", result)

remove("192.168.001.001")
