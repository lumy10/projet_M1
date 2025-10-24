from chempkg.atom import Atom

ATOMS =[
    (("O", 8, 16),),
    (("C", 6, 12),),
    (("H", 1, 1),),
    (("P", 15, 31),),
    (("K", 19, 39),),
    (("Na", 11, 23),),
    (("Cl", 17, 35.5,)),
    (("Mg", 12, 24.3,)),
    (("Fe", 26, 55.8,)),
    (("Zn", 30, 65,)),
    (("Au", 79, 197.,)),
    (("Fl", 114, 289.,)),
    (("Er", 68, 167.3,)),
    (("Er", 87, 223.,)),
]

def test_Atom():
    attr_names = ["name", "num_elec", "weight", "config_elec"]

    for (name, num_elec, weight)  in ATOMS:
        atom = Atom(name=name, num_elec=num_elec, weight=weight)
        for attr in attr_names:
            assert hasattr(atom, attr), f"{atom} has no attr {attr}"

        
