# MDO Consultech

Portfolio bilingue de Michel Do. HTML/CSS/JavaScript statiques, sans dépendance réseau, sans formulaire ni outil de mesure d’audience. GitHub Pages journalise les IP pour la sécurité ; les échanges par e-mail impliquent un traitement de données. Contact via LinkedIn ou le lien e-mail professionnel.

## Prévisualisation

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Ouvrir http://127.0.0.1:4173 (français) ou http://127.0.0.1:4173/en/ (anglais).

## Modifier les contenus

Les textes FR/EN et la structure commune se trouvent dans `scripts/build.py`. Les mentions légales sont dans `scripts/legal.py` et produisent `mentions-legales.html` et `en/legal-notice.html`.

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

## Mentions légales — activité exclusivement professionnelle

Les pages FR/EN sont reliées aux pieds de page. Le site et les mentions précisent
que les prestations sont réservées aux clients agissant dans leur activité professionnelle. Informations d’identité issues du document
INPI fourni ; aucun document INPI ni donnée personnelle étrangère aux mentions n’est copié.

Périmètre et règles à appliquer :

- **Clientèle professionnelle uniquement** : choix confirmé par Michel le 3 octobre
  2026. La médiation de la consommation ne s’applique pas aux litiges entre
  professionnels ; aucune adhésion ni rubrique de médiation n’est donc requise
  pour ce périmètre. Vérifier que les commandes concernent bien une activité
  professionnelle. Si l’offre s’ouvre aux consommateurs, réexaminer ces obligations
  avant de conclure les contrats correspondants.
- **Téléphone de l’hébergeur** : +1 877 448 4820 ajouté à la demande explicite
  de Michel le 3 octobre 2026. Source : brochure officielle GitHub Enterprise,
  https://enterprise.github.com/downloads/en/enterprise-datasheet.pdf (page 2).
  La source est ancienne ; le fonctionnement actuel du numéro n’est pas confirmé.
- **Messagerie** : la politique retient la suppression des demandes sans suite au plus
  tard 12 mois après leur clôture. Cette règle doit être appliquée dans Gmail (aucune
  suppression ou automatisation n’a été mise en place). Les pièces nécessaires à une
  prestation ou à une obligation légale ont une conservation distincte.
- **Documents commerciaux** : les devis et contrats restent distincts de ces mentions.
  Cette modification ne crée pas de contrat type et ne prétend pas écarter les
  protections légales éventuellement applicables à certains petits professionnels.

Sources consultées le 3 octobre 2026 :
- https://entreprendre.service-public.gouv.fr/vosdroits/F31228
- https://www.economie.gouv.fr/files/files/directions_services/mediation-conso/Fiche%20pratique%20professionnels.pdf
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- https://www.cnil.fr/fr/conformite-rgpd-information-des-personnes-et-transparence
- https://policies.google.com/privacy/frameworks?hl=fr
