h=float(input('enter hours'))
try:
    r=input('enter rate')
    int(r)
    pay=h*r
    print('pay is',pay)
except:
    print('invalid input')