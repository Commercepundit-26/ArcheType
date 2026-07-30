import re

with open('V4.html', 'r') as f:
    content = f.read()

# Update image src to point to optimized assets
content = re.sub(r'src="assets/([^"]+\.(?:jpg|png|jpeg))"', r'src="assets/opt/\1"', content)
content = re.sub(r"background-image: url\('assets/([^']+\.(?:jpg|png|jpeg))'\)", r"background-image: url('assets/opt/\1')", content)

with open('V4.html', 'w') as f:
    f.write(content)
