"""Generate both static documents. Run with Python 3; no dependencies."""
from pathlib import Path
from html import escape
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
COPY = {
    'fr': {
        'title': 'Michel Do — Développement web & conseil technique | MDO Consultech',
        'description': 'Consultant indépendant à Marseille. Sites web, applications sur mesure et intégration IA. Audit IA gratuit pour identifier les usages adaptés à vos processus.',
        'nav': ['Expertises', 'Expériences', 'Approche'], 'contact': 'Parlons de votre projet',
        'skip': 'Aller au contenu', 'eyebrow': 'MICHEL DO · CONSULTANT INDÉPENDANT',
        'headline': 'Vos idées.<br>Mon expertise.<br><em>Votre prochain<br>chapitre.</em>',
        'intro': 'Sites web, applications métiers et intégration de l’IA : je conçois des solutions adaptées à vos besoins. Avec le recul d’un ingénieur senior et l’implication d’un partenaire.',
        'aiLabel': '04 / NOUVELLE EXPERTISE · INTELLIGENCE ARTIFICIELLE',
        'aiTitle': 'L’IA, là où elle<br><em>vous est utile.</em>',
        'aiText': 'J’accompagne l’intégration de l’IA dans vos outils et vos processus : assistance aux équipes, traitement de l’information ou automatisation de tâches répétitives. Le point de départ reste votre besoin métier.',
        'auditLabel': 'AUDIT IA GRATUIT',
        'auditTitle': 'Quels usages auraient du sens pour vous ?',
        'auditText': 'Un premier audit pour comprendre votre fonctionnement, repérer les tâches qui pourraient bénéficier de l’IA et évaluer la pertinence d’une intégration.',
        'auditItems': ['Faire le point sur vos processus et vos contraintes', 'Identifier des pistes concrètes et leurs limites', 'Définir une suite adaptée si un besoin se confirme'],
        'auditNote': 'L’audit peut aussi conclure qu’une intégration IA n’est pas nécessaire.',
        'auditCTA': 'Demander mon audit gratuit',
        'auditSubject': 'Demande d’audit IA gratuit',
        'auditLinkedIn': 'En parler sur LinkedIn',
        'email': 'Ou échangeons par e-mail', 'connect': 'Échanger sur LinkedIn', 'work': 'Découvrir mon expertise',
        'location': 'Basé à Marseille · Ouvert aux collaborations à distance',
        'scroll': 'FAISONS CONNAISSANCE', 'years': 'ans d’expérience', 'scope': 'Du besoin à la mise en ligne',
        'serviceLabel': '01 / EXPERTISES', 'serviceTitle': 'Le bon accompagnement,<br><em>à chaque étape.</em>',
        'serviceIntro': 'Un site à créer, une application à faire évoluer ou une équipe à renforcer : nous partons de votre besoin.',
        'services': [
            ('Sites web', 'Une présence en ligne à votre image.', 'Sites vitrines, portfolios et sites de présentation d’activité. Une expérience soignée, lisible sur tous les écrans et facile à parcourir.', ['Conception & développement', 'Responsive & accessibilité', 'Mise en ligne']),
            ('Applications sur mesure', 'Des outils pensés pour votre métier.', 'Applications métiers, plateformes web et intégrations. Je relie vos besoins, vos données et vos outils pour construire une solution cohérente.', ['Développement full stack', 'API & intégrations', 'Données & architecture']),
            ('Accompagnement technique', 'Du renfort au leadership.', 'Un regard expérimenté sur votre projet et une implication concrète : développement, refonte, choix d’architecture et accompagnement de vos équipes.', ['Refonte & évolution', 'Lead technique & mentorat', 'Qualité & industrialisation']),
        ],
        'expLabel': '02 / EXPÉRIENCES SÉLECTIONNÉES', 'expTitle': 'Du concret.<br><em>Et de la diversité.</em>',
        'expIntro': 'Quelques projets auxquels j’ai contribué, au croisement de la technique, du produit et des usages métier.',
        'projects': [
            ('2025 — 2026', 'RDT Logistic', 'Mission via AddixGroup · Lead Developer Full Stack', 'Repenser un ERP logistique.', 'Refonte complète de l’ERP avec une équipe de cinq développeurs, une Product Owner et un BA/UX Designer. Architecture, reprise des données clients, services de réservation de transport et facturation électronique.', ['Symfony', 'Vue.js', 'PostgreSQL', 'RabbitMQ'], 'ERP / LOGISTIQUE'),
            ('2020 — 2023', 'Maison.fr', 'Développeur Full Stack puis Lead Developer', 'Connecter les outils des professionnels.', 'Développement de la plateforme B2B pour les professionnels du bâtiment, puis accompagnement technique de l’équipe. Intégrations Salesforce et paiements, gestion des documents professionnels et suivi des performances.', ['Symfony', 'React', 'TypeScript', 'Stripe'], 'PLATEFORME / B2B'),
            ('2023 — 2025', 'R-Advertising', 'Développeur Full Stack', 'Construire une plateforme d’affiliation.', 'Conception d’une plateforme de génération et de gestion de liens affiliés. Catalogue indexé, tableaux de bord, traitements asynchrones et widgets WordPress pour les créateurs de contenu.', ['Symfony', 'Elasticsearch', 'RabbitMQ', 'WordPress'], 'PLATEFORME / AFFILIATION'),
        ],
        'approachLabel': '03 / APPROCHE', 'quote': 'Le code est un moyen.<br><em>Comprendre votre métier</em><br>fait la différence.',
        'approachIntro': 'Plus de dix ans à construire des produits, faire évoluer des applications et travailler aux côtés des équipes. Une conviction : les bons choix techniques commencent par les bonnes questions.',
        'steps': [('Build.', 'Comprendre & construire', 'Clarifier vos besoins, choisir une solution adaptée et lui donner forme.'), ('Solve.', 'Résoudre & simplifier', 'Faire face aux contraintes réelles, connecter les outils et débloquer les sujets techniques.'), ('Evolve.', 'Améliorer & transmettre', 'Faire évoluer le produit, soigner la qualité et partager les connaissances.')],
        'contactLabel': '04 / ET LA SUITE ?', 'contactTitle': 'Votre prochain projet<br><em>commence par un échange.</em>',
        'contactText': 'Un site, une application, un besoin de renfort ou un projet IA ? Discutons de ce que vous souhaitez construire.',
        'cv': 'Mon parcours en détail', 'cvFR': 'CV français', 'cvEN': 'CV anglais',
        'github': 'Voir mon GitHub', 'footer': 'Conseil & développement web et logiciel', 'top': 'Retour en haut',
        'pause': 'Mettre en pause', 'play': 'Animer le logo',
    },
    'en': {
        'title': 'Michel Do — Web Development & Technical Consulting | MDO Consultech',
        'description': 'Independent consultant in Marseille. Websites, custom applications and AI integration. Free AI assessment to identify relevant uses for your business processes.',
        'nav': ['Expertise', 'Experience', 'Approach'], 'contact': 'Let’s talk about your project',
        'skip': 'Skip to content', 'eyebrow': 'MICHEL DO · INDEPENDENT CONSULTANT',
        'headline': 'Your ideas.<br>My expertise.<br><em>Your next<br>chapter.</em>',
        'intro': 'Websites, business applications and AI integration: I build solutions around your needs. Bringing a senior engineer’s perspective and a partner’s commitment.',
        'aiLabel': '04 / NEW EXPERTISE · ARTIFICIAL INTELLIGENCE',
        'aiTitle': 'AI, where it<br><em>works for you.</em>',
        'aiText': 'I help integrate AI into your tools and workflows: supporting teams, processing information or automating repetitive tasks. Your business needs are always the starting point.',
        'auditLabel': 'FREE AI ASSESSMENT',
        'auditTitle': 'Where could AI make sense for you?',
        'auditText': 'An initial assessment to understand how you work, identify tasks that could benefit from AI and assess whether integration would be worthwhile.',
        'auditItems': ['Review your workflows and constraints', 'Identify practical opportunities and their limitations', 'Define suitable next steps if a need emerges'],
        'auditNote': 'The assessment may also conclude that AI integration is not needed.',
        'auditCTA': 'Request my free assessment',
        'auditSubject': 'Free AI assessment request',
        'auditLinkedIn': 'Discuss it on LinkedIn',
        'email': 'Or get in touch by email', 'connect': 'Let’s connect on LinkedIn', 'work': 'Explore my expertise',
        'location': 'Based in Marseille, France · Open to remote collaboration',
        'scroll': 'LET’S GET ACQUAINTED', 'years': 'years of experience', 'scope': 'From requirements to launch',
        'serviceLabel': '01 / EXPERTISE', 'serviceTitle': 'The right support,<br><em>at every stage.</em>',
        'serviceIntro': 'A new website, an application to improve or a team to support: your needs are our starting point.',
        'services': [
            ('Websites', 'An online presence that feels like you.', 'Business websites, portfolios and company sites. A considered experience that works across screens and makes your content easy to explore.', ['Design & development', 'Responsive & accessible', 'Launch']),
            ('Custom applications', 'Tools built around your business.', 'Business applications, web platforms and integrations. I bring your requirements, data and tools together into a coherent solution.', ['Full-stack development', 'APIs & integrations', 'Data & architecture']),
            ('Technical consulting', 'From hands-on support to leadership.', 'An experienced perspective and practical involvement: development, application modernization, architecture decisions and guidance for your team.', ['Modernization & evolution', 'Technical leadership & mentoring', 'Quality & delivery practices']),
        ],
        'expLabel': '02 / SELECTED EXPERIENCE', 'expTitle': 'Real projects.<br><em>Different challenges.</em>',
        'expIntro': 'A selection of projects I have contributed to, connecting engineering, product thinking and business needs.',
        'projects': [
            ('2025 — 2026', 'RDT Logistic', 'Assignment through AddixGroup · Lead Full Stack Developer', 'Rebuilding a logistics ERP.', 'A complete ERP rebuild with five developers, a Product Owner and a BA/UX Designer. Architecture, customer data migration, transport booking services and electronic invoicing.', ['Symfony', 'Vue.js', 'PostgreSQL', 'RabbitMQ'], 'ERP / LOGISTICS'),
            ('2020 — 2023', 'Maison.fr', 'Full Stack Developer, then Lead Developer', 'Connecting tools for trade professionals.', 'Development of the B2B platform for building-industry professionals, followed by technical team leadership. Salesforce and payment integrations, professional document management and performance tracking.', ['Symfony', 'React', 'TypeScript', 'Stripe'], 'PLATFORM / B2B'),
            ('2023 — 2025', 'R-Advertising', 'Full Stack Developer', 'Building an affiliate platform.', 'Design and development of an affiliate-link generation and management platform. An indexed catalog, dashboards, asynchronous processing and WordPress widgets for content creators.', ['Symfony', 'Elasticsearch', 'RabbitMQ', 'WordPress'], 'PLATFORM / AFFILIATE MARKETING'),
        ],
        'approachLabel': '03 / APPROACH', 'quote': 'Code is a means.<br><em>Understanding your business</em><br>makes the difference.',
        'approachIntro': 'Over ten years building products, evolving applications and working alongside teams. One conviction: good technical decisions start with the right questions.',
        'steps': [('Build.', 'Understand & create', 'Clarify your needs, choose an appropriate solution and bring it to life.'), ('Solve.', 'Resolve & simplify', 'Work through real-world constraints, connect tools and remove technical obstacles.'), ('Evolve.', 'Improve & share', 'Develop the product further, care for its quality and share knowledge.')],
        'contactLabel': '04 / WHAT’S NEXT?', 'contactTitle': 'Your next project<br><em>starts with a conversation.</em>',
        'contactText': 'A website, an application, an extra pair of experienced hands or an AI project? Let’s talk about what you want to build.',
        'cv': 'Explore my background', 'cvFR': 'French CV', 'cvEN': 'English CV',
        'github': 'Explore my GitHub', 'footer': 'Web & software development consulting', 'top': 'Back to top',
        'pause': 'Pause animation', 'play': 'Animate logo',
    },
}

def render(lang):
    d = COPY[lang]
    base = './' if lang == 'fr' else '../'
    french, english = ('./', './en/') if lang == 'fr' else ('../', './')
    email = f'<p class="email-contact"><span>{d["email"]}</span><a href="mailto:domichelviet+pro@gmail.com">domichelviet+pro@gmail.com <span aria-hidden="true">↗</span></a></p>'
    nav = ''.join(f'<a href="#{s}">{label}</a>' for s, label in zip(['services', 'experience', 'approach'], d['nav']))
    services = ''.join(f'''<article class="service"><span class="service-number">0{i}</span><h3>{title}</h3><p class="service-lead">{lead}</p><p>{body}</p><ul>{''.join(f'<li>{item}</li>' for item in items)}</ul></article>''' for i, (title, lead, body, items) in enumerate(d['services'], 1))
    projects = ''.join(f'''<article class="project"><div class="project-index"><span>0{i}</span><p>{category}</p></div><div class="project-client"><p class="dates">{dates}</p><h3>{client}</h3><p class="role">{role}</p></div><div class="project-story"><h4>{headline}</h4><p>{body}</p><ul class="tags">{''.join(f'<li>{tag}</li>' for tag in tags)}</ul></div></article>''' for i, (dates, client, role, headline, body, tags, category) in enumerate(d['projects'], 1))
    steps = ''.join(f'<article><span class="step-index">0{i}</span><h3>{word}</h3><h4>{title}</h4><p>{body}</p></article>' for i, (word, title, body) in enumerate(d['steps'], 1))
    audit_url = 'mailto:domichelviet+pro@gmail.com?subject=' + quote(d['auditSubject'])
    ai_offer = f'''<section class="ai-offer" id="ai" aria-labelledby="ai-title"><div class="ai-intro"><p class="eyebrow">{d['aiLabel']}</p><h3 id="ai-title">{d['aiTitle']}</h3><p>{d['aiText']}</p></div><div class="audit"><p class="audit-badge">{d['auditLabel']}</p><h4>{d['auditTitle']}</h4><p>{d['auditText']}</p><ul>{''.join(f'<li>{item}</li>' for item in d['auditItems'])}</ul><p class="audit-note">{d['auditNote']}</p><a class="button button-wine" href="{audit_url}">{d['auditCTA']} <span aria-hidden="true">↗</span></a><a class="audit-linkedin" href="https://www.linkedin.com/in/domichel/">{d['auditLinkedIn']} ↗</a></div></section>'''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{d['title']}</title><meta name="description" content="{escape(d['description'], quote=True)}">
  <meta name="theme-color" content="#7c0f1a">
  <link rel="alternate" hreflang="fr" href="{french}"><link rel="alternate" hreflang="en" href="{english}">
  <link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{base}assets/site.css">
  <script src="{base}assets/logo.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{d['skip']}</a>
<div class="hero-shell" id="top">
  <header class="header wrap">
    <a href="#top" class="wordmark" aria-label="MDO Consultech"><span>MDO<span class="brand-dot">.</span></span><small>CONSULTECH</small></a>
    <nav class="main-nav" aria-label="{'Navigation principale' if lang == 'fr' else 'Main navigation'}">{nav}</nav>
    <div class="header-end"><nav class="languages" aria-label="{'Langue' if lang == 'fr' else 'Language'}"><a href="{french}" lang="fr" hreflang="fr" {'aria-current="page"' if lang == 'fr' else ''}>FR</a><span>/</span><a href="{english}" lang="en" hreflang="en" {'aria-current="page"' if lang == 'en' else ''}>EN</a></nav><a href="#contact" class="header-contact">{d['contact']} <span aria-hidden="true">↗</span></a></div>
  </header>
</div>
<main id="main">
<div class="hero-shell">
  <section class="hero wrap" aria-labelledby="hero-title">
    <div class="hero-copy"><p class="eyebrow"><span class="gold-dash"></span>{d['eyebrow']}</p><h1 id="hero-title">{d['headline']}</h1><p class="intro">{d['intro']}</p><div class="hero-actions"><a class="button button-gold" href="https://www.linkedin.com/in/domichel/">{d['connect']} <span aria-hidden="true">↗</span></a><a class="text-link" href="#services">{d['work']} <span aria-hidden="true">↓</span></a></div>{email}<a class="hero-audit" href="#ai">{d["auditLabel"]} <span aria-hidden="true">↗</span></a></div>
    <div class="hero-art"><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><span class="orbit-star" aria-hidden="true">✦</span><div class="logo-stage"><svg class="static-logo" viewBox="140 120 220 265" role="img" aria-label="{'Emblème MDO Consultech' if lang == 'fr' else 'MDO Consultech emblem'}"><image href="{base}assets/logo.png" width="510" height="540"/></svg><canvas class="liquid-logo" width="440" height="530" aria-hidden="true" data-image="{base}assets/logo.png"></canvas></div><p class="art-name">MDO</p><p class="art-subtitle">CONSULTECH</p><p class="art-motto">BUILD <span>·</span> SOLVE <span>·</span> EVOLVE</p><button class="animation-toggle" type="button" hidden data-pause="{d['pause']}" data-play="{d['play']}" aria-label="{d['pause']}"><span aria-hidden="true">{d['pause']}</span></button></div>
    <div class="hero-bottom"><p><span class="location-dot"></span>{d['location']}</p><a href="#services">{d['scroll']} <span aria-hidden="true">↓</span></a></div>
  </section>
</div>
<div class="proof-strip"><div class="wrap proof-content"><p><strong>10<span>+</span></strong> {d['years']}</p><span class="proof-divider"></span><p>Senior Software Engineer <span class="proof-dot">·</span> Lead Developer</p><span class="proof-divider"></span><p>{d['scope']}</p></div></div>
<section class="section wrap" id="services" aria-labelledby="service-title"><div class="section-heading"><div><p class="eyebrow">{d['serviceLabel']}</p><h2 id="service-title">{d['serviceTitle']}</h2></div><p class="section-intro">{d['serviceIntro']}</p></div><div class="services-grid">{services}</div>{ai_offer}</section>
<section class="experience-section" id="experience" aria-labelledby="experience-title"><div class="wrap section"><div class="section-heading"><div><p class="eyebrow">{d['expLabel']}</p><h2 id="experience-title">{d['expTitle']}</h2></div><p class="section-intro">{d['expIntro']}</p></div><div class="projects">{projects}</div></div></section>
<section class="section wrap approach" id="approach" aria-labelledby="approach-title"><p class="eyebrow">{d['approachLabel']}</p><div class="approach-heading"><h2 id="approach-title">{d['quote']}</h2><p>{d['approachIntro']}</p></div><div class="steps">{steps}</div></section>
<section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="wrap contact-inner"><p class="eyebrow">{d['contactLabel']}</p><h2 id="contact-title">{d['contactTitle']}</h2><p class="contact-description">{d['contactText']}</p><a class="button button-gold" href="https://www.linkedin.com/in/domichel/">{d['connect']} <span aria-hidden="true">↗</span></a>{email}<a class="github-contact" href="https://github.com/Milkshek">{d["github"]} <span aria-hidden="true">↗</span></a><div class="cv-row"><span>{d['cv']}</span><a href="{base}assets/cv/Michel-Do-CV-FR.pdf" download hreflang="fr">{d['cvFR']} <small>PDF</small><span aria-hidden="true">↓</span></a><a href="{base}assets/cv/Michel-Do-CV-EN.pdf" download hreflang="en">{d['cvEN']} <small>PDF</small><span aria-hidden="true">↓</span></a></div></div></section>
</main>
<footer class="footer"><div class="wrap footer-inner"><a href="#top" class="footer-brand">MDO <span>CONSULTECH</span></a><p>© 2026 Michel Do <span>·</span> {d['footer']}</p><a class="footer-github" href="https://github.com/Milkshek">GitHub <span aria-hidden="true">↗</span></a><a href="#top">{d['top']} ↑</a></div></footer>
</body></html>'''

for lang, name in [('fr', 'index.html'), ('en', 'en/index.html')]:
    destination = ROOT / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render(lang))
print('Built index.html and en/index.html')
