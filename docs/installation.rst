Installation
=======================================

Pour installer le projet en local, suivez les étapes ci-dessous :

1. Clonez le repository GitHub :

    git clone git@github.com:MouloudB-24/ModularDjangoArch.git

2. Accédez au dossier du projet :

    cd ModularDjangoArch

3. Créez et activez un environnement virtuel :

    python3 -m venv venv
    source venv/bin/activate  # Pour macOS/Linux
    venv\Scripts\activate  # Pour Windows

4. Installez les dépendances :

    pip install -r requirements.txt

5. Appliquez les migrations de la base de données :

    python manage.py migrate

6. Lancez le serveur local :

    python manage.py runserver

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

Vous pouvez également accéder à l'interface d'administration : http://127.0.0.1:8000/admin/