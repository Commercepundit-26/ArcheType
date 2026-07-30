import re
with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all string literals (single, double, or backtick)
pattern = r'(["\'`])(.*?)\1'
matches = re.findall(pattern, content)

for _, text in matches:
    text = text.strip()
    # Filter for human readable sentences (at least 4 words, spaces, some capitalization)
    if len(text) > 30 and ' ' in text and not re.search(r'[{}\[\]\\]', text):
        if re.search(r'[A-Z]', text) and re.search(r'[a-z]{4,}', text):
            # Ignore css classes and html
            if 'text-' not in text and 'bg-' not in text and 'hover:' not in text and 'data-' not in text and '<' not in text:
                print(text)
