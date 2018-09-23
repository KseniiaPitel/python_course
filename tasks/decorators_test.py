def my_decorator(func_to_decorate):
    def wrapper():
        print("строка которая выводится до вызова функцию, которую будем декорировать")
        func_to_decorate()
        print("строка после вызова функции котую нужно декорировать")

    return wrapper

def stand_alone_func():
    print("независимая функция")
#def stand_alone_func(a):
 #   return  a ** 2

#print(list(map(stand_alone_func, range(5))))
#stand_alone_decorated = my_decorator(stand_alone_func)
#stand_alone_decorated()

#stand_alone_func=my_decorator(stand_alone_func)

#stand_alone_func()

@my_decorator
def new_func():
    print("test call decorator")

new_func()

