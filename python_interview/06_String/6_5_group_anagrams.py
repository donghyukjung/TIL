import collections
def groupAnagrams(words:list[str])->list[list[str]]:
    anagrams=collections.defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

words=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(words))