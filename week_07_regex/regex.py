import re


#So far I can get the program to read doctor's names. I tried to get the program to read two words that both start with capital letters, but the names of the hospitals and doctor's offices also came up

#It is also including some lower case words, and I can't figure out how to exclude them yet.

def find_name(line):
    pattern = "((Dr.|Mr.|Ms.|Mrs.|Miss)\s[A-Z][a-z][a-z][a-z]?[a-z]?[a-z]?[a-z]?\s?([A-Z]?[a-z]?[a-z]?[a-z]?[a-z]?[a-z]?))"
    result = re.findall(pattern,line)

    pattern = "((Dr.|Mr.|Ms.|Mrs.|Miss)\s[A-Z][a-z][a-z][a-z]?[a-z]?[a-z]?[a-z]?\s?([A-Z]?[a-z]?[a-z]?[a-z]?[a-z]?[a-z]?))"
    result = result + re.findall(pattern,line)

    #if result != "General Hospit" or "Medical Review" or "Primary Care":
    return result

  



f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)