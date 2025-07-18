
#SETS
'''
thisset = {1, 2, 3, 4, 5}

print(thisset)

thisset.add(6)

print(thisset)

thisset.remove(2)

print(thisset)
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5} 


#union
union_set = set1.union(set2)
print(union_set)

#Intersection
inter_set = set1.intersection(set2)
print(inter_set)

#Difference
diff_set = set1.difference(set2)
print(diff_set)