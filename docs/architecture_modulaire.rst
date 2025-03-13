Architecture Modulaire
======================
Pour améliorer la maintenabilité et l’évolutivité, l’architecture monolithique a été décomposée en deux applications
distinctes :

**Application "lettings" :**
Contient les modèles Address et Letting.
Dispose de ses propres templates et URLs.
Une migration Django transfère les données existantes dans les nouvelles tables sans utiliser de SQL direct.

**Application "profiles" :**
Contient le modèle Profile.
Intègre ses propres templates et URLs.

**Actions réalisées :**
 - Déplacement des fichiers HTML vers des dossiers de templates spécifiques à chaque application.
 - Réorganisation des URL : déplacement et création d’espaces de nom pour assurer une isolation des routes.
 - Renommage des vues et templates d’index (ex. : lettings_index.html devient index.html avec la vue index dans l’application concernée).
 - Suppression des fichiers et tables obsolètes dans l’application initiale oc_lettings_site