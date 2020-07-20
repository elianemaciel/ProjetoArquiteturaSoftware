#!/usr/bin/env python3

from MenuOptions import MenuOptions


def main():

    menu_options = MenuOptions.instance()
    option = 0
    # import ipdb; ipdb.set_trace()
    while option < 5:
        menu_options.show_menu()
        option = int(input("Digite a opção: "))
        if option == 1:
            menu_options.option_one()
        elif option == 2:
            menu_options.option_two()
        elif option == 3:
            menu_options.option_three()
        elif option == 4:
            menu_options.option_four()
        elif option == 5:
            res = input("Deseja realmente sair? ")
            if res.upper() == "S":
                break


main()
