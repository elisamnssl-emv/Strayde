# Design System — Strayde

Ce document centralise les règles de design et composants de Strayde pour assurer la cohérence visuelle sur toutes les pages.

## Couleurs

La palette de couleurs principale (configurée dans Tailwind) :
- **Primary** : `#231a3d` (Bleu nuit profond)
- **Secondary** : `#1e929b` (Sarcelle/Teal)
- **Accent** : `#c5d97d` (Vert lime)
- **Navy** : `#36365f`
- **Teal** : `#30b7c0`
- **Muted** : `#6f6fad`
- **Sage** : `#dff1bb`
- **Offwhite** : `#f4fbe5`

## Typographie

- **Titres (Display)** : `Barlow Condensed` (sans-serif, poids : 500, 700, 800)
- **Corps (Body)** : `DM Sans` (sans-serif, poids : 300, 400, 500, 600)

## Boutons

Les classes de boutons sont gérées dans `assets/style.css` :
- `.btn-primary` : Fond très sombre, couleur claire. Transition douce au hover.
- `.btn-accent` : Fond vert lime (Accent), pour attirer l'attention (CTA fort).
- `.btn-teal` : Fond Sarcelle.
- `.btn-outline-light` : Bordure semi-transparente, texte blanc (pour fond sombre).
- `.btn-outline-dark` : Bordure sombre, texte sombre (pour fond clair).

## Composants (style.css)

- `.card` : Carte blanche standard, ombre au survol.
- `.card-dark` : Carte sombre semi-transparente (utile sur les fonds Primary).
- `.module-pill` : Badges pour tag/module :
  - `.mp-green`, `.mp-green-light`
  - `.mp-teal`, `.mp-teal-light`
- `.grad-text` : Texte avec dégradé Sarcelle vers Vert lime.
- `.reveal` : Classe pour l'animation au scroll (`.in` ajoutée via JS).

## Animation (Tailwind Config)
- `fade-up`, `fade-up-2`, `fade-up-3` : Apparition progressive.
- `floatY` : Flottaison verticale légère (pour interfaces / images hero).
