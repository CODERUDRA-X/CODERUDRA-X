import requests
import os

USERNAME = "CODERUDRA-X"

def get_contributions(token):
    query = """
    query($userName:String!) {
      user(login: $userName) {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                contributionCount
                color
              }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("https://api.github.com/graphql", json={'query': query, 'variables': {'userName': USERNAME}}, headers=headers)
    return response.json()['data']['user']['contributionsCollection']['contributionCalendar']['weeks']

def generate_shooter_svg(weeks):
    width, height = 820, 160
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#0d1117" rx="10"/>'

    # Draw Boxes (Targets)
    for x, week in enumerate(weeks[-52:]):
        for y, day in enumerate(week['contributionDays']):
            color = day['color'] if day['contributionCount'] > 0 else "#161b22"
            svg += f'<rect x="{x*14 + 45}" y="{y*14 + 25}" width="10" height="10" rx="2" fill="{color}">'
            # Blast/Flicker Effect: Boxes will slightly glow/flicker randomly
            if day['contributionCount'] > 0:
                svg += f'<animate attributeName="opacity" values="1;0.5;1" dur="{0.5 + (x%3)*0.2}s" repeatCount="indefinite" />'
            svg += '</rect>'

    # Moving Group (Ship + Laser + Impact)
    svg += '<g>'
    svg += '<animateTransform attributeName="transform" type="translate" values="40,135; 740,135; 40,135" dur="8s" repeatCount="indefinite"/>'
    
    # 1. Real Shooting Laser
    svg += '<rect x="14" y="-10" width="2" height="20" fill="#39d353">'
    svg += '<animate attributeName="y" from="-10" to="-120" dur="0.3s" repeatCount="indefinite"/>'
    svg += '<animate attributeName="opacity" values="1;1;0" keyTimes="0;0.7;1" dur="0.3s" repeatCount="indefinite"/>'
    svg += '</rect>'

    # 2. Impact Blast (Star shape at the top of the laser path)
    svg += '<path d="M15,-110 L17,-105 L22,-105 L18,-102 L20,-97 L15,-100 L10,-97 L12,-102 L8,-105 L13,-105 Z" fill="#ffcc00">'
    svg += '<animate attributeName="opacity" values="0;1;0" dur="0.3s" repeatCount="indefinite"/>'
    svg += '<animate attributeName="transform" attributeType="XML" type="scale" values="0.5;1.5;0.5" dur="0.3s" repeatCount="indefinite" additive="sum"/>'
    svg += '</path>'

    # 3. Sleek Defense-AI Spaceship
    svg += '<path d="M15,-20 L0,5 L5,10 L15,5 L25,10 L30,5 Z" fill="#58a6ff" stroke="#fff" stroke-width="0.5"/>'
    svg += '<rect x="12" y="-2" width="6" height="4" fill="#39d353" rx="1"/>' # Cockpit
    svg += '</g>'
    
    svg += '</svg>'
    
    with open("contribution_shooter.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# Main logic
token = os.getenv("GH_TOKEN")
if token:
    generate_shooter_svg(get_contributions(token))
