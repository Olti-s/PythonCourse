my_set={1,4,3,4,4,4,5,2,6}
print(my_set)

my_set1=set([1,2,3,4,4,5])
print(my_set1)

A={1,2,3}
B={3,5,6}

#to find the union

unioni=A.union(B)
print(unioni)

#intersection / preprja


preprja=A.intersection(B) # prerja= A & B
print(preprja)

#diferneca

diferenca = A.difference(B) #diference=A-B
print(diferenca)

#diferenca simetrike

d_simetrike=A.symmetric_difference(B) #d_dimetrike=A ^ B
print(d_simetrike)

#add element
A.add(6)
print(A)

#remove element
A.remove(6)

#discard - remove an element without error if it does not exists
A.discard(100)

#removes all elements
A.clear()

#find the number of element of a set
print(len(A))

list=[1,2,3,3,2,7,8,5,5,6]
C=set(list)
print(C)

A=(1,2,3,4,5)
numri=1
#operatori In edhe Not in

print(numri in A) # true ose false nese numri eshte pjese e bashkesise
print(numri not in A)
















































