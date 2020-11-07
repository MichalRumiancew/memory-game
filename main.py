import random
import os
import copy


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

    choice = input("You choice: ")

    while choice not in ["1", "2", "3"]:
        print("please pick 1 or 2 or 3")
        choice = input("You choice: ")
    return choice


def board_size(choice):
    if choice == "1":
        return [5, 4]
    elif choice == "2":
        return [5, 6]
    elif choice == "3":
        return [5, 10]


def init_board(col, row):
    board = []
    new_row = []

    for i in range(col):
        new_row.append("#")
    for x in range(row):
        copy_row = new_row.copy()
        board.append(copy_row)

    return board


def get_list_of_letter(size):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    list_of_letter = []

    while size > len(list_of_letter):
        letter = random.choice(letters)
        list_of_letter.append(letter)
        list_of_letter.append(letter)
        letters.remove(letter)

    random.shuffle(list_of_letter)

    return list_of_letter


def get_letter(list_of_letter):
    pass

def set_letter_on_board (list_of_letter, size_x, size_y):
    board_with_letters = []
    
    for x in range(size_y):
        row = []
        for i in range(size_x):
            
            letter = list_of_letter.pop()
            row.append(letter)
        board_with_letters.append(row) 

    return board_with_letters   
             
    




def generate_table(size_x, size_y):
    pass





def main():
    #     size_x = 5
    #     size_y = 10
    #     size = size_x * size_y
    #     letter_list = get_list_of_letter(size)
    #     get_letter(letter_list)

    choice = difficulty_level()
    size_list = board_size(choice)
    size = size_list[0]*size_list[1]
    list_of_letter = get_list_of_letter(size)
    print(set_letter_on_board(list_of_letter,size_list[0],size_list[1]))
    # print(init_board(size_list[0],size_list[1]))



main()