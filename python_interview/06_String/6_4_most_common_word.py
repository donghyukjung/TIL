import collections
import re
paragraph="Bob hit a ball, the hit BALL flew far after it was hit"
banned=["hit"]

words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
# substitute with blank if the letter is not word character
print(words)
count=collections.defaultdict(int)
# automotically add new key if there is no key
for word in words:
    count[word]+=1
print(max(count, key=count.get))
