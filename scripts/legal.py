"""Bilingual legal copy. Update here, then run build.py. No INPI source document is published."""
from html import escape
from hashlib import sha256

EMAIL = 'domichelviet+pro@gmail.com'
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
GITHUB_PRIVACY = 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'
GOOGLE_PRIVACY = 'https://policies.google.com/privacy'
GOOGLE_TRANSFERS = 'https://policies.google.com/privacy/frameworks'

COPY = {
    'fr': {
        'title': 'Mentions légales et confidentialité', 'home': 'Retour au portfolio',
        'intro': 'Les informations sur MDO Consultech et le traitement de vos données.',
        'sections': [
            ('Éditeur du site', f'''<p><strong>MDO Consultech — Michel Viet Do, entrepreneur individuel (EI)</strong><br>
22 avenue Elleon, résidence Château Saint-Cyr, bâtiment Les Cèdres<br>13010 Marseille, France</p>
<p>SIREN : 811 983 550 · SIRET : 811 983 550 00039<br>Activité : conseil et développement informatique — APE 6202A.</p>
<p>E-mail : {MAIL}<br>Téléphone : <a href="tel:+33622714063">+33 6 22 71 40 63</a></p>
<p>Directeur de la publication : Michel Viet Do.</p>
<p>Les prestations de MDO Consultech sont exclusivement destinées aux professionnels agissant dans le cadre de leur activité professionnelle.</p>'''),
            ('Hébergement', '''<p>GitHub Pages, un service de GitHub, Inc.<br>88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.<br>Téléphone : <a href="tel:+18774484820">+1 877 448 4820</a>.<br>Contact : <a href="https://support.github.com/">GitHub Support</a>.</p>'''),
            ('Vos échanges avec MDO Consultech', f'''<p>Michel Viet Do, aux coordonnées ci-dessus, est responsable du traitement des données que vous lui communiquez. Vos coordonnées, messages et pièces jointes servent à répondre à vos demandes, étudier vos projets et organiser les audits IA.</p>
<p>Le traitement repose sur les mesures précontractuelles prises à votre demande pour un projet de prestation, ou sur l’intérêt légitime à répondre aux autres sollicitations professionnelles. Fournir ces informations est facultatif ; des coordonnées et une description du besoin sont nécessaires pour vous répondre.</p>
<p>Les échanges sans suite commerciale sont supprimés au plus tard douze mois après la clôture de la demande. En cas de prestation, les informations nécessaires sont conservées pendant la relation contractuelle, puis seules les pièces nécessaires aux obligations légales ou à la défense des droits sont archivées pendant les délais applicables, notamment dix ans pour les pièces comptables.</p>
<p>Les échanges sont destinés à Michel Viet Do et passent par Gmail, le service de messagerie de Google. Google peut traiter des données hors de l’Espace économique européen, notamment aux États-Unis. Consultez ses <a href="{GOOGLE_PRIVACY}?hl=fr">règles de confidentialité</a> et les <a href="{GOOGLE_TRANSFERS}?hl=fr">garanties encadrant ces transferts</a> (décisions d’adéquation et, lorsque nécessaire, clauses contractuelles types).</p>
<p>Vous pouvez demander l’accès, la rectification, l’effacement ou la limitation du traitement de vos données. Selon les conditions prévues par le RGPD, vous disposez aussi d’un droit d’opposition et de portabilité. Contact : {MAIL}. Vous pouvez adresser une réclamation à la <a href="https://www.cnil.fr/fr/plaintes">CNIL</a>.</p>'''),
            ('Navigation et liens externes', f'''<p>Ce site ne comporte ni formulaire, ni outil de mesure d’audience, ni traceur publicitaire. Les liens e-mail ouvrent votre messagerie.</p>
<p>GitHub Pages enregistre les adresses IP des visiteurs à des fins de sécurité, y compris sans connexion à un compte GitHub. GitHub précise ses pratiques, ses critères de conservation et les garanties applicables aux transferts internationaux dans sa <a href="{GITHUB_PRIVACY}">politique de confidentialité</a>.</p>
<p>Les liens vers LinkedIn et GitHub vous conduisent vers des services tiers dont les politiques de confidentialité s’appliquent lorsque vous les utilisez.</p>'''),
        ],
    },
    'en': {
        'title': 'Legal notice and privacy', 'home': 'Back to portfolio',
        'intro': 'Information about MDO Consultech and how your personal data is handled.',
        'sections': [
            ('Website publisher', f'''<p><strong>MDO Consultech — Michel Viet Do, sole trader (entrepreneur individuel, EI)</strong><br>
22 avenue Elleon, résidence Château Saint-Cyr, bâtiment Les Cèdres<br>13010 Marseille, France</p>
<p>SIREN: 811 983 550 · SIRET: 811 983 550 00039<br>Business: IT consulting and software development — APE 6202A.</p>
<p>Email: {MAIL}<br>Telephone: <a href="tel:+33622714063">+33 6 22 71 40 63</a></p>
<p>Publication director: Michel Viet Do.</p>
<p>MDO Consultech services are exclusively intended for clients acting in the course of their business or professional activity.</p>'''),
            ('Hosting', '''<p>GitHub Pages, a service provided by GitHub, Inc.<br>88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States.<br>Telephone: <a href="tel:+18774484820">+1 877 448 4820</a>.<br>Contact: <a href="https://support.github.com/">GitHub Support</a>.</p>'''),
            ('Your correspondence with MDO Consultech', f'''<p>Michel Viet Do, reachable at the contact details above, is the controller of the personal data you provide. Your contact details, messages and attachments are used to answer enquiries, assess projects and organise AI assessments.</p>
<p>Processing is based on steps taken at your request before entering a service contract, or on the legitimate interest in responding to other business enquiries. Providing information is optional; contact details and a description of your needs are necessary to respond.</p>
<p>Enquiries that do not lead to a business relationship are deleted no later than twelve months after the enquiry is closed. For commissioned work, necessary information is retained during the contractual relationship. Afterwards, only records needed for legal obligations or legal claims are archived for the applicable periods, including ten years for accounting records.</p>
<p>Correspondence is intended for Michel Viet Do and is processed through Google's Gmail service. Google may process data outside the European Economic Area, including in the United States. See its <a href="{GOOGLE_PRIVACY}?hl=en">privacy policy</a> and <a href="{GOOGLE_TRANSFERS}?hl=en">international transfer safeguards</a> (adequacy decisions and, where necessary, standard contractual clauses).</p>
<p>You may request access, rectification, erasure or restriction of processing. Subject to the conditions set by the GDPR, you also have rights to object and to data portability. Contact: {MAIL}. You may lodge a complaint with the <a href="https://www.cnil.fr/en">CNIL</a> or your competent data protection authority.</p>'''),
            ('Browsing and external links', f'''<p>This site has no contact form, analytics tool or advertising tracker. Email links open your email application.</p>
<p>GitHub Pages logs visitors’ IP addresses for security purposes, even when they are not signed in to GitHub. GitHub explains its practices, retention criteria and international transfer safeguards in its <a href="{GITHUB_PRIVACY}">privacy statement</a>.</p>
<p>LinkedIn and GitHub links lead to third-party services whose privacy policies apply when you use them.</p>'''),
        ],
    },
}


def render_legal(lang, root, site_url):
    data = COPY[lang]
    base = './' if lang == 'fr' else '../'
    home = './'
    fr = site_url + 'mentions-legales.html'
    en = site_url + 'en/legal-notice.html'
    french = './mentions-legales.html' if lang == 'fr' else '../mentions-legales.html'
    english = './en/legal-notice.html' if lang == 'fr' else './legal-notice.html'
    css = sha256((root / 'assets/site.css').read_bytes()).hexdigest()[:12]
    sections = ''.join(f'<section><h2>{escape(title)}</h2>{body}</section>' for title, body in data['sections'])
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{data['title']} | MDO Consultech</title><meta name="description" content="{data['intro']}">
<link rel="canonical" href="{fr if lang == 'fr' else en}">
<link rel="alternate" hreflang="fr" href="{fr}"><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="x-default" href="{fr}">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{base}assets/site.css?v={css}">
</head><body class="legal-page"><a class="skip" href="#main">{'Aller au contenu' if lang == 'fr' else 'Skip to content'}</a>
<div class="hero-shell"><header class="header wrap"><a class="wordmark" href="{home}" aria-label="MDO Consultech"><span>MDO<span class="brand-dot">.</span></span><small>CONSULTECH</small></a>
<nav class="languages" aria-label="{'Langue' if lang == 'fr' else 'Language'}"><a href="{french}" lang="fr" hreflang="fr" {'aria-current="page"' if lang == 'fr' else ''}>FR</a><span>/</span><a href="{english}" lang="en" hreflang="en" {'aria-current="page"' if lang == 'en' else ''}>EN</a></nav></header></div>
<main class="wrap legal-content" id="main"><a class="legal-back" href="{home}">← {data['home']}</a><h1>{data['title']}</h1><p class="legal-intro">{data['intro']}</p>{sections}</main>
<footer class="footer"><div class="wrap footer-inner"><span class="footer-brand">MDO <span>CONSULTECH</span></span><p>© 2026 Michel Viet Do EI</p><a href="{home}">{data['home']} ↑</a></div></footer>
</body></html>'''
