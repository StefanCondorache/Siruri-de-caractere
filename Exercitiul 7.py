S=str(input('sirul de caractere: '))
x1=len([i for i in S if i=='A'])
print("a) numarul de aparitie a caracterului 'A':",x1)
s1=S.replace('A','*')
print('b)',s1)
s2=S.replace('B','')
print('c)',s2)
x2=len([i for i in S if i=='M' and S[S.index(i)+1]=='A'])
print('d)',x2)
s3,s4=[],[]
s3.extend(S)
s4.extend(S)
for i in s3:
    if i=='M' and s3[s3.index(i)+1]=='A':
        s3[s3.index(i)]='T'
print('e) ',*s3,sep='')
for i in range(len(s4)):
    if s4[i]=='T' and s4[i+1]=='O':
        s4[i]=''
        s4[i+1]=''
print('f) ',*s4,sep='')
print('g)',S[::-1])
