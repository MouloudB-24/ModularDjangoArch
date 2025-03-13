Déploiement et Gestion de l'Application
==================

**Pipeline CI/CD**

Le projet utilise GitHub Actions pour l'intégration et le déploiement continus. À chaque push sur la branche main,
le pipeline s'exécute en trois étapes :

1. CI pipeline

2. Build et Push de l'image Docker sur Docker Hub

3. Déploiement sur Azure Web Apps

**Lancer l'application avec Docker**

1. Extraire l'image depuis Docker Hub :
 - *docker pull nom-utilisateur/my-python-app:latest*

2. Lancer le conteneur :

 - *docker run --rm -d -p 8000:8000 nom-utilisateur/my-python-app:latest*

3. Accéder à l'application sur http://127.0.0.1:8000/