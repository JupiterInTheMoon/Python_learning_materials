# 简单的数字运算
print((749+371+828+503+1379)/5)

# 赋值，然后直接找出变量
albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379
print(anaheim)

# 字符的类型输出
atlanta_string = "Atlanta"
print(type(atlanta_string))

# 数组list和dot notation
列表名字.append(要添加的内容) 
cities = [] 
cities.append("Albuquerque")
cities.append("Anaheim")

crime_rates =[749,371,828,503,1379] # 也可以一大串直接添加


# A list starts at index 0；zero indexing
anchorage_str = cities[2]
# 前面不需要定义什么，直接就将这个值塞到这个空的变量中
len_cr = len(crime_rates) # 数组的长度

# 数组切片slicing
ending_index = len(crime_rates)
two_to_end = crime_rates[2:ending_index]

# open（文档名字(字符形式)，处理文档的方式 (字符形式))
a = open("test.txt", "r")
print(a)
f = open("crime_rates.csv", "r")

f = open("test.txt", "r")
g = f.read()
# 文件名.处理方式

# 数组.split('\n') 这个是Python常用的语法，被处理文件或数组.处理动词（具体按照哪种方式）
sample = "john,plastic,joe"
split_list = sample.split(",")
# split_list is a list of _strings_: ["john", "plastic", "joe"]

# loop 
ten_rows = rows[0:10]
for row in ten_rows:
    print(row) # 关键就是这个row怎么确定呢
	
# 将一个数组
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []

for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)

# 如何把别的数组拆出来，放到另一个新的数组中，使用循环结构
crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]

    # crime_rate is a string, the crime rate of the city
    crime_rates.append(crime_rate)
	
# 看不是很懂	！！！
class Dataset:
    def __init__(self, data):
        self.data = data	
		f = open("somefile.csv", 'r')
csvreader = csv.reader(f)
csv_data = list(csvreader)

csv_dataset = Dataset(csv_data)
