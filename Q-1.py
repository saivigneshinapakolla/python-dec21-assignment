l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
res=list()
odd_elements = l1[1::2]
print("Element at odd index position from list one")
print(odd_elements)
even_elements=l2[0::2]
print("Element at even index position from list two")
print(even_elements)

print("Printing final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)
