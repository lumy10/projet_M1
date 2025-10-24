# Un package pour de la chimie

Ce repo montre une structure pour l'organisation du projet pour la deuxieme partie
de l'evaluation du cours de Python.  

Le dossier est organise de la maniere suivante :
```
.
├── README.md
├── chempkg
├── pyproject.toml
└── tests
    ├── test_atom.py
    ├── test_molecule.py
    └── test_reactions_utils.py
```

## Projet

Les differents modules de notre package `chempkg` ont vocation a etre mis dans
le dossier `chempkg`.  

Le dossier `tests` contient les fichiers pour verifier que les objets et fonctions
codes ont bien le comportement prevu.  
Pour lancer les tests installer pytest avec pip puis executer `pytest tests`.
