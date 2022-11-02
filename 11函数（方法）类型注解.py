# def add(x:int,y:int):
#     return x+y
# def func(data:list)->list:#返回值类型注解 提示性not绝对性
#     return data

#union类型
from typing import Union
my_list:list[Union[str,int]]=[1,2,"itheima","itcast"]
my_dict:dict[str,Union[str,int]]={"name":"周杰伦","age":31}

def func(data:Union[int,str])->Union[int,str]:
    pass
