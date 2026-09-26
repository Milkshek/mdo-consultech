# MDO Consultech

Portfolio bilingue de Michel Do. HTML/CSS/JavaScript statiques, sans dépendance réseau, sans formulaire ni collecte de données. Contact via LinkedIn ou le lien e-mail professionnel.

## Prévisualisation

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Ouvrir http://127.0.0.1:4173 (français) ou http://127.0.0.1:4173/en/ (anglais).

## Modifier les contenus

Les textes FR/EN et la structure commune se trouvent dans `scripts/build.py`.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests
```

Les fichiers `index.html` et `en/index.html` générés sont versionnés pour permettre un hébergement GitHub Pages sans build. La feuille de style et le script d’animation sont dans `assets/`.

## Identité et sources

- Logo original fourni : `assets/logo.png`, conservé sans modification.
- CV FR et EN fournis : `assets/cv/`. Les PDF contiennent les coordonnées présentes dans les originaux et sont proposés tels quels, conformément à la demande.
- Les trois expériences sont synthétisées depuis les CV. Aucun résultat chiffré ou témoignage ajouté. Les expériences ne sont pas présentées comme des clients de MDO Consultech.
- Titres Georgia et texte Arial : polices système, aucun service tiers.
- Le reflet doré WebGL adapte le champ vectoriel de [liquid-logo](https://github.com/collidingScopes/liquid-logo). Licence MIT conservée dans `assets/vendor/liquid-logo-LICENSE.txt`. Il préserve les contours, s’arrête hors écran et dans un onglet masqué, respecte la réduction des mouvements et possède un bouton pause. Logo statique si WebGL échoue ou JavaScript est désactivé.

## Publication

Compatible avec GitHub Pages (fichiers à la racine, `.nojekyll`, URLs relatives compatibles avec un sous-répertoire). Aucun push ni déploiement n’est effectué par le script. Configurer l’hébergement sur la branche souhaitée au moment de publier.

## Référencement naturel

L’adresse publique est centralisée dans `SITE_URL` dans `scripts/build.py` :
`https://milkshek.github.io/mdo-consultech/`.
Le générateur produit les URL canoniques propres à chaque langue, les alternates
`hreflang` absolus et réciproques (FR, EN, x-default), les métadonnées de partage,
les données structurées WebSite / WebPage / Person et `sitemap.xml`.
Le contenu reste rendu en HTML sans dépendre du JavaScript.

Après publication :

1. Ajouter la propriété **Préfixe de l’URL** `https://milkshek.github.io/mdo-consultech/`
   dans Google Search Console et suivre sa procédure de validation. Si une balise
   de validation est choisie, fournir sa valeur pour l’ajouter au générateur ;
   ne pas modifier uniquement le HTML généré.
2. Soumettre `https://milkshek.github.io/mdo-consultech/sitemap.xml`.
3. Inspecter les URL française et anglaise, contrôler la canonique retenue et
   demander leur indexation. La disponibilité et le classement dans Google ne
   sont pas garantis par ces réglages.
4. Mesurer les performances du site publié avec PageSpeed Insights ; les tests
   locaux ne constituent pas une mesure des Core Web Vitals des visiteurs.

Pas de `robots.txt` dans ce dépôt de projet : seul
`https://milkshek.github.io/robots.txt`, à la racine du domaine, a autorité.
Un fichier sous `/mdo-consultech/` serait sans effet. Le sitemap peut être soumis
directement dans Search Console. Aucun accès Search Console ou résultat
d’indexation n’a été vérifié lors de l’implémentation.

Références : [versions localisées](https://developers.google.com/search/docs/specialty/international/localized-versions),
[robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro).
