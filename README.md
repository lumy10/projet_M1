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

## Cloner projet

Pour faire votre propre projet sur Github, la premiere etape est d'avoir un compte Github. Pour cela suivez les
[instructions](https://docs.github.com/fr/get-started/start-your-journey/creating-an-account-on-github)
d'installation.

Ensuite, il faut que vous cloniez (ie copiez), ce repo.
Pour cela installer `git` sur votre ordinateur puis executez la commande suivante :
`git clone https://github.com/etienneguevel/exemple_projet.git`.  

Le dossier clone pointe toujours vers l'adresse de mon dossier en ligne. Pour
changez ca, il va falloir changer le `remote origin` du dossier.  
Protocole :
- [Creez un repo github](https://docs.github.com/fr/repositories/creating-and-managing-repositories/creating-a-new-repository) sur votre compte Github, et notez l'url
- Dans votre terminal, allez dans le dossier clone, `cd exemple_projet`
- Enlevez le pointage vers mon depot avec la commande `git remote rm origin`
- Pointez vers le dossier que vous venez de creer `git remote add origin <url_votre_repo>`

Pour votre premier commit vous devrez push de cette maniere :  
`git push --set-upstream origin main`
