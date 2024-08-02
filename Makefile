##
## EPITECH PROJECT, 2021
## Untitled (Workspace)
## File description:
## Makefile
##

all:
	cp main.py game
	chmod +x game

clean:

fclean: clean
		rm game

re: fclean all