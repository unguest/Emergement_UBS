# 🎓 Automatisation de l'émergement sur Moodle pour l'Université Bretagne Sud

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
MoodleSt=Présent #Absent #Excusé #Absent
```

4. Render geckodriver executable
```bash
chmod +x geckodriver
```

## Configuration du fichier .env

### **MoodleUs** : 
Définissez votre identifiant pour moodle

### **MoodlePa** : 
Définissez votre mot de passe pour moodle

### **MoodleSh** :  
Définissez si vous souhaitez que le navigateur s'exécute en mode invisible :  
- `True`
- `False`

### **MoodleSt** :  
Définissez le statut à utiliser pour l'émergement :  
- `Présent`
- `Absent`
- `Excusé`
- `Absent`

## Lancement 

Une fois configuré, lancez le script avec :
```bash
python3 Emerge.py
```

## ⏰ Automatisation avec Crontab

Automatisation de l'émergement tous les jours de la semaine (du lundi au vendredi) le matin et le soir 

1. ⚠️ Configuration ⚠️

Selenium doit être configuré pour s'exécuter sans ouvrir de fenêtre de navigateur
```bash
MoodleSh=True
```

2. Ouvrir l'éditeur de crontab
```bash
crontab -e
```

3. Ajouter les lignes suivantes
```bash
1 8 * * 1-5 python3 /path/to/Emerge.py
46 14 * * 1-5 python3 /path/to/Emerge.py
```

Les logs sont automatiquement sauvegarder dans le fichier emergement.log