import random
import os


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

def clear():
    os.system("cls || clear")

def difficulty_level():
    clear()

    print("=========================================================")
    print("Choose difficulty level: ")
    print("\n")
    print("1. Easy difficulty")
    print("2. Medium difficulty")
    print("3. Hard")
    print("\n")
    
    print("================================================================")

    choice = input( "You choice: ")

    while choice not in["1", "2", "3"]:

        print("please pick 1 or 2 or 3")
        choice = input( "You choice: ") 
    return choice


def board_size (choice):
    if choice == "1":
        return 5,4
    elif choice == "2":
        return 5,6
    elif choice == "3":
        return 5,10


def init_board(col, row):
    board = []
    index = 0
    index_row = 0

    while index < col:
        row = []
        row.append("#")
        index += 1
    while index_row < row:
        board.append(row)

    return board



        
    




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
    pass

difficulty_level()




def main():

#     size_x = 5
#     size_y = 10
#     size = size_x * size_y
#     letter_list = get_list_of_letter(size)
#     get_letter(letter_list)

difficulty_level()


