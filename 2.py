# КОДИРОВАНИЕ ПО ХАФФМАННУ

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.left = None
        self.right = None
        self.priority = priority

    def __repr__(self):
        return f'{str(self.value)} {self.priority}'


class Tree:
    def __init__(self, value: Node):
        self.root = value

    def _print(self):
        def __str(node: Node):
            print(node)

            if node.left:
                __str(node.left)
            if node.right:
                __str(node.right)

        __str(self.root)

    # функция создания таблицы символ, обычный рекурсивный обход дерева по всем ветвям.
    # при каждом вызове взове функции, складывается код в зависимости от направления с индексом
    # и передается как параметр вместе следующем узлом. в случае если узел является узлов рекурсия остонавливается
    # и значения узла вносится в таблицу кодирования.
    def get_coding_table(self):
        coding_table = {}

        def __coding_maker(node: Node, code=''):
            if node.left is None and node.right is None and len(node.value) == 1:
                coding_table.setdefault(node.value, code)
            if node.left is not None:
                __coding_maker(node.left, code + '0')
            if node.right is not None:
                __coding_maker(node.right, code + '1')

        __coding_maker(self.root)
        return coding_table

# функция вычисления частотности вхожениий символов в строку.
def get_frequent_dict(string: str):
    frequent_dict = {}
    for i in string:
        if i in frequent_dict:
            frequent_dict[i][0] += 1
        else:
            frequent_dict.setdefault(i, [1, ])
    return frequent_dict

# функция для сортировки  таблицы символов по приорететам, реализована для замены очереди с приорететами
def priority_queue(frequent_dict: dict):
    sorted_by_priority_dict = {}
    temp_tuple = sorted(frequent_dict.items(), key=lambda x: x[1][0], reverse=True)
    for i in temp_tuple:
        sorted_by_priority_dict.setdefault(i[0], i[1])
    return sorted_by_priority_dict

# функция создания  H-дерева
def huffman_tree_builder(sorted_by_priority_dict: dict):
    while len(sorted_by_priority_dict) != 1:
        first_code = sorted_by_priority_dict.popitem()# возвращаем два элемента для создания поддерева
        second_code = sorted_by_priority_dict.popitem()
        if len(first_code[1]) > 1 and len(second_code[1]) == 1: # проверка является ли узел листом, если нет меняем
            first_code, second_code = second_code, first_code # местам элементы(возможно избыточна) .
        first_node = Node(first_code[0], first_code[1][0])# создаем два дочерних узла
        second_node = Node(second_code[0], second_code[1][0])
        new_node = Node(first_code[0] + second_code[0], first_code[1][0] + second_code[1][0])# создаем родителя
        new_node.left = first_node if len(first_code[1]) == 1 else first_code[1][1]#Если узлы не являютс листьям сохраняем их в ноду
        new_node.right = second_node if len(second_code[1]) == 1 else second_code[1][1]# в противном случае сохраняем созданную реанее ноду
        sorted_by_priority_dict.setdefault(new_node.value, [new_node.priority, new_node])# возвращаем новую ноду обратно в словарь
        sorted_by_priority_dict = priority_queue(sorted_by_priority_dict)# снова сортируем словарь по приоритетам
    root = sorted_by_priority_dict.popitem()# если в словаре остался один елемент, создаем класс дерева и
    return Tree(root[1][1])# и передаем в нее корневой узел созданого нами H-дерева

# объеденяющая функция создания H-дерева
def get_huffman_tree(string: str):
    return huffman_tree_builder(priority_queue(get_frequent_dict(string)))

#функция кодировки строки возвращает таблицу и закодированную строку
def get_encoding_string_table(huffman_tree: Tree, init_string) -> tuple:
    string = ''
    table = tree.get_coding_table()

    for i in init_string:
        string += table[i]
    return string, table

# декодирующая функция
def decoding_string(sting_table: tuple):
    reversed_table = {i: j for j, i in sting_table[1].items()}
    decoded_string = ''
    char_code = ''
    for i in str(sting_table[0]):
        char_code += i
        if char_code in reversed_table:
            decoded_string += reversed_table[char_code]
            char_code = ''
    return decoded_string


if __name__ == '__main__':
    string = 'hello beautiful python world!'
    tree = get_huffman_tree(string)
    encoded_string_and_table = get_encoding_string_table(tree, string)
    print(f'Кодируемая строка  - {string}')
    print(f'Закодированая строка: "{encoded_string_and_table[0]}"\nТаблица символов: {encoded_string_and_table[1]}')

    print(f'Разкодированная строка: {decoding_string(encoded_string_and_table)}')

    # если считать, что на хранение символа используется 8 бит, исходная строка хранится в 232 бита, а закодированная
    # в 116, то кодирование по Хаффману сжало строку ровно в два раза.
