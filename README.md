# DevSecOps Project

## Description

Ce projet est une API REST développée avec Flask afin de mettre en pratique les concepts DevOps et DevSecOps.

L'objectif est de construire une chaîne complète comprenant :

- Développement d'une API REST
- Tests automatisés avec Robot Framework
- Intégration Continue avec GitHub Actions
- Conteneurisation avec Docker
- Analyse de sécurité avec Bandit

---

## Technologies utilisées

- Python 3.13
- Flask
- Robot Framework
- Git
- GitHub
- GitHub Actions
- Docker
- Bandit

---

## Structure du projet

```text
devsecops-project/
│
├── .github/
│   └── workflows/
│       └── robot-test.yml
│
├── tests/
│   └── api_tests.robot
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer le venv :

Windows

```bash
venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Lancer l'application

```bash
python app.py
```

L'API sera disponible sur :

```
http://localhost:5000
```

---

## Exécuter les tests Robot Framework

```bash
robot tests/api_tests.robot
```

Les rapports générés :

- report.html
- log.html
- output.xml

---

## Lancer avec Docker

Construire l'image :

```bash
docker build -t devsecops-api .
```

Démarrer le conteneur :

```bash
docker run -p 5000:5000 devsecops-api
```

---

## Pipeline GitHub Actions

À chaque push sur GitHub, le pipeline :

- installe les dépendances
- lance Bandit
- démarre Flask
- exécute les tests Robot Framework
- génère les rapports

---

## Analyse de sécurité

Le projet utilise Bandit afin d'effectuer une analyse statique du code Python et de détecter des vulnérabilités potentielles avant l'exécution des tests.

---
             Git Push
                 │
                 ▼
        GitHub Actions
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
   Bandit     Flask     Robot Framework
      │          │          │
      └──────────┼──────────┘
                 ▼
          Rapport de tests

## Compétences acquises

- Développement d'une API REST avec Flask
- Automatisation des tests avec Robot Framework
- Gestion de versions avec Git et GitHub
- Mise en place d'un pipeline CI avec GitHub Actions
- Conteneurisation d'une application avec Docker
- Analyse statique de sécurité avec Bandit
