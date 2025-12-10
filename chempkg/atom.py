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
            return ...
        
        def __repr__(self):
            return f"Atom(name='{self.name}', num_electron={self.num_electron}, weight={self.weight})"

        def __str__(self):
            return f"{self.name} ({self.weight},{self.num_electron} )"
        
        def __eq__(self,other):
            if self.name==other.name and self.num_electron==other.num_electron and self.weight==other.point:
                return True 
            

carbon = Atom ( name ="C", num_electron =6, weight =12)


def get_orbitales (Z: int ):
    # Z est le nombre d’electrons de notre atome
    sorted_orbitales =[(n,l) for n in range(1,8) for l in range(n)].sort(key=lambda x: (x[0] + x[1], x[0]))
    atoms_free = Z
    orbitales_atom = []
    i=0
    while atoms_free > 0:
        i+=1
        l, n = sorted_orbitales[i+1] # Selectionner la bonne orbitale
        atoms_orb = (l*2 + 1)*2 # nombre d’atomes sur une orbitales
        atoms_free -= atoms_orb
        # Ajouter la couche avec le nombre d’atomes dessus
        num_atom=...
        orbitales_atom . append ((n, l, num_atom )) # num_atom est a trouver
    return orbitales_atom