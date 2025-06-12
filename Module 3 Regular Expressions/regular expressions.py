


import re

# result = re.search(r"aza", "maze")
# print(result)

# print(re.search(r"^x", "xenon"))


# print(re.search(r"p.ng", "clapping"))
# print(re.search(r"p.ng", "sponge"))

# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))


# print(re.search(r"[a-z]way", "The end of the highway"))
# print(re.search(r"[a-z]way", "What a way to go"))
# print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# print(re.search("cloud[a-zA-Z0-9]", "cloud9"))


# print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))