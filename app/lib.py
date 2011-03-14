import re

def title_to_path(title):
    """
    Follows our convention of converting a PB title to a path by
    replacing spaces with hyphens and removing any non-alphanumeric
    characters (including other hyphens)
    """
    title_path = re.sub(r'[^a-zA-Z0-9]', r'', title)
    title_path = re.sub(r'\s+', r'\-', title_path)
    return title_path