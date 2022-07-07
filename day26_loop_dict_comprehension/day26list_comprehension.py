
# list comprehension
number = [1,2,3]
new_list = [n+1 for n in number]
print(new_list)

name = "Kevin"
letter_list = [letter for letter in name]
print(letter_list)

# turn range(1,5) into list of 2,4,6,8
range(1,5) # 1,2,3,4
range_list = [2*n for n in range(1,5)]
print(range_list)

# conditional list comprehension
names =['kevin','tobyy','tommmy','gg','wu']
new_names = [n for n in names if len(n)>4]
print(new_names)

# turn all longer name capitalized
upper_names =[n.title() for n in names if len(n)>4]
print(upper_names)

# squared number list
raw_num = [1,1,2,3,5,8,21,55,34,13]
raw_num.sort()
print(raw_num)
squared_num =[n**2 for n in raw_num]
print(squared_num)

# return even number in a list(raw_num)
even_list = [n for n in raw_num if n%2 ==0]
print(even_list)

"""
turn data type in the end
with open("file1.txt") as file1:
    list1 = file1.readlines()
    
with open("file2.txt") as file2:
    list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]

# Write your code above 👆
print(result)
"""

#dictionary comprehension
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.item() if test}

names= ['Alex',"bill",'caro','fill']
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score>60}
print(passed_students)


# count the len of each words in list
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {item:len(item) for item in sentence.split()}
print(result)

total_len = []
for item in sentence.split():
    total_len.append(len(item))
print(total_len)

# change all c into f temperature in dictionary exercise
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# re edit a existed dictionary
#weather_f = {new_key:new_value for (key,value) in dictionary.items()}
weather_f = {key:32+(int(temp_c)*9/5) for (key,temp_c) in weather_c.items()}


student_dict = {
    "student" :["Angela","James","Lily"],
    "score" : [56,76,98]
}

for (key,value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


for (key,value) in student_data_frame.items():
    print(value)

# loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    print(row)


for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
