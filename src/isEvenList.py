#Python one line of code to create a new list with only even elements.

def evenList(list):
  return [x for x in list if x % 2 == 0]

normal_list = [1,2,3,4,56,7,8,99,17,0]
even_list = evenList(normal_list)
print(even_list)
