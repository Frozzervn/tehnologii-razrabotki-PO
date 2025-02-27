from cgitb import reset


def back_string(text):
    return text[::-1]

def polindrome(s):
    s_r = "".join(s.lower().split())
    print(s_r == s_r[::-1])
    return s

def vowels(string):
    vowels = "роывадпршыдпРОЫВАДПРШЫДП"
    sum = 0
    for char in string:
        if char in vowels:
            sum += 1
    return sum

def remove_duplicates(q):
    result = []
    seen = set()
    for char in q:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)