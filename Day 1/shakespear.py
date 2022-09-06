from urllib.request import urlopen
from math import sqrt

shakespear = urlopen('http://composingprograms.com/shakespeare.txt')

set = set(shakespear.read().decode().split())
print(len(set))

for words in set:
    if len(words) ==6 and words[::-1] in set:
        print(words)

#test incrementally, check for errors by isolating them, check assumptions?
print(sqrt(10))