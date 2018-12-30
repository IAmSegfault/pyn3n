'''
A python port of https://github.com/IAmSegfault/N3N
Useful for example, when creating a deterministic seed for a given chunk coordinate.
(x,y,z)->(x combine 1)+((x+y+1) combine 2)+((x+y+z+2) combine 3).
See https://math.stackexchange.com/questions/1176184/how-to-find-unique-numbers-from-3-numbers
https://math.stackexchange.com/questions/312879/how-to-define-a-injective-and-surjective-function-from-mathbbz-to-mathbb
https://en.wikipedia.org/wiki/Combination#Example_of_counting_combinations
for details.
'''
maxint = 262144
maxmagic = 68719476735
magic = 9001

def constraint(j):
    if j > 0:
        j = 2 * j
    else:
        j = (-2 * j) + 1

    return j

def combine(n, k):
    c = 1
    for i in range(1, k + 1):
        x = n - (i - 1)
        c = (x / i) * c

    return c

def injection_map(x, y, z=0, w=False):
    x = constraint(x)
    y = constraint(y)
    z = constraint(z)

    n1 = x
    x1 = combine(n1, 1)

    n2 = x + y + 1
    x2 = combine(n2, 2)

    n3 = x + y + z + 2
    x3 = combine(n3, 3)

    r = x1 + x2 + x3

    if r > maxint:
        return None

    if w and abs(w) <= maxmagic:
        r = r * w
    else:
        r = r * magic

    r = r + 0.5 - (r + 0.5) % 1

    return r