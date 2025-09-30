def reverse_string(text):
    reversed_string = ""
    index = len(text)-1
    while index>=0:
        reversed_string+=text[index]
        index-=1
    return reversed_string