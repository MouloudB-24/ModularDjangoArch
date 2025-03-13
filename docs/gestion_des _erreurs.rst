Gestion des Erreurs et Surveillance avec Sentry
==============================================
Pour améliorer l’expérience utilisateur et la sécurité, la gestion des erreurs a été renforcée :

**Pages d’erreur personnalisées :**

Mise en place de templates personnalisés pour les erreurs 404 et 500.
Configuration dans settings.py et urls.py pour utiliser les handlers de Django en production.

**Intégration de Sentry :**
 - Installation : Ajoutez Sentry via pip (pip install sentry-sdk).
 - Configuration : Initialisez Sentry dans votre code (par exemple dans le fichier de configuration ou le wsgi.py) en utilisant une variable d’environnement pour la DSN.
 - Logging : Insérez des logs dans les zones critiques du code (fonctionnalités clés, blocs try/except, validations de données) en utilisant le module logging.
 - Sécurité : Ne jamais stocker les identifiants Sentry directement dans le code source ; utilisez des variables d’environnement.