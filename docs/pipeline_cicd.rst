Tests Unitaires et d'Intégration
================================
Le pipeline CI/CD automatisé (via GitHub Actions) comporte plusieurs étapes clés :

**1. Compilation et Tests :**

 - Exécution du linting et de la suite de tests.
 - Le pipeline vérifie que la couverture de tests est supérieure à 80 %.
 - Ce travail s’exécute pour toutes les branches.

**2. Conteneurisation et Tagging :**

 - Si les tests sont réussis et uniquement pour la branche master (ou main), une image Docker du site est construite.
 - L’image est taguée avec un identifiant unique (par exemple, le hash du commit).
 - L’image est ensuite poussée sur Docker Hub.

**3. Déploiement :**
 - Le déploiement sur Azure Web Apps est déclenché uniquement après la réussite de la phase de conteneurisation.
 - L’application est déployée en production en utilisant la nouvelle image Docker.

**4. Mise à jour de la Documentation :**
 - En parallèle, la documentation technique est mise à jour sur Read The Docs.

**Commande Unique pour Tester Localement :** Pour lancer l’application localement avec Docker (après conteneurisation) :

 - *docker pull nom-utilisateur/my-python-app:latest*
 - *docker run --rm -d -p 8000:8000 nom-utilisateur/my-python-app:latest*