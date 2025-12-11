
from chempkg import atom

#dictionnaire symbole str et objet Atom correspondant
biosphere_elements = {i.name:i for i in vars(atom).values() if isinstance(i, atom.Atom)}

def parse_formula(s):
    s=list(s)
    i = 1
    while i < len(s):
        if s[i].isupper() and not s[i-1].isdigit():
            s.insert(i, "1")
            i += 1  # Sauter le "1" qu'on vient d'insérer
        i += 1

    # Si la formule finit par une lettre sans nombre ajouter 1
    if s[-1].isalpha():
        s += "1"

    #créer le dictionnaires, les clés sont les instances d'Atom, les valeurs sont les quantités
    d = {}
    i = 0
    while i<len(s)-1:
        if s[i].isalpha(): 
            elem = s[i] 
            if s[i+1].islower():
                elem += s[i+1]; i+=1
            i+=1
            atom_instance = biosphere_elements[elem]
            count = int(s[i])
            if atom_instance in d:
                d[atom_instance] += count
            else:
                d[atom_instance] = count
        i+=1
    return d

class Molecule:
    def __init__(self, formula:str):
       
        """
        formula (str): Formule brute (exemple: "C2OH6")
        atoms (dict[Atom, int]): dictionnaire des atomes dans la molecule
        weight (float): Masse atomique total
        """
        self.formula = formula

    @property
    def atoms(self):
        return parse_formula(self.formula)
    
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