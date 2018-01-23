# module
from math import * # math中的所有function
root = sqrt(1001)
print（math.pi）
a = sqar(math.pi)

import csv
f = open("nfl.csv") # 是open，不是reader
csvreader = csv.reader(f) # 忘记了要module.function, 漏了module
nfl = list(csvreader) # 将这个文件转换成list

# 自己写代码才知道自己有很多问题
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team_name): 
    count = 0  # 将这个count和team_name写作同一个东西
    for line in nfl:
        if line[2] == team_name : # 这里直接可以是team_name,不需要写成“team_name"
            count += 1
    return count
    
cowboys_wins = nfl_wins("Dallas Cowboys") 
falcons_wins = nfl_wins("Atlanta Falcons")
# Class
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。

# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
# 这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，
# 然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。


# Create a class called Dataset.
class Dataset:
#  Inside the class, create a type attribute. Assign the value "csv" to it.
    def __init__(self):   这个是method（argument）
        self.type = "csv"
# Create an instance of the Dataset class, and assign it to the variable dataset.		
# Print the type attribute of the dataset instance.
dataset = Dataset()
print(dataset.type)




# Add a data parameter to the __init__() method, and set the value to the self.data attribute.
class Dataset:
    def __init__(self, data):
        self.data = data
# Read the data from nfl.csv and set it to the variable nfl_data.
f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

# Make an instance of the class, passing in nfl_data to the __init__() method (when you call Dataset(...)).
# Assign the result to the variable nfl_dataset.
# Use the data attribute to access the underlying data for nfl_dataset and assign the result to the variable dataset_data.
nfl_dataset = Dataset(nfl_data) # 这里在干什么？？ 类（对象）
dataset_data = nfl_dataset.data # 这个例子也有这个类的属性

class Dataset:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print(self.data[:10])
        
class Dataset:
    def __init__(self,data):
        self.data = data # 将这个属性给了self
        
    def print_data(self, num_row): # 定义一个函数
        print(self.data[:num_row]) # 直接print（变量），这个变量变成了self.data
                        
nfl_dataset = Dataset(nfl_data) # 举个栗子，
nfl_dataset.print_data(5) # 这里是dot notation method

class Dataset:
    def __init__(self, data):
        self.data = data

nfl_dataset = Dataset(nfl_data)

# Add the extract_header() code to the initializer and set the header data to self.header.
class Dataset:
    def __init__(self, data):
        self.header = data[0] # self就是变量
        self.data = data[1:]

# Create a variable called nfl_header and set it to the header attribute       
nfl_dataset = Dataset(nfl_data) 
nfl_header = nfl_dataset.header
       		
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):  # Add a method named column that takes in a label argument, 
		if label not in self.header:  # finds the index of the header, and returns a list of the column data.
            return None
        
        index = 0
        for idx, element in enumerate(self.header):  #  A great function to help us search the header and extract both the index and label to check is called enumerate(). 
				if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

