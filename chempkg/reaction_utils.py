import mol
import numpy as np
import matplotlib.pyplot as plt


def valid_reaction(reactives: list[tuple[mol.Molecule, int]],products: list[tuple[mol.Molecule, int]]):
    L_reac = {}
    for molecule, coeff in reactives:
        for atom, count in molecule.atoms.items():
            L_reac[atom] = L_reac.get(atom, 0) + count * coeff

    L_prod = {}
    for molecule, coeff in products:
        for atom, count in molecule.atoms.items():
            L_prod[atom] = L_prod.get(atom, 0) + count * coeff
        
    return L_reac == L_prod

#h2 , o2 , h2o = mol.Molecule ("H2"), mol.Molecule ("O2"), mol.Molecule ("H2O")
#print( valid_reaction ( reactives =[( h2 , 2), (o2 , 1)] , products =[( h2o , 2)]))

def kinetic_decomp(A0: float, k: float, T: float, steps: int = 10, figure_path: str = None):
    x=np.linspace(0,10,10)
    y=[A0*2.7182818**(-k*t) for t in x]
    if figure_path != None:
        plt.plot(x,y)
        plt.title("Evolution de [A](t)")
        plt.xlabel("Temps (s)")
        plt.ylabel("[A](t) (mol/L)")
        plt.savefig(figure_path)
        plt.show()
    return y

A_t = kinetic_decomp (A0 =0.1 , k=0.5 , T=5, steps =10)
print (A_t )

A_t = kinetic_decomp (A0 =0.1 , k=0.5 , T=5, steps =10 , figure_path ="test.jpeg")