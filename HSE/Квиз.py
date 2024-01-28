import platform
import sys
print(sys.version)
def print_system_info():
    print("Архитектура:", platform.architecture())
    print("Платформа:", platform.platform())
    print("Информация о сборке Python:", platform.python_build())
    print("Сетевое имя компьютера:", platform.node())

if __name__ == "__main__":
    print("Информация о системе:")
    print_system_info()
МояПеременная ="hello"
_my_var = 1
Myvar = 4
print(type(МояПеременная))
text = "Мама мыла раму"
words = text.split()

print(words)
x = [1,2,3,4,5]
x.append(6)
print(x)
