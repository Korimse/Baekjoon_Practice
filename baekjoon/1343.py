string = input()

string = string.replace("XXXX", "AAAA")
string = string.replace("XX", "BB")
if 'X' in string:
    print(-1)
else:
    print(string)