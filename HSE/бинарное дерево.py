from binarytree import Node

# Функция для создания бинарного дерева из ввода пользователя
def create_binary_tree(target_sum=None):
    val = input("Введите значение узла (для пустого узла нажмите Enter): ")
    if val == '':
        return None
    else:
        node = Node(int(val))
        print("Введите левого потомка для узла", val)
        node.left = create_binary_tree(target_sum)
        print("Введите правого потомка для узла", val)
        node.right = create_binary_tree(target_sum)
        return node

# Функция для поиска путей с суммой по веткам
def find_paths(root, target_sum, path=[], paths=[]):
    if root is None:
        return paths

    path.append(root.value)

    if root.left is None and root.right is None and sum(path) == target_sum:
        paths.append(path[:])

    paths = find_paths(root.left, target_sum, path, paths)
    paths = find_paths(root.right, target_sum, path, paths)

    path.pop()

    return paths

# Создание бинарного дерева
print("Введите корневой узел для бинарного дерева:")
root = create_binary_tree()

# Ввод целевой суммы
target_sum = int(input("Введите целевую сумму для поиска путей: "))

# Поиск путей с целевой суммой
paths = find_paths(root, target_sum)

# Вывод результатов
if paths:
    print(f"Пути с суммой {target_sum}:")
    for path in paths:
        print('->'.join(map(str, path)))
    # Получение бинарного дерева
    print('Binary tree:', root)
else:
    print(f"Нет путей с суммой {target_sum}")
