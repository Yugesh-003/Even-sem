#To check that string contains only certain set of characters (incase of a – z, A – Z,0 – 9)
import re

def check(s):
    pattern = "^[a-zA-Z0-9]*$"
    if re.search(pattern, s):
        print("Valid")
    else:
        print("Invalid")
check("yugg")
check("yugg12%")