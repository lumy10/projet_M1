import atom
import mol


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