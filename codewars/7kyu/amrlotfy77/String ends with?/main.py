def solution(string, ending):
    if string.endswith(ending):
        return True
    return False


def solution1(string, ending):
    # your code here...
    string1 = len(string) - len(ending)
    string2 = len(string) - string1
    string3 = string[string1:]
    if string3 == ending:
        return True
    else:
        return False
