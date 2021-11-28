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


def get_frequent_dict(string: str):
    frequent_dict = {}
    for i in string:
        if i in frequent_dict:
            frequent_dict[i][0] += 1
        else:
            frequent_dict.setdefault(i, [1, ])
    return frequent_dict


def priority_queue(frequent_dict: dict):
    sorted_by_priority_dict = {}
    temp_tuple = sorted(frequent_dict.items(), key=lambda x: x[1][0], reverse=True)
    for i in temp_tuple:
        sorted_by_priority_dict.setdefault(i[0], i[1])
    return sorted_by_priority_dict


def huffman_tree_builder(sorted_by_priority_dict: dict):
    while len(sorted_by_priority_dict) != 1:
        first_code = sorted_by_priority_dict.popitem()
        second_code = sorted_by_priority_dict.popitem()
        if len(first_code[1]) > 1 and len(second_code[1]) == 1:
            first_code, second_code = second_code, first_code
        first_node = Node(first_code[0], first_code[1][0])
        second_node = Node(second_code[0], second_code[1][0])
        new_node = Node(first_code[0] + second_code[0], first_code[1][0] + second_code[1][0])
        new_node.left = first_node if len(first_code[1]) == 1 else first_code[1][1]
        new_node.right = second_node if len(second_code[1]) == 1 else second_code[1][1]
        sorted_by_priority_dict.setdefault(new_node.value, [new_node.priority, new_node])
        sorted_by_priority_dict = priority_queue(sorted_by_priority_dict)
    root = sorted_by_priority_dict.popitem()
    return Tree(root[1][1])


def get_huffman_tree(string: str):
    return huffman_tree_builder(priority_queue(get_frequent_dict(string)))


def get_encoding_string_table(huffman_tree: Tree, init_string) -> tuple:
    string = ''
    table = tree.get_coding_table()

    for i in init_string:
        string += table[i]
    return string, table


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
