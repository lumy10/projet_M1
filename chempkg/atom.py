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

class Atom:
    def __init__(self, name:str,num_electron:int, weight:float):
       
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
        return f"Atom(name='{self.name}', num_electron={self.num_electron}, weight={self.weight})"

    def __str__(self):
        return f"{self.name} ({self.weight},{self.num_electron} )"
    
    def __eq__(self,other):
        if self.name==other.name and self.num_electron==other.num_electron and self.weight==other.weight:
            return True 
        else:
            return False
        

oxygen = Atom("O", 8, 16)      
carbon = Atom("C", 6, 12)       
hydrogen = Atom("H", 1, 1)        
nitrogen = Atom("N", 7, 14)       
calcium = Atom("Ca", 20, 40)   
phosphorus = Atom("P", 15, 31)      
potassium = Atom("K", 19, 39)      
sulfur = Atom("S", 16, 32)       
sodium = Atom("Na", 11, 23)    
chlorine = Atom("Cl", 17, 35)     
iron = Atom("Fe", 26, 56)    
iodin = Atom("I", 53, 127)     
fluorine = Atom("F", 9, 19)       
colbat = Atom("Co", 27, 59)    
molybdenum = Atom("Mo", 42, 96)     






#print(carbon)
#print(carbon.elec_config)
#print(carbon==oxygen)
#print(oxygen.elec_config)
