import re

with open("templates/index.html", "r") as f:
    content = f.read()

# Replace book section content
# 1. Book title
content = content.replace(
    '<h3 class="font-display text-white text-3xl font-bold mb-3 leading-tight drop-shadow-lg">Vade-mecum<br><span class="text-xl font-light text-white/90">de la sécurité numérique</span></h3>',
    '<h3 class="font-display text-white text-3xl font-bold mb-3 leading-tight drop-shadow-lg">{{ book.title if book else "Vade-mecum de la sécurité numérique" }}</h3>'
)

# 2. Book subtitle
content = content.replace(
    '<p class="text-white/70 font-mono text-xs uppercase tracking-widest">Aisance Kalonji</p>',
    '<p class="text-white/70 font-mono text-xs uppercase tracking-widest">{{ book.subtitle if book else "Aisance Kalonji" }}</p>'
)

# 3. Book section title
content = content.replace(
    '<h2 class="font-display text-4xl md:text-5xl font-medium mb-6 text-adaptive leading-[1.1]">\n                            Le Vade-mecum de <br>\n                            <span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-purple-500">la sécurité numérique.</span>\n                        </h2>',
    '<h2 class="font-display text-4xl md:text-5xl font-medium mb-6 text-adaptive leading-[1.1]">\n                            {{ book.title if book else "Le Vade-mecum de la sécurité numérique" }}\n                        </h2>'
)

# 4. Book description
content = content.replace(
    '<p class="font-sans text-adaptive-muted text-lg font-light mb-8 leading-relaxed max-w-xl mx-auto lg:mx-0">\n                            Un guide essentiel et pratique conçu pour démystifier l\'hygiène numérique. À travers cet ouvrage, je partage des stratégies concrètes et des protocoles de sécurité pour protéger les actifs digitaux des entreprises et des particuliers face aux menaces modernes.\n                        </p>',
    '<p class="font-sans text-adaptive-muted text-lg font-light mb-8 leading-relaxed max-w-xl mx-auto lg:mx-0">\n                            {{ book.description if book else "Un guide essentiel et pratique conçu pour démystifier l\'hygiène numérique. À travers cet ouvrage, je partage des stratégies concrètes et des protocoles de sécurité pour protéger les actifs digitaux des entreprises et des particuliers face aux menaces modernes." }}\n                        </p>'
)

# 5. Book CTA
content = content.replace(
    '<a href="https://www.cyberconfiance.com" target="_blank" rel="noopener noreferrer" class="btn-solid !px-8 !py-4 shadow-lg hover:shadow-[0_0_30px_rgba(59,130,246,0.4)] !text-base transition-all inline-flex items-center group w-full sm:w-auto justify-center">\n                                Obtenir mon exemplaire <i class="fas fa-arrow-right ml-3 group-hover:translate-x-1 transition-transform"></i>\n                            </a>',
    '<a href="{{ book.cta_link if book and book.cta_link else \'https://www.cyberconfiance.com\' }}" target="_blank" rel="noopener noreferrer" class="btn-solid !px-8 !py-4 shadow-lg hover:shadow-[0_0_30px_rgba(59,130,246,0.4)] !text-base transition-all inline-flex items-center group w-full sm:w-auto justify-center">\n                                {{ book.cta_text if book and book.cta_text else \'Obtenir mon exemplaire\' }} <i class="fas fa-arrow-right ml-3 group-hover:translate-x-1 transition-transform"></i>\n                            </a>'
)

with open("templates/index.html", "w") as f:
    f.write(content)
