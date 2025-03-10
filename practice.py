sujith = 7
Sujith = 23
print(sujith)  
print(Sujith)  

Sujith = [1, 2, 3, 45, 23, 7]
print(Sujith)  

print(Sujith[2])   
print(Sujith[-2:-1])  

Sujith.append(77)  
print(Sujith)  

Sujith.remove(2)  
print(Sujith)  

Sujith.insert(1, 2)  
print(Sujith)  

sujith = (7, 23, 4, 5, 8)
print(sujith)  

print(sujith[0:2])  

a, b, c, d, e = sujith
print(a, b, c, d, e)  

print(23 in sujith)  

Sujith_tuple = tuple(Sujith)
print(Sujith_tuple)  

print(sujith.index(4))  

print(sujith.count(23))  

Sujith.sort()
print(Sujith)  

Sujith.reverse()
print(Sujith)  

for num in Sujith:
    print(num, end=" ")  

print()  

for val in sujith:
    print(val, end=" ")  

print()  

squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)  

squared_tuple = tuple(x**2 for x in range(1, 6))
print(squared_tuple)  
