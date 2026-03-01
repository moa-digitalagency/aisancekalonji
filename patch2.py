with open("templates/index.html", "r") as f:
    content = f.read()

# Replace hero light image
content = content.replace(
    '<img src="https://i.ibb.co/23nxjv1R/AK-Light.png" class="w-full h-full object-cover object-top img-parallax block dark:hidden" data-speed="0.8" alt="Aisance Kalonji Portrait Light">',
    '<img src="{{ get_image_url(page_images.hero_light, \'https://i.ibb.co/23nxjv1R/AK-Light.png\') }}" class="w-full h-full object-cover object-top img-parallax block dark:hidden" data-speed="0.8" alt="Aisance Kalonji Portrait Light">'
)

# Replace hero dark image
content = content.replace(
    '<img src="https://i.ibb.co/0RrbS4b1/AK-Dark.png" class="w-full h-full object-cover object-top img-parallax hidden dark:block" data-speed="0.8" alt="Aisance Kalonji Portrait Dark">',
    '<img src="{{ get_image_url(page_images.hero_dark, \'https://i.ibb.co/0RrbS4b1/AK-Dark.png\') }}" class="w-full h-full object-cover object-top img-parallax hidden dark:block" data-speed="0.8" alt="Aisance Kalonji Portrait Dark">'
)

# Replace vision image
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1531384441138-2736e62e0919?q=80&w=2000&auto=format&fit=crop" data-speed="0.95" class="img-parallax" alt="Vision et Stratégie">',
    '<img src="{{ get_image_url(page_images.vision, \'https://images.unsplash.com/photo-1531384441138-2736e62e0919?q=80&w=2000&auto=format&fit=crop\') }}" data-speed="0.95" class="img-parallax" alt="Vision et Stratégie">'
)

# Replace book section image
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=1000&auto=format&fit=crop" alt="Vade-mecum de la sécurité numérique" class="w-full h-full object-cover opacity-90">',
    '<img src="{{ get_image_url(page_images.book, \'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=1000&auto=format&fit=crop\') }}" alt="Vade-mecum de la sécurité numérique" class="w-full h-full object-cover opacity-90">'
)

# Replace portrait image (CTA section)
content = content.replace(
    '<img src="https://i.ibb.co/N6GMYcy9/Use-my-photo-202511241827.jpg" alt="Aisance Kalonji" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700">',
    '<img src="{{ get_image_url(page_images.portrait, \'https://i.ibb.co/N6GMYcy9/Use-my-photo-202511241827.jpg\') }}" alt="Aisance Kalonji" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700">'
)

with open("templates/index.html", "w") as f:
    f.write(content)
