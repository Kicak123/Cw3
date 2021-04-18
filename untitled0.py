import numpy as np


# wezly = np.array([[1, 0],
#                   [2, 1],
#                   [3, 0.5],
#                   [4, 0.75]])

# elementy = np.array([[1, 1, 3],
#                      [2, 4, 2],
#                      [4, 3, 4]])



def parametry_kontrolne(c, f):
    return c,f

def wstaw_parametry(sekcja, warunki, typy): 
    parametry = list(sekcja, warunki, typy)
    return  parametry



#funkcja def geo
def geo_def(sekcja, wezly, c, f):
    x= sekcja[1] - sekcja[0]
    wezly_n = len(wezly)
    ilosc_elementu = wezly_n - 1
    dlugosc_elementu = x/ilosc_elementu
    return x, wezly_n, ilosc_elementu, dlugosc_elementu



#funkcja fenerujaca geo automatycznie
def gen(x_0,x_p,n):
    tmp = (x_p - x_0)/(n-1);
    prze=np.array([x_0])
    i = []
    for i in range (1,n,1):
        prze = np.block([prze, i * tmp + x_0])
    return prze

