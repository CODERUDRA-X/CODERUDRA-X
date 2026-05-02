import datetime
import re

# 1. TIMING & DATA
now = datetime.datetime.now()
day_of_year = now.timetuple().tm_yday

# 2. THE 20 SACRED PROTOCOLS
gita_protocols = [
    {"hook": "Focus on the Logic, not the Green Box.", "verse": "Karma-any-evadhika-raste ma phaleshu kadachana...", "interpretation": "You have a right to perform your prescribed duties (Logic), but you are not entitled to the fruits (Green Squares) of your actions."},
    {"hook": "One-Pointed Intelligence (The Focus).", "verse": "Vyavasayatmika buddhir ekeha kuru-nandana...", "interpretation": "Concentrate on one complex architecture at a time. A fragmented mind creates buggy code; a unified mind builds the future."},
    {"hook": "Precision is the Ultimate Yoga.", "verse": "Yoga karmasu kaushalam...", "interpretation": "Excellence in your logic is a spiritual practice. In Defense-AI, precision is the divine difference between success and failure."},
    {"hook": "Action in Inaction: The Stealth Bot.", "verse": "Karmanyakarma yah pashyed akarmani cha karma yah...", "interpretation": "Seeing action in inaction—like a bot working silently while the developer rests. True intelligence is efficient and persistent."},
    {"hook": "Uplift your System by your Own Effort.", "verse": "Uddhared atmanatmanam natmanam avasadayet...", "interpretation": "You are your own Root Access. Elevate your status through your own hard-coded will. Never let your inner system crash."},
    {"hook": "Knowledge is the Supreme Weapon.", "verse": "Nahi jnanena sadrisham pavitram iha vidyate...", "interpretation": "Verily, there is nothing as pure as knowledge. Master the underlying architecture to master the machine. AI is the tool, you are the Key."},
    {"hook": "Be Steady Amidst the Runtime Errors.", "verse": "Siddhy-asiddhyoh samo bhutva samatvam yoga uchyate...", "interpretation": "Stay equanimous in success (compilation) and failure (bugs). Balance is the true system status. A steady pulse builds stable systems."},
    {"hook": "The Mind is like a Restless Bug.", "verse": "Chanchalam hi manah krishna pramathi balavad dridham...", "interpretation": "The mind is turbulent like an unoptimized loop. Through constant practice (debugging), it can be tamed and redirected."},
    {"hook": "Follow your Svadharma (Your Own Path).", "verse": "Sreyan sva-dharmo vigunah para-dharmat svanusthitat...", "interpretation": "Build your own Defense-AI path, even if imperfect, rather than following a perfect path that isn't yours. Authenticity is the best encryption."},
    {"hook": "The Fire of Knowledge Burns Errors.", "verse": "Jnanagnih sarva-karmani bhasma-sat kurute tatha...", "interpretation": "The fire of true understanding burns all past misconceptions and coding errors into ashes. Learn the 'Why' and the 'How' will fix itself."},
    {"hook": "Clarity is the Best IDE.", "verse": "Tatra tam buddhi-samyogam labhate paurva-dehikam...", "interpretation": "When clarity of thought is achieved, the logic flows without the need for external tools. Your mind is the most powerful processor."},
    {"hook": "Endure the Heat of the Deadline.", "verse": "Matra-sparshas tu kaunteya shitosna-sukha-duhkha-dah...", "interpretation": "Deadlines and bugs are like seasons; they come and go. Endure them with a steady pulse and unwavering focus on the deployment."},
    {"hook": "Seeing the Unified Swarm in All.", "verse": "Vidya-vinaya-sampanne brahmane gavi hastini...", "interpretation": "A master sees the same underlying logic in a single line of code and a massive neural network. Everything is connected through source code."},
    {"hook": "The Lotus Leaf Logic (Pure Execution).", "verse": "Brahmany adhaya karmani sangam tyaktva karoti yah...", "interpretation": "Work without attachment, like water on a lotus leaf. Let bugs touch your code, but never let them touch your spirit."},
    {"hook": "Steady Engagement leads to Victory.", "verse": "Yatra yogeshwarah krishno yatra partho dhanur-dharah...", "interpretation": "Where there is Vision and Execution, victory is certain. Combine your data science with action to build the future."},
    {"hook": "The Silence of Deep Work.", "verse": "Maunam chaivasti guhyanam jnanam jnanavatam aham...", "interpretation": "Silence is the secret of deep architecture. In the quietest mind, the most complex and elegant logic is compiled and born."},
    {"hook": "Determination of the S-Rank Builder.", "verse": "Dhritua yaya dharayate manah-pranendriya-kriyah...", "interpretation": "Through unwavering determination, control the mind, the life-force, and the keyboard towards one singular goal: The Mission."},
    {"hook": "Every Project has its own Smoke (Bugs).", "verse": "Saha-jam karma kaunteya sa-dosam api na tyajet...", "interpretation": "Every undertaking is clouded by defects, as fire is by smoke. Accept the bugs as part of the process, but never stop developing."},
    {"hook": "Master the Self, Master the Environment.", "verse": "Jitamanah prashantashya paramatma samahitah...", "interpretation": "For one who has conquered the mind, the heat of the deadline and the cold of failure are the same. You remain the Master of the Mainframe."},
    {"hook": "Sacrifice of Knowledge (Open Source).", "verse": "Sreyan dravya-mayaj jnanat jnana-yajnah parantapa...", "interpretation": "The sacrifice of sharing knowledge (Open Source) is higher than mere accumulation of private code. To teach is to master."}
]

protocol_index = day_of_year % len(gita_protocols)
p = gita_protocols[protocol_index]

# 3. GENERATE SVG
svg_code = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" rx="10" fill="#0d1117"/>
  <rect x="10" y="10" width="780" height="380" rx="8" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="6 6"/>
  <text x="50%" y="70" text-anchor="middle" fill="#D4AF37" font-family="Georgia, serif" font-size="28" font-weight="bold" letter-spacing="3">THE DHARMA OF ACTION</text>
  <text x="50%" y="140" text-anchor="middle" fill="#F5F5DC" font-family="Georgia, serif" font-size="22" font-style="italic">"{p['verse']}"</text>
  <line x1="250" y1="190" x2="550" y2="190" stroke="#D4AF37" stroke-width="0.5"/>
  <text x="50%" y="240" text-anchor="middle" fill="#D4AF37" font-family="Verdana, sans-serif" font-size="16" font-weight="bold" letter-spacing="1">PROTOCOL {protocol_index+1:02d} // {p['hook'].upper()}</text>
  <foreignObject x="80" y="270" width="640" height="120">
    <div xmlns="http://www.w3.org/1999/xhtml" style="color: #C0C0C0; font-family: Georgia, serif; font-size: 18px; text-align: center; line-height: 1.4;">
      {p['interpretation']}
    </div>
  </foreignObject>
  <text x="50%" y="380" text-anchor="middle" fill="#D4AF37" font-size="24">❈</text>
</svg>"""

with open('gita_verse.svg', 'w', encoding='utf-8') as f:
    f.write(svg_code)

# 4. UPDATE README MARKERS
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

start_m, end_m = "<!-- GITA_START -->", "<!-- GITA_END -->"
gita_block = f"{start_m}\n<div align='center'>\n  <img src='gita_verse.svg' width='100%' />\n</div>\n{end_m}"

pattern = re.compile(rf"{re.escape(start_m)}.*?{re.escape(end_m)}", re.DOTALL)
new_content = re.sub(pattern, gita_block, content) if pattern.search(content) else gita_block + "\n\n" + content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
