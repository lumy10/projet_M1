"""
module chempkg.atom
definition des atomes et configuration electronique
"""
def get_orbitales (m: int ):
    """
    :param m: nombre d'electron de l'atome
    :type m: int
    """
    sorted_orbitales=[(n,l) for n in range(1,8) for l in range(n)]
    sorted_orbitales.sort(key=lambda x: (x[0] + x[1], x[0]))
    #initialisation
    atoms_free = m
    orbitales_atom = []
    i=0
    n=1
    while atoms_free > 0:
        n,l = sorted_orbitales[i] # Selectionner la bonne orbitale
        atoms_orb = (l*2 + 1)*2 # capacité de l'orbitale
        if atoms_free<atoms_orb:
            atoms_orb = atoms_free #orbital non pleine
            atoms_free = 0
        else:
            atoms_free -= atoms_orb
        orbitales_atom.append((n, l, atoms_orb))
        i+=1
    return orbitales_atom

element=[
"O", # Oxygen
"C", # Carbon
"H", # Hydrogen
"N", # Nitrogen
"Ca", # Calcium
"P", # Phosphorus
"K", # Potassium
"S", # Sulfur
"Na", # Sodium
"Cl", # Chlorine
"Fe", # Iron
"I", # Iodine
"F", # Fluorine
"Co", # Cobalt
"Mo", # Molybdenum
]

class Atom:
    """
    definition des atomes
    """
    def __init__(self, name:str,num_electron:int, weight:float):
        """
        :param name: symbole chimique
        :type name: str
        :param num_electron: Nombre d'électrons
        :type num_electron: int
        :param weight: Masse atomique
        :type weight: float
        """
        if name not in element:
            raise ValueError(f"Élément chimique inconnu: {name}")
        self.name = name
        self.num_electron = num_electron
        self.weight = weight

    @property
    def elec_config(self):
        """
        renvoie la configuration electronique d'un atome
        """
        letters = 'spdf' #incomplet mais suffisant pour l'exercice
        orbitales_list = get_orbitales(self.num_electron)
        return tuple(f"{n}{letters[l]}{nb_elec}" for n, l, nb_elec in orbitales_list)
    def __repr__(self):
        return self.name
    def __str__(self):
        return f"{self.name} ({self.weight},{self.num_electron})"
    def __eq__(self,other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)

O = Atom("O", 8, 16) #oxygen
C = Atom("C", 6, 12) #carbon
H = Atom("H", 1, 1) #hydrogen
N = Atom("N", 7, 14) #nitrogen
Ca = Atom("Ca", 20, 40) #calcium
P = Atom("P", 15, 31) #phosphorus
K = Atom("K", 19, 39) #potassium
S = Atom("S", 16, 32) #sulfur
Na = Atom("Na", 11, 23) #sodium
Cl = Atom("Cl", 17, 35.5) #chlorine
Fe = Atom("Fe", 26, 55.8) #iron
I = Atom("I", 53, 127) #iodin
F = Atom("F", 9, 19) #fluorine
Co = Atom("Co", 27, 59) #colbat
Mo = Atom("Mo", 42, 96) #molybdenum