list1=[]

for outer in range(10):
    list2 = []
    for inner in range(10):
        list2.append(inner)
    list1.append(list2)

print(list1)

list3 = []
for outer_step in list1:
    for inner_value in range(10):
        #list1[outer].len()
        if list1[outer][inner_value] % 2 == 0:
            list3.append(list1[outer][inner_value])
print(list3)
