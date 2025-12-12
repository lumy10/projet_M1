# Un package pour de la chimie

Ce repertoire est organisé de la maniere suivante:
```
.
├── README.md
├── chempkg
├   ├──atom.py
├   ├──mol.py
├   └──reaction_utils.py
├── pyproject.toml
└── tests
    ├── test_atom.py
    ├── test_molecule.py
    └── test_reactions_utils.py
```
chempkg est un package pour de la chime. Il contient trois modules: atom, mol et reaction.

## Module atom

Ce module contient :
- une classe Atom (name:str, num_electron:int, weight:float) 
- des instances de cette classe O, C, H, N, Ca, P, K,S, Na, Cl, Fe, I, F, Co, et Mo
- une methode elec_config qui fourni la configuration electronique d'un atome selon la règle de Klechkowski


## Module mol

## Module reaction_utils


