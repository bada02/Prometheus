import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
codeword = sys.argv[1]
u=""
q=0
a=[]
answer=[]

x=list(codeword)
for i in x:
    if x[q]==' ':
        del x[q]
    q=q+1
q=0
x=x[0:len(x)/5*5] # throwing out last terms
for i in x: # transforming into ab sequence
    n=x[q].isupper()
    if n == True:
        a.append('b')
    elif n == False:
        a.append('a')
    q=q+1
q=0
s=len(a)

while s>=0: # decoding ab sequence
    if a==[]:
        break
    else:
        z=str(u.join(a[0:5]))
        v=key.find(z)
        answer.append(alphabet[v])

        del a[0:5]
    s=s-1
answer=u.join(answer)
print answer
