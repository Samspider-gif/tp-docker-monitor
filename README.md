# TP Docker - Infrastructure Multi-Services Sécurisée
**Module :** Orchestration & Containerisation (M1 Cybersécurité)  
**Auteur :** Haissam / Quentin

---

## 📋 Description du Projet
Ce projet implémente une infrastructure applicative complète respectant l'approche **"No Install"** (tout est conteneurisé). Il simule une architecture d'entreprise partitionnée et sécurisée.

### Services déployés :
1.  **API (Backend) :** Application Python (Flask) légère.
2.  **Base de Données :** PostgreSQL (Persistance des données).
3.  **Reverse Proxy :** Nginx (Point d'entrée unique).
4.  **Monitoring :** Service "maison" (Script Bash) analysant les logs en temps réel.

---

## 🏗️ Architecture & Choix Techniques

### 1. Isolation Réseau (Network Segmentation)
L'architecture utilise deux réseaux distincts pour garantir la sécurité :
* **Réseau `frontend` :** Connecte le Reverse Proxy et l'API.
* **Réseau `backend` :** Connecte l'API et la Base de Données.
* **Sécurité :** La base de données est configurée sur un réseau `internal: true`. Elle est **totalement inaccessible** depuis l'extérieur ou depuis le Reverse Proxy. Seule l'API peut lui parler.

### 2. Durcissement des Conteneurs (Security Hardening)
* **Utilisateur Non-Root :** L'API s'exécute avec un utilisateur dédié (`myuser`) créé dans le Dockerfile, et non en root.
* **Système de fichiers en lecture seule :** Le conteneur API tourne avec l'option `read_only: true`. Seul le volume `/app/logs` est inscriptible.
* **Moindre Privilège :** Les capacités Linux inutiles sont implicitement limitées par l'usage d'images `alpine`.

### 3. Gestion des Données
* **Persistance DB :** Volume nommé `db_data` pour ne pas perdre les données au redémarrage.
* **Logs partagés :** Volume `logs_volume` monté en écriture pour l'API et en lecture seule (`:ro`) pour le Monitoring.

---

## 🚀 Guide de Démarrage

### Prérequis
* Docker Engine & Docker Compose installés.
* Port 8080 libre sur la machine hôte.

### Lancement de la stack
À la racine du projet, exécuter :
```bash
docker compose up -d --build
