# Déploiement de l'application Python avec CI/CD sur Azure

## 🚀 Vue d'ensemble du pipeline CI/CD

Le pipeline CI/CD est structuré en trois étapes principales :

1. **Intégration continue (CI)** :
   - Vérifie le code à chaque push ou pull request sur branche main.
   - Installe les dépendances, exécute le linter (`flake8`) et lance les tests avec `pytest`.
   - S'assure que la couverture des tests dépasse 80 %.

2. **Conteneurisation avec Docker** (uniquement sur la branche `main`) :
   - Construit une image Docker de l'application.
   - Tague l'image avec le hash du commit.
   - Pousse l'image sur Docker Hub.

3. **Déploiement sur Azure Web App** (uniquement si la conteneurisation réussit) :
   - Récupère l'image Docker depuis Docker Hub.
   - Déploie l'image sur Azure Web App.
   - Vérifie que le site est accessible après le déploiement.

---

## 🛠 Configuration requise

### 1. Secrets GitHub

Les variables secrètes suivantes doivent être configurées dans le dépôt GitHub :

| Secret                  | Description                           |
|------------------------|---------------------------------------|
| `DOCKER_USERNAME`       | Nom d'utilisateur Docker Hub         |
| `DOCKER_PASSWORD`       | Mot de passe ou token Docker Hub     |
| `AZURE_CREDENTIALS`     | Identifiants pour Azure (JSON)       |
| `AZURE_APP_NAME`        | Nom de l'Azure Web App               |
| `AZURE_PUBLISH_PROFILE` | Profil de publication Azure         |

### 2. Fichiers nécessaires

- `Dockerfile` : Configuration de l'image Docker.
- `requirements.txt` : Liste des dépendances Python.
- `.github/workflows/ci.yml` : Workflow pour l'intégration continue.
- `.github/workflows/build.yml` : Workflow pour la conteneurisation.
- `.github/workflows/deploy.yml` : Workflow pour le déploiement.

---

## 🚢 Déploiement

### Étapes automatiques

1. **Sur une branche autre que `main` :**
   - Le pipeline CI s'exécute : linting, tests et vérification de couverture.

2. **Sur la branche `master` :**
   - Le pipeline CI s'exécute.
   - Si les tests sont réussis, la conteneurisation démarre.
   - Si la conteneurisation réussit, le déploiement sur Azure est lancé.

### Déploiement manuel local

Pour tester l'image Docker localement :

```bash
# Récupérer l'image Docker
docker pull $DOCKER_USERNAME/my-python-app:<commit_hash>

# Lancer le conteneur localement
docker run --rm -d -p 8000:8000 $DOCKER_USERNAME/my-python-app:<commit_hash>

# Accéder à l'application
http://localhost:8000
```

---

## 📝 Remarque

Après chaque déploiement, vérifiez que :
- Les fichiers statiques sont bien chargés.
- L'interface admin fonctionne correctement comme en local.

Bon déploiement ! 🚀

# Documentation clic ici (https://readthedocs.org/projects/modulardjangoarch/badge/?version=latest)](https://modulardjangoarch.readthedocs.io/en/latest/)

