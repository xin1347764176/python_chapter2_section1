my_list=[["a",33],["b",55],["c",11]]
# #--------------way1
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key,reverse=True)

#---------wya2
my_list.sort(key=lambda element:element[1],reverse=True)

print(my_list)