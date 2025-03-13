Tests Unitaires et d'Intégration
================================
**Objectif qualité :** Une couverture de tests supérieure à 80 % est exigée.

**Organisation des tests :**
 - Chaque application (lettings, profiles) contient ses propres tests unitaires.
 - Les tests couvrent les vues, les URLs et les modèles.

**Outils :**
 - pytest pour l’exécution des tests.
 - coverage.py pour mesurer la couverture.

**Linting et Qualité du Code :**
 - Utilisation de flake8 avec la configuration définie dans setup.cfg.
 - Correction de toutes les erreurs signalées par l’outil de linting sans modifier la configuration.