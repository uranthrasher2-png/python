def greeting(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'




print(greeting('John', 'John'))

print(greeting('Ivan', 'manager'))
