
from chempkg import atom

#dictionnaire symbole str et objet Atom correspondant
biosphere_elements = {i.name:i for i in vars(atom).values() if isinstance(i, atom.Atom)}

def parse_formula(s):
    d = {}
    i = 0
    while i<len(s):
        elem = s[i] 
        if elem not in biosphere_elements:
            raise ValueError(f"Élément chimique inconnu: {elem}")
        #recuperer toutes les lettres du symbole
        i+=1
        if i < len(s) and s[i].islower():
            elem += s[i]; i+=1
        atom_instance = biosphere_elements[elem]
        #recuperer tout les chiffres de la quantité
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        count = int(num) if num else 1
        #créer le dictionnaires, les clés sont les instances d'Atom, les valeurs sont leurs quantités
        d[atom_instance] = d.get(atom_instance, 0) + count

    return d

class Molecule:
    def __init__(self, formula:str):
       
        """
        formula (str): Formule brute (exemple: "C2OH6")
        atoms (dict[Atom, int]): dictionnaire des atomes dans la molecule
        weight (float): Masse atomique total
        """
        self.formula = formula
        self._atoms_dict = parse_formula(self.formula)


    @property
    def atoms(self):
        return self._atoms_dict
    
    @property
    def weight(self):
        return float( sum(atom.weight * count for atom, count in self.atoms.items()))
    
    def __repr__(self):
        return f"Atom(formula='{self.formula}')"

    def __str__(self):
        return f"{self.formula}"
    
    def __eq__(self,other):
        if self.formula==other.formula:
            return True 
        else:
            return False
        

#x=Molecule("C2OH6")
#print(x.weight)
#print(x.atoms)