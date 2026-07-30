import re
with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract strings
strings = re.findall(r'(["\'])(.*?)\1', content)
for _, text in strings:
    text = text.strip()
    if len(text) > 40 and ' ' in text and not re.search(r'[{}<>\\]', text):
        if re.search(r'[a-z]{3}', text):
            print(text)
