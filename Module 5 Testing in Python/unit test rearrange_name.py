#!/usr/bin/env python3
import re
# def rearrange_name(name):
#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
#     return "{} {}".format(result[2], result[1])
from rearrange import rearrange_name








print(rearrange_name("Lovelace, Ada"))  # Expected: Ada Lovelace
print(rearrange_name("Curie, Marie"))  # Expected: Marie Curie
print(rearrange_name("Hopper, Grace M."))  # Expected: Grace M. Hopper
print(rearrange_name("Einstein, Albert"))  # Expected: Albert Einstein
print(rearrange_name("Newton, Isaac"))  # Expected: Isaac Newton
print(rearrange_name("Turing, Alan")) 

# Expected: Alan Turing
print(rearrange_name("Hawking, Stephen"))  # Expected: Stephen Hawking
print(rearrange_name("Darwin, Charles"))  # Expected: Charles Darwin

print(rearrange_name("Galileo, Galileo"))  # Expected: Galileo Galileo
print(rearrange_name("Kepler, Johannes"))

