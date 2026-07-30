import re

with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# find anything between quotes
matches = re.findall(r'["\']([^"\']{20,})["\']', text)
# also try backticks
matches += re.findall(r'`([^`]{20,})`', text)
# also look for raw children: texts
matches += re.findall(r'children:([a-zA-Z0-9_,\.\- ]{20,})', text)
matches += re.findall(r'>([^<]{20,})<', text)

sentences = set()
for m in matches:
    m = m.strip()
    if len(m) > 30 and ' ' in m and not re.search(r'[{}\[\]\\]', m):
        words = m.split()
        # Ensure it looks like a sentence (mostly alphabetical)
        if len(words) > 4 and all(re.match(r'^[a-zA-Z0-9,\.\-\?!:]+$', w) for w in words):
            sentences.add(m)

for s in sorted(sentences):
    print(s)
