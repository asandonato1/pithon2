def avg(results):
    counter = 0
    for number in results:
        counter = counter + number
    return counter / len(results)

def lazy():
    d = input("LAZYd = ")
    c = float(d) * 3.14
    return c

def piCalc():
    diameter : float = input("d = ")
    c : float = input("c = ")
    pi = float(c) / float(diameter)
    return pi
#print(lazy())
#print(piCalc())
results = [3.141538461538462, 3.14, 3.14]
print(avg(results))
