a=float(input())
b=float(input())
c=float(input())
dtb=(a*2+b*3+c)/6
if dtb<3:
    print('Kem')
elif dtb>=3 and dtb<5:
    print('Yeu')
elif dtb>=5 and dtb<6:
    print('Trung binh')
elif dtb>=7 and dtb<8:
    print('Kha')
elif dtb>=8 and dtb<9:
    print('Gioi')
else :
    print('Xuat sac')
