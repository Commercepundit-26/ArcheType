const fs = require('fs');
const content = fs.readFileSync('prevail_text_utf8.txt', 'utf-8');
const strings = content.match(/(["'])(?:(?=(\\?))\2.)*?\1/g) || [];
const validStrings = strings.filter(s => {
  const stripped = s.slice(1, -1);
  return stripped.length > 30 && /^[A-Z][a-z0-9 ,\.-]+$/.test(stripped) && stripped.split(' ').length > 4;
});
console.log(Array.from(new Set(validStrings)).join('\n'));
