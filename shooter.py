import requests
import os
import datetime

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
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" fill="none">'
    
    # CSS for true Space Invaders vibe
    svg += """
    <style>
        .bg { fill: #0d1117; rx: 10; }
        .box { width: 10px; height: 10px; rx: 2; }
        .ship { font-size: 22px; }
        .laser { stroke: #39d353; stroke-width: 3; stroke-linecap: round; }
        
        @keyframes ship-move {
            0%, 100% { transform: translateX(40px); }
            50% { transform: translateX(740px); }
        }
        
        @keyframes laser-shoot {
            0% { transform: translateY(0); opacity: 1; }
            70% { opacity: 1; }
            100% { transform: translateY(-100px); opacity: 0; }
        }
        
        .ship-container {
            animation: ship-move 10s linear infinite;
        }
        
        .laser-effect {
            animation: laser-shoot 0.4s linear infinite;
        }
    </style>
    """
    
    svg += f'<rect width="{width}" height="{height}" class="bg"/>'

    # Draw Contribution Boxes (The Targets)
    for x, week in enumerate(weeks[-52:]):
        for y, day in enumerate(week['contributionDays']):
            color = day['color'] if day['contributionCount'] > 0 else "#161b22"
            svg += f'<rect class="box" x="{x*14 + 45}" y="{y*14 + 25}" fill="{color}" />'
            
    # The Spaceship + Laser (Moving Together)
    svg += '<g transform="translate(0, 135)" class="ship-container">'
    # The Laser Bolt
    svg += '  <line x1="11" y1="-10" x2="11" y2="-30" class="laser laser-effect" />'
    # The Ship Icon
    svg += '  <text x="0" y="5" class="ship">🚀</text>'
    svg += '</g>'

    svg += '</svg>'
    
    with open("contribution_shooter.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# Main Execution
token = os.getenv("GH_TOKEN")
if token:
    try:
        weeks = get_contributions(token)
        generate_shooter_svg(weeks)
        print("SVG Updated Successfully!")
    except Exception as e:
        print(f"Error: {e}")
