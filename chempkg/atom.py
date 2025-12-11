def get_orbitales (Z: int ):
    # Z est le nombre d’electrons de l'atome
    sorted_orbitales=[(n,l) for n in range(1,8) for l in range(n)]
    sorted_orbitales.sort(key=lambda x: (x[0] + x[1], x[0]))
    #initialisation
    atoms_free = Z
    orbitales_atom = []
    i=0
    n=1
    while atoms_free > 0:
        n,l = sorted_orbitales[i] # Selectionner la bonne orbitale
        atoms_orb = (l*2 + 1)*2 # capacité de l'orbitale
        if atoms_free<atoms_orb:
            atoms_orb=atoms_free #tout le reste est dans l'orbital
            atoms_free=0 #et c'est fini
        else:
            atoms_free -= atoms_orb
        orbitales_atom . append ((n, l, atoms_orb )) # num_atom: nombre d'atome de l'orbitale pas forcement pleine
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
    
    def __init__(self, name:str,num_electron:int, weight:float):
        if name not in element: 
            raise ValueError(f"Élément chimique inconnu: {name}")
       
        """
        name (str): Symbole chimique (ex: 'C', 'O')
        num_electron (int): Nombre d'électrons
        weight (float): Masse atomique
        elec_config (tuple[str]): Configuration électronique selon Klechkowski
        """
        self.name = name
        self.num_electron = num_electron
        self.weight=weight

    @property
    def elec_config(self):
        letters = 'spdf' #incomplet mais suffisant pour l'exercice
        orbitales_list=get_orbitales (self.num_electron )
        return tuple(f"{n}{letters[l]}{nb_elec}" for n, l, nb_elec in orbitales_list)
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.weight},{self.num_electron} )"
    
    def __eq__(self,other):
        if self.name==other.name :
            return True 
        else:
            return False
        
    def __hash__(self):
        return hash(self.name)
        

O = Atom("O", 8, 16)     #oxygen 
C = Atom("C", 6, 12)     #carbon  
H = Atom("H", 1, 1)      #hydrogen
N = Atom("N", 7, 14)     # nitrogen 
Ca = Atom("Ca", 20, 40)   # calcium
P = Atom("P", 15, 31)     # phosphorus
K = Atom("K", 19, 39)     # potassium
S = Atom("S", 16, 32)     #sulfur
Na = Atom("Na", 11, 23)    #sodium
Cl = Atom("Cl", 17, 35.5)    # chlorine
Fe = Atom("Fe", 26, 55.8)    #iron
I = Atom("I", 53, 127)    # iodin
F = Atom("F", 9, 19)      # fluorine
Co = Atom("Co", 27, 59)    #colbat
Mo = Atom("Mo", 42, 96)    # molybdenum





#print(C)
#print(C.elec_config)
#print(C==oxygen)
#print(O.elec_config)
#print(O.name)
