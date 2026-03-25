import array as arr
array_num =arr.array('i', [7,7,7,7,7,7,7,6,6,6])
print("original array : "+str(array_num))
print("number of occurrences of the number 7 in the said array:"+str(array_num.count(7)))
array_num.reverse()
print("reverse teh order of items :")
print(str(array_num))