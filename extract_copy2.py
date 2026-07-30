import re
with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract any string literal that contains spaces and is longer than 20 chars
matches = re.findall(r'(["\'])(.{20,200}?)\1', content)
unique_texts = set()
for _, text in matches:
    if ' ' in text and not re.search(r'[\{\}\[\]\\]', text) and not text.startswith('<'):
        if re.search(r'[A-Z]', text) and not re.search(r'(hover|flex-|text-|bg-|padding|margin|data-)', text):
            unique_texts.add(text.strip())

for t in sorted(unique_texts):
    print(t)
