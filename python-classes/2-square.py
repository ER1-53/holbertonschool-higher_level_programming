#!/usr/bin/python3
class Square:
    """
    It's class Square for creat a square.
    """

    def __init__(self, size=0):

        """
    Calcule et renvoie l'aire d'un rectangle.
    :param length: Longueur du rectangle.
    :param width: Largeur du rectangle.
    :return: L'aire du rectangle.
        """
        if is not isintance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
