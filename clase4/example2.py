# from math import sin as SIN
# import os

# # print(dir(os))

# print(os.system('pwd'))

# # def sin(x):
# #     print('hola mundo')
# # API_KEY = 21.211

# # # print = 'hola'

# # # print('cualquier valor')

# # sin(2)
# # A = SIN(2)
# # print(A)

# import random

# print(random.random())

# print(random.randint(1, 10))


# import platform
# import os 

# def clear_window():
#     if platform.system() == 'Windows':
#         os.system('cls')
#     else:
#         os.system('clear')

# print(dir(platform))
# clear_window();
# print(platform.system())

# import requests

# res = requests.get('https://www.google.com/search?q=python&sxsrf=ALeKk02r8OvzqbuZ1Zap25ZTxUVFy4Gb8A:1622853923419&source=lnms&tbm=isch&sa=X&ved=2ahUKEwii9oH9of_wAhWdpZUCHQH7ANwQ_AUoAXoECAEQAw&biw=1920&bih=937')

# print(res.content)

word = input('Ingrese palabra a buscar')

splitted = word.split()
print(splitted)
length = len(splitted)
print(length)

print(len(word.split()))