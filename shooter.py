import requests
import datetime

# 1. SETTINGS
USERNAME = "CODERUDRA-X"
# Token will be passed from GitHub Actions

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
    # SVG Dimensions and Styles
    svg = '<svg width="800" height="150" xmlns="http://www.w3.org/2000/svg" fill="none">'
    svg += '<style> .box { width: 10px; height: 10px; rx: 2; } .laser { stroke: #39d353; stroke-width: 2; visibility: hidden; } '
    svg += '.spaceship { font-size: 20px; } @keyframes move { 0% { transform: translateX(0); } 100% { transform: translateX(750px); } } '
    svg += '@keyframes fire { 0% { opacity: 1; stroke-dashoffset: 100; } 100% { opacity: 0; stroke-dashoffset: 0; } } </style>'
    
    # Background
    svg += '<rect width="800" height="150" fill="#0d1117" rx="10"/>'

    # Draw Boxes (Targets)
    for x, week in enumerate(weeks[-52:]): # Last 52 weeks
        for y, day in enumerate(week['contributionDays']):
            color = day['color'] if day['contributionCount'] > 0 else "#161b22"
            svg += f'<rect class="box" x="{x*14 + 40}" y="{y*14 + 20}" fill="{color}" />'
            
    # The Interceptor Spaceship (Animated)
    svg += '<g>'
    svg += '  <text x="0" y="140" class="spaceship">🛸</text>'
    svg += '  <animateTransform attributeName="transform" type="translate" from="0 0" to="750 0" dur="10s" repeatCount="indefinite" />'
    
    # Simple Laser Logic (Randomly firing for effect)
    for i in range(10):
        svg += f'<line x1="{i*80}" y1="130" x2="{i*80}" y2="20" class="laser" stroke-dasharray="100">'
        svg += f'<animate attributeName="visibility" from="hidden" to="visible" begin="{i}s" dur="0.1s" repeatCount="indefinite" />'
        svg += '</line>'
    svg += '</g>'

    svg += '</svg>'
    with open("contribution_shooter.svg", "w") as f:
        f.write(svg)

# Run logic
import os
token = os.getenv("GH_TOKEN")
weeks = get_contributions(token)
generate_shooter_svg(weeks)
