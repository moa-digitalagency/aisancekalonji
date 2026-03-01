import re

with open("templates/index.html", "r") as f:
    content = f.read()

# Update Footer & Contacts

# 1. Email button in footer
content = content.replace(
    '<a href="mailto:hello@aisancekalonji.com" class="btn-glass !px-8 !py-4 !text-lg backdrop-blur-md w-full sm:w-auto">\n                                <i class="fas fa-envelope mr-2"></i> hello@aisancekalonji.com\n                            </a>',
    '<a href="mailto:{{ settings.get(\'email\', \'hello@aisancekalonji.com\') }}" class="btn-glass !px-8 !py-4 !text-lg backdrop-blur-md w-full sm:w-auto">\n                                <i class="fas fa-envelope mr-2"></i> {{ settings.get(\'email\', \'hello@aisancekalonji.com\') }}\n                            </a>'
)

# 2. Social Media Links
social_links = {
    'Facebook': 'facebook',
    'Instagram': 'instagram',
    'X (Twitter)': 'x',
    'LinkedIn': 'linkedin',
    'WhatsApp': 'whatsapp'
}

for aria_label, key in social_links.items():
    pattern = f'<a href="#" target="_blank" rel="noopener noreferrer" class="([^"]*)" aria-label="{aria_label}">'
    replacement = f'<a href="{{{{ settings.get(\'{key}\', \'#\') }}}}" target="_blank" rel="noopener noreferrer" class="\\1" aria-label="{aria_label}">'
    content = re.sub(pattern, replacement, content)

# 3. Phone number
content = content.replace(
    '<p class="mt-4 font-mono text-xs">+212 699 14 00 01</p>',
    '<p class="mt-4 font-mono text-xs">{{ settings.get(\'phone\', \'+212 699 14 00 01\') }}</p>'
)

with open("templates/index.html", "w") as f:
    f.write(content)
