###############################################
# 1. first word of each log is identifier     #
# 2. letter log has priority than number      #
# 3. if letter is same, sort with identifier  #
# 4. number logs keep order                   #
###############################################

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
letters, digits=[],[]
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
letters.sort(key=lambda x : (x.split()[1:],x.split()[0]))
sorted=letters+digits
print(sorted)
