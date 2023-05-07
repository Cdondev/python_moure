#listas 
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [12,34,56,43,23]
print(len((my_list)))

my_other_list = [24, 1.66, 'carlos', 'Dominguez']
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[3])
print(my_other_list[-4])

#agregar elementos a una lista 
my_other_list.append('cdomdev')
print(my_other_list)
#agregar elementos dandole el indece en numero que queremos que quede
my_other_list.insert(2, 'negro')
print(my_other_list)
#remueve elentos de nuestra lista definiendo el indico o la palanra que queremos que elimine 
my_other_list.remove('negro')
print(my_other_list)


