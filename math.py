#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import time
def ebob():
    a = int(input("a="))
    b = int(input("b="))
    print("ƏBOB(a,b)=",math.gcd(a,b))
def ekob():
    a = int(input("a="))
    b = int(input("b="))
    print("ƏKOB(a,b)=",math.lcm(a,b))
def kokaltı():
    n = int(input("Ədədi daxil edin:"))
    print("kökaltında n = ",math.sqrt(n))
def kvadrat():
    n = int(input("Ədədi daxil edin:"))
    print("n ədədinin kvadratı  = ",n**2)
def kub():
    n = int(input("Ədədi daxil edin:"))
    print("n ədədinin kubu  = ",n**3)
def perimetrkvadrat():
    n = int(input('Kvadratın Tərəfini daxil edin'))
    print("Kvadratın Perimetri=",n*4)
def sahekvadrat():
    n = int(input('Kvadratın Tərəfini daxil edin'))
    print("Kvadratın Sahəsi=",n**2)
def perimetrduzbucaqli():
    u = int(input('Uzunluğ='))
    e = int(input('En='))
    print("Düzbucaqlının Perimetri=",(e+u)*2)
def saheduzbucaqli():
    u = int(input('Uzunluğ='))
    e = int(input('En='))
    print("Düzbucaqlının Sahəsi=",e*u)
while True:
    time.sleep(0.5)
    print('''
-----------------------------
1.ƏBOB(a,b)
2.ƏKOB(a,b)
3.Kökaltı
4.Ədədin kvadratı
5.Ədədin kubu
6.Kvadratın perimetri
7.Kvadratın sahəsi
8.Düzbucaqlının perimetri
9.Düzbucaqlının sahəsi
0.çıxış
-----------------------------''')
    selection = int(input('Seçiminizi edin:[0,1,2,3,4,5,6,7,8,9]:'))
    if selection==0:
        for i in range(3):
            print('Çıxış!!!')
            time.sleep(0.5)
        break
    elif selection==1:
        print('ƏBOB(a,b)')
        ebob()
    elif selection==2:
        print('ƏKOB(a,b)')
        ekob()
    elif selection==3:
        print('Kökaltı')
        kokaltı()
    elif selection==4:
        print('Ədədin kvadratı')
        kvadrat()
    elif selection==5:
        print('Ədədin kubu')
        kub()
    elif selection==6:
        print('Kvadratın perimetri')
        perimetrkvadrat()
    elif selection==7:
        print('Kvadratın sahəsi')
        sahekvadrat()
    elif selection==8:
        print('Düzbucaqlının perimetri')
        perimetrduzbucaqli()
    elif selection==9:
        print('Düzbucaqlının sahəsi')
        saheduzbucaqli()
    else:
        for i in range(3):
            print('Səhfə yol verdiniz')
            time.sleep(0.5)


# In[ ]:




