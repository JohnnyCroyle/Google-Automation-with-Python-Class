import re




print(re.search(r"[a-zA-Z]{5}", "a ghost"))


print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))



print(re.findall(r"\w{5,}", "I really like strawberries"))


print(re.search(r"s\w{,20}", "I really like strawberries"))