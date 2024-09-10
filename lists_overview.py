'''
Question 1
I set my maximum to zero, then any number that was larger than my maximum
(while going through a loop), I changed the maximum to that number.
'''
def max_of_list(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    print(max)
max_of_list([4,12,10,6])


'''
Question 2
I set my sum to zero, and while going through a loop, 
I began to add the numbers one after the other
'''
def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)
sum_of_list([4,7,3,6])

'''
Question 3
I set all the lists to an empty list, 
then I appended my numbers from my 'for loop' into that list.
'''
list1 = []
for i in range(10,21):
    list1.append(i)
print(list1)
list2 = []
for i in range(10,101,10):
    list2.append(i)
print(list2)
list3 = []
for i in range(100,9,-10):
    list3.append(i)
print(list3)



