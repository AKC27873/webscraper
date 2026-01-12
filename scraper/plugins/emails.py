import re 

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract(html):
    return list(set(re.findall(EMAIL_REGEX, html)))
