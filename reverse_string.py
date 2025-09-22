def reverse_string(text):
    reversed_string = ""
    index = len(s)-1
    while index>=0:
        reversed_string+=s[index]
        index-=1
    return reversed_string