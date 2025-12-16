# Un package pour de la chimie

Ce repertoire est organisé de la maniere suivante:
```
├── README.md
├── chempkg
│   ├── atom.py
│   ├── mol.py
│   └── reaction_utils.py
├── pyproject.toml
└── tests
    ├── test_atom.py
    ├── test_molecule.py
    └── test_reactions_utils.py
```
`chempkg` est un package pour de la chime. Il contient trois modules: `atom`, `mol` et `reaction_utils`.

## Module atom
Ce module permet de représenter des atomes.

### Classe Atom  

```python
Atom(name: str, num_electron: int, weight: float)
```

Attributs :
- `name` : symbole chimique de l’atome
- `num_electron` : nombre d’électrons
- `weight` : masse atomique


### Atomes prédéfinis :

`O`, `C`, `H`, `N`, `Ca`, `P`, `K`, `S`, `Na`, `Cl`, `Fe`, `I`, `F`, `Co`, `Mo` 

### Méthode :
- `elec_config()` : renvoie la configuration électronique de l’atome selon la règle de Klechkowski


## Module mol

Ce module permet de manipuler des molécules à partir de leur formule chimique.

### Classe Molecule  
```python
Molecule(formule: str)
```

### Méthodes :
- `atoms()` : renvoie un dictionnaire associant chaque atome de la molécule à sa quantité
- `weight()` : calcule et renvoie la masse molaire de la molécule

## Module reaction_utils

Ce module fournit des outils liés aux réactions chimiques et à la cinétique.

### Fonctions :
```python
valid_reaction(reactifs: list[tuple[Molecule, int]], produits: list[tuple[Molecule, int]]) -> bool
```
Vérifie si une réaction chimique est équilibrée.

```python
kinetic_decomp(A0: float, k: float, T: float, steps: int = 10, figure_path: str | None = None)  
```
Calcule l’évolution temporelle de la concentration d’une molécule lors d’une réaction de décomposition cinétique.  
Une figure peut être sauvegardée si figure_path est fourni

## Installation

Cloner le dépôt puis installer le package en mode développement :

`pip install -e .` 