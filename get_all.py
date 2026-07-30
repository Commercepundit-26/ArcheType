import re

with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# find anything between quotes
matches = re.findall(r'["\'](.*?)["\']', text)
matches += re.findall(r'`(.*?)`', text)

for m in matches:
    if len(m) > 40 and ' ' in m and not re.search(r'[{}\[\]\\]', m) and not re.search(r'<|>', m) and not m.startswith('http'):
        print(m)
