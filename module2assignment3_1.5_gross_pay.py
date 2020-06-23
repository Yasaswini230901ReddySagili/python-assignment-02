r=float(input('enter rate'))
h=float(input('enter hours'))
if h>=40:
    p=1.5*r*h
    print('the pay is',p)
else:
    p=r*h
    print('the pay is',p)