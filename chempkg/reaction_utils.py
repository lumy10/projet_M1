"""
module chempkg.reaction_utils
outils liees aux reactions chimiques
"""
import numpy as np
import matplotlib.pyplot as plt
from chempkg import mol

def valid_reaction(reactives:list[tuple[mol.Molecule, int]], products:list[tuple[mol.Molecule, int]]):
    """
    :param reactives: molecules des reactifs avec leurs quantites
    :type reactives: list[tuple[Molecule, int]]
    :param products: molecules des produits avec leurs quantites
    :type products: list[tuple[Molecule, int]]
    """
    reac = {}
    for molecule, coeff in reactives:
        for atom, count in molecule.atoms.items():
            reac[atom] = reac.get(atom, 0) + count * coeff

    prod = {}
    for molecule, coeff in products:
        for atom, count in molecule.atoms.items():
            prod[atom] = prod.get(atom, 0) + count * coeff
    return reac == prod

def kinetic_decomp(a: float, k: float, periode: float, steps: int = 10, figure_path: str = None):
    """
    :param a: Concentration initiale
    :type a: float
    :param k: Constante de reaction
    :type k: float
    :param periode: Periode temporelle
    :type periode: float
    :param steps: Pas
    :type steps: int
    :param figure_path: Titre de la figure
    :type figure_path: str
    """
    x=np.linspace(0,periode,steps)
    y=np.array([a*np.exp(-k*t) for t in x])
    if figure_path is not None:
        plt.plot(x,y)
        plt.title("Evolution de [A](t)")
        plt.xlabel("Temps (s)")
        plt.ylabel("[A](t) (mol/L)")
        plt.savefig(figure_path)
        plt.show()
    return y
