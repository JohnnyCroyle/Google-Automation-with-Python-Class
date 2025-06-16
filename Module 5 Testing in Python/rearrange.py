#!/usr/bin/env python3
import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name.strip()
    return "{} {}".format(result[2], result[1])




#print(rearrange_name(" ", " "))  # Expected: Ada Lovelace
# print(rearrange_name("Curie, Marie"))  # Expected: Marie Curie
# print(rearrange_name("Hopper, Grace M."))  # Expected: Grace M. Hopper