# 🎓 Automatisation Moodle Université Bretagne Sud

Ce projet automatise l'émergement des élèves de l'Université Bretagne Sud en utilisant Selenium. 

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/MTlyx/Emergement_UBS.git && cd Emergement_UBS
```

2. Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

3. Créez le fichier `.env` pour y stocker vos identifiants et paramètres :
```bash
MoodleUs=A_Remplacer_Identifiant
MoodlePa=A_Remplacer_MotDePasse
MoodleSh=False #True
MoodleSt=Présent #Absent #... #...
```

## Configuration

- **`MoodleUs`** : 
Définissez votre identifiant pour moodle

- **`MoodlePa`** : 
Définissez votre mot de passe pour moodle

- **`MoodleSh`** :  
Définissez si vous souhaitez que le navigateur s'exécute en mode invisible :  
- `True`
- `False`

- **`MoodleSt`** :  
Définissez le statut à utiliser pour l'émergement :  
- `Présent`
- `Absent`
- `..`
- `. .`

## Lancement 

Une fois configuré, lancez le script avec :
```bash
python script.py
```

