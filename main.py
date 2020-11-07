import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def get_list_of_letter(size):
    list_of_letter = []

    while size // 2 > len():
        letter = random.choice(letters)
        list_of_letter.append(letter)
        list_of_letter.append(letter)

    random.shuffle(list_of_letter)

    return list_of_letter


def get_letter(list_of_letter):
    pass


def genrate_coordinates(size_x, size_y, letter):
    pass


def generate_table(size_x, size_y):





def main():
    size_x = 5
    size_y = 10
    size = size_x * size_y
    letter_list = get_list_of_letter(size)
    get_letter(letter_list)
