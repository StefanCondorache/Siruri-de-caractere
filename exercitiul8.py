sir1,sir2='ABCGH JIOL YZ',''
for i in sir1:
    if i==' ':
        sir2+='-'
    if i=='Z':
        sir2+='A'
    if i!='Z' and i!=' ': sir2+=chr(ord(i)+1)
print(sir2)
