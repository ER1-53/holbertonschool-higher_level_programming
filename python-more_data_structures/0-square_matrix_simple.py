#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resultat = []
    for ligne in matrix:
        nouvelle_ligne = []
        for element in ligne:
            nouvelle_ligne.append(element ** 2)
        resultat.append(nouvelle_ligne)
    return resultat
