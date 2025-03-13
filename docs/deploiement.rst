Déploiement et Gestion de l'Application
==================

**Pipeline CI/CD**

Le projet utilise GitHub Actions pour l'intégration et le déploiement continus. À chaque push sur la branche main,
le pipeline s'exécute en trois étapes :

1. Build et Push de l'image Docker sur Docker Hub

2; Déploiement sur Azure Web Apps

3. Mise à jour automatique de la documentation sur Read The Docs

**Lancer l'application avec Docker**

1. Extraire l'image depuis Docker Hub :

    docker pull nom-utilisateur/my-python-app:latest

2. Lancer le conteneur :

    docker run --rm -d -p 8000:8000 nom-utilisateur/my-python-app:latest

3. Accéder à l'application sur http://127.0.0.1:8000/

**Surveillance avec Sentry**

Sentry est configuré pour suivre les erreurs et les performances de l'application. Les alertes et rapports sont accessibles depuis le tableau de bord Sentry.