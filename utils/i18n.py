import json
import os
from functools import lru_cache

LANG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lang')
DEFAULT_LANG = 'fr'

@lru_cache(maxsize=1)
def load_translations():
    """Load all translations into a dictionary."""
    translations = {}
    if not os.path.exists(LANG_DIR):
        return translations

    for filename in os.listdir(LANG_DIR):
        if filename.endswith('.json'):
            lang_code = filename[:-5]
            filepath = os.path.join(LANG_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    translations[lang_code] = data
            except Exception as e:
                print(f"Error loading translation file {filename}: {e}")
                translations[lang_code] = {}

    return translations

def get_translation(lang_code, key):
    """
    Get translation for a specific key in a specific language.
    Falls back to French if key or language is not found.
    Key format: "section.subsection.key"
    """
    translations = load_translations()

    # Try specified language first, then fallback to French
    langs_to_try = [lang_code]
    if lang_code != DEFAULT_LANG:
        langs_to_try.append(DEFAULT_LANG)

    keys = key.split('.')

    for lang in langs_to_try:
        current_dict = translations.get(lang, {})
        found = True

        for k in keys:
            if isinstance(current_dict, dict) and k in current_dict:
                current_dict = current_dict[k]
            else:
                found = False
                break

        if found and not isinstance(current_dict, dict):
            return current_dict

    # If all fails, return the key itself
    return key
