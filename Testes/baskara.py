a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
delta=b**2-4*a*c
print('delta:',delta)
if delta<0:
    print('Sem raízes reais')
else:
    res1=(-b+delta**0.5)/(2*a)
    res2=(-b-delta**0.5)/(2*a)
    print('S={',res1,',',res2,'}')
    print('ou',-b+delta**0.5,'/',2*a)
    print('  ',-b-delta**0.5,'/',2*a)
