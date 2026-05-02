import datetime
import re

# 1. TIMING & DATA
now = datetime.datetime.now()
day_of_year = now.timetuple().tm_yday

gita_protocols = [
    # ... (Aapki puri 20 protocols ki list yahan copy-paste karein) ...
]

protocol_index = day_of_year % len(gita_protocols)
p = gita_protocols[protocol_index]

# 2. GENERATE SVG
svg_code = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" rx="10" fill="#0d1117"/>
  <rect x="10" y="10" width="780" height="380" rx="8" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="6 6"/>
  <text x="50%" y="70" text-anchor="middle" fill="#D4AF37" font-family="Georgia, serif" font-size="28" font-weight="bold" letter-spacing="3">THE DHARMA OF ACTION</text>
  <text x="50%" y="140" text-anchor="middle" fill="#F5F5DC" font-family="Georgia, serif" font-size="22" font-style="italic">"{p['verse']}"</text>
  <line x1="250" y1="190" x2="550" y2="190" stroke="#D4AF37" stroke-width="0.5"/>
  <text x="50%" y="240" text-anchor="middle" fill="#D4AF37" font-family="Verdana, sans-serif" font-size="16" font-weight="bold" letter-spacing="1">PROTOCOL {protocol_index+1:02d} // {p['hook'].upper()}</text>
  <foreignObject x="80" y="270" width="640" height="100">
    <div xmlns="http://www.w3.org/1999/xhtml" style="color: #C0C0C0; font-family: Georgia, serif; font-size: 18px; text-align: center; line-height: 1.5;">
      {p['interpretation']}
    </div>
  </foreignObject>
  <text x="50%" y="370" text-anchor="middle" fill="#D4AF37" font-size="24">❈</text>
</svg>"""

with open('gita_verse.svg', 'w', encoding='utf-8') as f:
    f.write(svg_code)

# 3. UPDATE README MARKERS
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "<!-- GITA_START -->"
end_marker = "<!-- GITA_END -->"
gita_block = f"{start_marker}\n<div align='center'>\n  <img src='gita_verse.svg' width='100%' />\n</div>\n{end_marker}"

pattern = re.compile(rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
content = re.sub(pattern, gita_block, content) if pattern.search(content) else gita_block + "\n\n" + content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
