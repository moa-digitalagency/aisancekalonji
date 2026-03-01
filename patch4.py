import re

with open("templates/index.html", "r") as f:
    content = f.read()

# Replace everything inside the grid with the jinja loop
start_marker = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">\n                    \n'
end_marker = '\n                </div>\n            </section>\n\n            <!-- FOOTER -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_grid_content = '''<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    {% for item in portfolio %}
                    <a href="{{ item.link if item.link else '#' }}" target="_blank" rel="noopener noreferrer" class="glass-premium p-6 md:p-8 rounded-[32px] group relative overflow-hidden flex flex-col justify-between hover:-translate-y-2 transition-transform duration-500 gs-reveal cursor-pointer min-h-[240px]">
                        <div class="flex justify-between items-start mb-6">
                            <div class="w-12 h-12 rounded-full bg-{{ item.color_class }}/10 flex items-center justify-center text-{{ item.color_class }}">
                                <i class="{{ item.icon_class }} text-xl"></i>
                            </div>
                            <div class="w-8 h-8 rounded-full glass-premium flex items-center justify-center text-adaptive-muted group-hover:text-adaptive transition-colors">
                                <i class="fas fa-arrow-up-right-from-square text-xs"></i>
                            </div>
                        </div>
                        <div>
                            <h3 class="font-display font-medium text-xl text-adaptive mb-2 group-hover:text-{{ item.color_class }} transition-colors">{{ item.title }}</h3>
                            <p class="font-sans text-sm text-adaptive-muted font-light mb-4">{{ item.description }}</p>
                            {% if item.link %}
                            <span class="font-mono text-[10px] uppercase text-adaptive-muted tracking-widest">{{ item.link | replace("https://", "") | replace("http://", "") | replace("www.", "") | truncate(25, True, '...') }}</span>
                            {% endif %}
                        </div>
                    </a>
                    {% endfor %}'''

    content = content[:start_idx] + new_grid_content + content[end_idx:]

with open("templates/index.html", "w") as f:
    f.write(content)
