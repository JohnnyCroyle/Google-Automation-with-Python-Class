import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))



print(re.search(r"\w*", "This is an example")) #    \w* matches zero or more word characters
print(re.search(r"\w*", "And_this_is_another"))#    \w* matches zero or more word characters