a = {2,3,4,5,8,9,7,6,5,1}
print(a)
a.add(10)
print(a)
b = {3,4,5,6,2,7,8,9,1,11}
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
array_num = arr.array('i',[3,4,6,2,7,8,4,3,3])
print('Original array: '+str(array_num))
print("Number of occurences of the number 4 in the said array:"+str(array_num.count(4)))
#reverse
array_num.reverse()
print("Reversed array:")
print (str(array_num))