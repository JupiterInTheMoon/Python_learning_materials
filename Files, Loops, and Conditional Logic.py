

#把一堆数据先是按照空格分开放入一个个小盒子，再把小盒子里的数据按照逗号分开
f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for row in names_list:
    comma_list = row.split(',')
    nested_list.append(comma_list)
print(nested_list[0:5])


#这里要做的事情是把每一个盒子中的第一个数进行筛选，符合条件的第二个数进行相加
thousand_or_greater = []
for row in numerical_list:
    if row[1] >= 1000: # 这个问题在于你直接拿盒子去运作了，你需要一个变量碗
    thousand_or_greater.append(row[0])
print(thousand_or_greater[0:10])


numerical_list[len(numerical_list)-1] #这一步是在于测算这里有多少个盒子
thousand_or_greater = []
for line in numerical_list:
    name = line[0]  #要把盒子中的一个数据放到一个新的变量碗中，每一次都拿这个碗来进行下一步
    population = line[1]
    if population >= 1000:
        thousand_or_greater.append(name)
print(thousand_or_greater[0:10])




