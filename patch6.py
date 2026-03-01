import re

with open("templates/index.html", "r") as f:
    content = f.read()

# Replace Twitter (X) link manually since it seems the regex missed it due to the parenthesis
content = content.replace(
    '<a href="#" target="_blank" rel="noopener noreferrer" class="w-12 h-12 rounded-full glass-premium flex items-center justify-center text-adaptive-muted hover:text-adaptive hover:scale-110 hover:-translate-y-1 transition-all" aria-label="X (Twitter)">',
    '<a href="{{ settings.get(\'x\', \'#\') }}" target="_blank" rel="noopener noreferrer" class="w-12 h-12 rounded-full glass-premium flex items-center justify-center text-adaptive-muted hover:text-adaptive hover:scale-110 hover:-translate-y-1 transition-all" aria-label="X (Twitter)">'
)

with open("templates/index.html", "w") as f:
    f.write(content)
