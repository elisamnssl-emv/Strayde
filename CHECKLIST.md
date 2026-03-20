# Workflow & Checklist pour le Site Strayde V1

Avant de publier une modification ou de créer une nouvelle page, vérifie ces points :

1.  **Architecture Static Site Generator** :
    - As-tu créé la nouvelle page dans le dossier `pages/` ?
    - As-tu ajouté un commentaire HTML en haut de page avec `title: ...` et `description: ...` ?

2.  **Fragments Communs** :
    - Les changements touchant toute la structure (liens de nav) doivent être faits dans `fragments/head.html`, `fragments/header.html` ou `fragments/footer.html`.

3.  **Build** :
    - Après tes changements, as-tu exécuté la commande `python build.py` depuis la racine (`Strayde V1/`) ?
    - Teste le rendu final des pages directement depuis le dossier `dist/`.

4.  **Couleurs, CSS et Classes** :
    - Vérifie que tu utilises les classes gérées par `assets/style.css` (`.btn-accent`, `.card`, etc.) pour éviter les doublons dans l'HTML.
    - Le tailwind config doit rester dans le `<head>` de `head.html` (sans ajouter le style complet).

5.  **Javascript** :
    - Les modifications globales de logique sont à mettre dans `assets/app.js`.

6.  **SEO & Assets** :
    - Vérifie que chaque balise titre `<h1>` est unique sur la page.
    - Ouvre la page et vérifie que les icônes (Lucide) se chargent grâce à `lucide.createIcons();` dans `app.js`.
