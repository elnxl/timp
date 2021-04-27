secret=b'c3zrd4ga'
stroka=b'4I}w0Br8'

res=[a ^ b for a,b in zip(secret,stroka)]
print(res)

key=''
for x in res:
  if 1<=x<=26:
    key+=chr(ord('a')+x-1)
  elif 80<=x<=89:
    key+=str(x-80)
  else:
    key+=chr(x)
print(key)