import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from zad15 import zad15

#3
print("Zadanie 3")

k1 = np.array([np.linspace(1,5,5),np.linspace(5,1,5)])
k2 = np.zeros((3,2))
k3 = np.ones((2,3))*2
k4 = np.linspace(-90,-70,3)
k5 = np.ones((5,1))*10
A0 = np.block([[k3], [k4]])
A0 = np.block([k2,A0])
A0 = np.block([[k1],[A0]])
A = np.block([A0,k5])
print(A)



#4
print("Zadanie 4")

B = A[1] + A[3]
print(B)



#5
print("Zadanie 5")

C = np.array([])
C = np.append(C, max(A[:,0]))
C = np.append(C, max(A[:,1]))
C = np.append(C, max(A[:,2]))
C = np.append(C, max(A[:,3]))
C = np.append(C, max(A[:,4]))
C = np.append(C, max(A[:,5]))
print(C)


#6
print("Zadanie 6")

D = np.array([])
D = np.delete(B, [0,5])
print(D)


#7
print("Zadanie 7")

D[D == 4] = 0
print(D)


#8
print("Zadanie 8")

E = np.array([])
mini = np.min(C)
maxi= np.max(C)
E = np.delete(C, np.where(C == mini))
E = np.delete(E, np.where(E == maxi))
print(E)


#9
print("Zadanie 9")

minimum = np.min(C)
maximum = np.max(C)
for a in range(np.shape(A)[0]):
    if minimum in A[a,:]:
        if maximum in A[a,:]:
            print(A[a,:])


#10
print("Zadanie 10")

print(D*E)
print(D@E)


#11
print("Zadanie 11")

def fun(l):
    macierz = np.random.randint(0,11,[l, l])
    return macierz, np.trace(macierz)

print(fun(7))



#12
print("Zadanie 12")

def fun1(macierz):
    np.fill_diagonal(macierz, 0)
    np.fill_diagonal(np.fliplr(macierz),0)
    return macierz

macierz2 = np.array([[1,2,3,13],[4,5,6,14],[7,8,9,15],[10,11,12,16]])
print(fun1(macierz2))


#13
print("Zadanie 13")

def fun2(macierz1):
    suma = 0
    size = np.shape(macierz1)
    for i in range(size[0]):
        if i % 2 == 0:
            suma = suma + np.sum(macierz1[i, :])
    return suma

print(fun2(macierz2))



#14
print("Zadanie 14")

x = np.linspace(-10, 10, 201)
y = lambda x: np.cos(2 * x)
plt.plot(x, y(x), 'r--')
plt.show()


#15
print("Zadanie 15")

x = np.linspace(-10, 10, 201)
macierz2 = np.zeros([len(x)])

for i in range(len(x)):
    macierz2[i] = zad15(x[i])


plt.plot(x,macierz2,'g+',x,y(x),'r--')



#zad16 z gwiazdką


#zad 17
print("Zadanie 17")
y2=3*(y(x)) + macierz2
plt.plot(x,y2,'b*',x,macierz2,'g+',x,y(x),'r--')

#zad18
print("Zadanie 18")
m3 = np.array([[10,5,1,7],[10,9,5,5],[1,6,7,3],[10,0,1,5]])
m4 = np.array([[34],[44],[25],[27]])

x= np.linalg.inv(m3) @ m4

print(x)



#zad19
print("Zadanie19")
m=1000000
x = np.linspace(0,2*np.pi,m)
y = lambda x:np.sin(x)
calka = integrate.quad(y, 0, 2*np.pi)[0]

print(calka)

#zad20 nie robimy
