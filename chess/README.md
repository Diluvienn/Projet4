Projet 4 - Développez un programme logiciel en Python

Ce logiciel est prévu pour un club d'échec. Il permet de : 

    Afficher la liste des tournois enregistrés
    Afficher les détails d'un tournoi
    Afficher la liste des joueurs
    Créer un nouveau joueur
    Créer un nouveau tournoi
    Ajouter des joueurs à un tournoi non commencé
    Reprendre un tournoi non terminé

Ces données sont enregistrées dans deux fichiers JSON. 

    Un pour les tournois
    Un pour les joueurs

Installation

    Clonez le dépot

    Depuis le terminal : 

        git clone https://github.com/Diluvienn/Chess.git

    Créez un environnement virtuel Dans le terminal :

        cd Chess
        python -m venv venv
        venv/Scripts/activate

Installez les dépendances

    pip install -r requirements.txt
Comment exécuter

Dans le terminal :

    python main.py

Arborescence :

    Chess/
    
    ├── main.py    
    ├── model/    
    │   ├── __init__.py    
    │   ├── match.py    
    │   ├── player.py    
    │   ├── round.py    
    │   └── tournament.py    
    ├── controller/    
    │   ├── __init__.py    
    │   ├── main_controller.py    
    │   ├── player_controller.py    
    │   └── tournament_controller.py    
    ├── view/    
    │   ├── __init__.py    
    │   ├── main_view.py    
    │   ├── player_view.py    
    │   └── tournament_view.py    
    ├── repository/    
    │   ├── __init__.py      
    │   ├── player_repository.py    
    │   └── tournament_repository.py    
    ├── utils/    
    │   ├── __init__.py    
    │   └── formatvalidator.py    
    ├── data/    
    │   ├── __init__.py    
    │   ├── players.json    
    │   └── tournament.json    
    ├── requirements.txt    
    ├── README.md

