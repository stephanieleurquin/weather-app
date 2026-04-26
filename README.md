# 🌤️ Météo Live PRO

Application web interactive développée avec Streamlit permettant d’afficher la météo en temps réel et les prévisions sur plusieurs jours.

---

## 🚀 Fonctionnalités

* 🌍 Sélection de villes (Paris, Bruxelles, Liège, etc.)
* 🌡️ Température en temps réel
* 💨 Vitesse du vent
* 🌧️ Précipitations
* 🧠 Analyse automatique de la météo
* 📅 Prévisions sur 7 jours
* 📊 Historique météo sauvegardé (SQLite)
* 🗺️ Carte interactive

---

## 🛠️ Technologies utilisées

* Python
* Streamlit
* SQLite
* Pandas
* API Open-Meteo

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/stephanieleurquin/weather-app.git
cd weather-app
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l’application

```bash
streamlit run apimeteo.py
```

---

## ☁️ Déploiement

L’application est déployée sur Streamlit Cloud.

---

## 📊 Base de données

Les données météo sont stockées dans une base SQLite locale (`meteo.db`).

⚠️ Note : sur le cloud, les données peuvent être temporaires.

---

## 📁 Structure du projet

```
weather-app/
│── apimeteo.py
│── requirements.txt
│── meteo.db
│── README.md
```

---

## 🎯 Objectif du projet

Ce projet a été réalisé dans le but de :

* apprendre le développement d’applications web avec Streamlit
* comprendre l’utilisation d’API
* manipuler une base de données SQLite
* découvrir le déploiement cloud

---

## 👨‍💻 Auteur

Vanschoor St.

---

## 📌 Améliorations futures

* 🔐 système de login utilisateur
* ☁️ migration vers base de données cloud (PostgreSQL)
* 📱 amélioration du design UI
* 📈 graphiques avancés

---



N’hésite pas à mettre une ⭐ sur le repository !
