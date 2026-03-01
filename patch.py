with open("templates/index.html", "r") as f:
    content = f.read()

content = content.replace(
    "<title>Aisance KALONJI | Consultant IA & Cybersécurité</title>",
    "{{ seo.custom_head_script | safe if seo and seo.custom_head_script else '' }}\n    <title>{{ seo.meta_title if seo and seo.meta_title else 'Aisance KALONJI | Consultant IA & Cybersécurité' }}</title>\n    {% if seo and seo.meta_description %}<meta name=\"description\" content=\"{{ seo.meta_description }}\">{% endif %}"
)

content = content.replace(
    "<body class=\"antialiased\">\n\n    <!-- PRELOADER -->",
    "<body class=\"antialiased\">\n    {% macro get_image_url(img_obj, fallback_url) -%}\n        {%- if img_obj and img_obj.is_uploaded and img_obj.upload_path -%}\n            {{ url_for('static', filename=img_obj.upload_path) }}\n        {%- elif img_obj and img_obj.image_url -%}\n            {{ img_obj.image_url }}\n        {%- else -%}\n            {{ fallback_url }}\n        {%- endif -%}\n    {%- endmacro %}\n\n    <!-- PRELOADER -->"
)

with open("templates/index.html", "w") as f:
    f.write(content)
