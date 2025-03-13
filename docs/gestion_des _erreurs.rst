Gestion des Erreurs et Surveillance avec Sentry
==============================================
Pour améliorer l’expérience utilisateur et la sécurité, la gestion des erreurs a été renforcée :

**Pages d’erreur personnalisées :**

Mise en place de templates personnalisés pour les erreurs 404 et 500.
Configuration dans settings.py et urls.py pour utiliser les handlers de Django en production.

**Intégration de Sentry :** Sentry est configuré pour suivre les erreurs et les performances de l'application.
Les alertes et rapports sont accessibles depuis le tableau de bord Sentry.