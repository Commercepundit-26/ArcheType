import re
with open('prevail_text_utf8.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract jsx children strings
matches = re.findall(r'children:\s*(["\'])(.*?)\1', content)
for _, text in matches:
    if len(text) > 10:
        print(text)
        
# Extract template literals
matches2 = re.findall(r'children:\s*`([^`]*)`', content)
for text in matches2:
    if len(text) > 10:
        print(text)
