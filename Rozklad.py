from random import randint              ##pro test prvociselnosti
from math import sqrt                   ##pro fermata i eulera
from collections import defaultdict     ##pro nsn s prvociselnym rozkladem


###test prvociselnosti###
def je_prvocislo(n: int) -> bool:       ##vse v okamziku
    """Funkce určí, jestli je dané číslo prvočíslem."""

    #vnitrni funkce potrebna pro rozklad cisla#
    def rozklad(n: int) -> tuple[int,int]:
        """Funkce rozloží dané číslo do tvaru (2^k)*q."""

        k = 0
        while n%2 == 0:
            n = n//2
            k += 1
        return k, n
    #konec vnitrni funkce#
    

    #vnitrni funkce pro urychleni vypoctu#
    def modularni_mocneni(x: int, q: int, n: int) -> int:
        """Funkce spočítá q-tou mocninu čísla x modulo n."""

        a, b, c = q, 1, x
        while a != 0:
            t = a%2
            a = a//2
            if t != 0:
                b = (b*c)%n
            c = (c*c)%n
        return b
    #konec vnitrni funkce#
    
    if n == 2:
        return True

    k, q = rozklad(n-1)
    if k == 0:
        return False

    for _ in range(25):
        j = 0
        y = modularni_mocneni(randint(2,n-1), q, n)

        while True:
            if y == n-1:
                break
            if y == 1 and j == 0:
                break
            if y == 1 and j > 0:
                return False
            j += 1
            if j < k:
                y = (y*y)%n
            else: return False
    return True


###nejvetsi spolecny delitel###
def nsd_moderni_euklid(u: int, v: int) -> int:          ##nejrychlesjsi
    """Funkce spočítá největšího společného jmenovatele čísel u a v."""

    while v != 0:
        r = u%v
        u = v
        v = r
    return u


def nsd_dvojkovy(u: int, v: int) -> int:                ##nejpomalejsi - asi dvakrat pomalejsi nez rozsireny_euklid
    """Funkce spočítá největšího společného jmenovatele čísel u a v."""

    #vnitrni funkce pro vypocet 2^k potrebny k vraceni#
    def mocneni(x: int, q: int) -> int:
        """Funkce spočítá q-tou mocninu čísla x."""

        a, b, c = q, 1, x
        while a != 0:
            t = a%2
            a = a//2
            if t != 0:
                b = b*c
            c = c*c
        return b
    #konec vnitrni funkce#

    if u<0:
        u *= -1
    if v<0:
        v *= -1
    
    k = 0
    while u%2 == 0 and v%2 == 0:
        k += 1
        u //= 2
        v //= 2

    if u % 2 == 0:
        t = u
    else:
        t = -v
    while t != 0:
        while t%2 == 0:
            t //= 2
        if t>0:
            u = t
        else:
            v = -t
        t = u-v
    return u*(mocneni(2,k))


def nsd_rozsireny_euklid(u: int, v: int) -> int:        ##prostredne rychly - asi trikrat pomalejsi nez moderni_euklid
    """Funkce spočítá největšího společného jmenovatele čísel u a v."""

    u1, u2, u3 = 1, 0, u
    v1, v2, v3 = 0, 1, v

    while v3 != 0:
        q = u3//v3
        t1, t2, t3 = u1-q*v1, u2-q*v2, u3-q*v3
        u1, u2, u3 = v1, v2, v3
        v1, v2, v3 = t1, t2, t3
    return u3


###nejmensi spolecny nasobek###
def nsn_euklid(u: int, v: int) -> int:              ##nejrychlejsi
    """Funkce spočítá nejmenší společný násobek čísel u a v."""

    u //= nsd_moderni_euklid(u, v)
    return u*v


def nsn_rozklad(u: int, v: int) -> int:             ##pomale - asi padesatkrat pomalejsi nez nsn_euklid
    """Funkce spočítá nejmenší společný násobek čísel u a v."""

    #vnitrni funkce kvuli rozkladu#
    def fermat_telo_pro_nsn(n: int, seznam: dict[int]):

        while n%2 == 0:
            seznam[2] += 1
            n //= 2

        a = 2*(int(sqrt(n))) + 1
        b = 1
        r = (int(sqrt(n)))**2 - n

        while r != 0:
            r += a
            a += 2
            while r > 0:
                r -= b
                b += 2
        c = (a - b)//2
        d = (a + b - 2)//2

        if c != 1 and je_prvocislo(c):
            seznam[c] += 1
        else:
            if c != 1:
                fermat_telo_pro_nsn(c, seznam)
        if d != 1 and je_prvocislo(d):
            seznam[d] += 1
        else:
            if d != 1:
                fermat_telo_pro_nsn(d, seznam)
    #konec vnitrni funkce#

    #vnitrni funkce kvuli konecnemu vypoctu#
    def mocneni(x: int, q: int) -> int:
        """Funkce spočítá q-tou mocninu čísla x."""

        a, b, c = q, 1, x
        while a != 0:
            t = a%2
            a = a//2
            if t != 0:
                b = b*c
            c = c*c
        return b
    #konec #vnitrni funkce#

    rozklad_u = defaultdict(int)
    rozklad_v = defaultdict(int)

    fermat_telo_pro_nsn(u, rozklad_u)
    fermat_telo_pro_nsn(v, rozklad_v)

    for klic, hodnota in rozklad_v.items():
        rozklad_u[klic] = max(rozklad_u[klic], rozklad_v[klic])

    x = 1
    for klic, hodnota in rozklad_u.items():
        x *= mocneni(klic, hodnota)

    return x


###prvociselny rozklad###
def fermat(n: int) -> list[int]:                    ##rozlozi vzdy
    """Funkce rozloží dané číslo na prvočinitele."""
    
    #vnitrni funkce kvuli rekurzi#
    def fermat_telo(n: int, seznam: list[int]):

        while n%2 == 0:
            seznam.append(2)
            n //= 2

        a = 2*(int(sqrt(n))) + 1
        b = 1
        r = (int(sqrt(n)))**2 - n

        while r != 0:
            r += a
            a += 2
            while r > 0:
                r -= b
                b += 2
        c = (a - b)//2
        d = (a + b - 2)//2

        if c != 1 and je_prvocislo(c):
            seznam.append(c)
        else:
            if c != 1:
                fermat_telo(c, seznam)
        if d != 1 and je_prvocislo(d):
            seznam.append(d)
        else:
            if d != 1:
                fermat_telo(d, seznam)
    #konec vnitrni funkce#

    seznam = []
    fermat_telo(n, seznam)
    return sorted(seznam)


def euler(n: int) -> list[int]:                     ##ne vzdy rozlozi
    """Funkce rozloží dané číslo na prvočinitele. Ne vždy se jí to podaří, je k tomu pořeba mít dva různé rozklady na součet čtverců."""

    #vnitrni funkce kvuli rekurzi#
    def euler_telo(n: int, seznam: list[int]):
        
        for a in range(1, int(sqrt(n//2)+2)):
            x = n - a**2
            b = int(sqrt(x))
            if b**2 == x:
                break
        if a**2 + b**2 != n:
                raise ValueError
        c = None
        for c in range(a+1, int(sqrt(n//2) + 2)):
            x = n - c**2
            d = int(sqrt(x))
            if d**2 == x:
                break
        if not c or c**2 + d**2 != n:
            raise ValueError

        k = nsd_moderni_euklid(b - d, c - a)
        l = nsd_moderni_euklid(b - d, a + c)
        m = nsd_moderni_euklid(b + d, c - a)
        h = nsd_moderni_euklid(b + d, c + a)

        x, y = (k//2)**2 + (h//2)**2, (l//2)**2 + (m//2)**2

        if x != 1 and je_prvocislo(x):
            seznam.append(x)
        else:
            if x != 1:
                euler_telo(x, seznam)
        if y != 1 and je_prvocislo(y):
            seznam.append(y)
        else:
            if y != 1:
                euler_telo(y, seznam)
    #konec vnitrni funkce#
    
    seznam = []
    euler_telo(n, seznam)
    return sorted(seznam)


def rozklad(n: int) -> list[int]:
    """Funkce rozloží dané číslo na prvočinitele."""

    try:
        euler(n)
    except ValueError:
        fermat(n)
