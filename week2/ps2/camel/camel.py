str = input("camelCase : ")
sl = len(str)
print("snake_case : ", end = "")
for i in range(sl):
    tc = str[i]
    if(tc.isupper()):
        print("_",tc.upper(), end = "")
    else:
        print(tc, end = "")
print()
