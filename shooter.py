import requests
import os

USERNAME = "CODERUDRA-X"

def get_contributions(token):
    # Fetch GitHub graph data
    # Query for last 52 weeks
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
    # SVG canvas setup
    width, height = 820, 160
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#0d1117" rx="10"/>'

    # Draw grid
    for x, week in enumerate(weeks[-52:]):
        for y, day in enumerate(week['contributionDays']):
            color = day['color'] if day['contributionCount'] > 0 else "#161b22"
            svg += f'<rect x="{x*14 + 45}" y="{y*14 + 25}" width="10" height="10" rx="2" fill="{color}" />'

    # Ship and laser group
    # Using SMIL animations for GitHub compatibility
    svg += '<g>'
    svg += '<animateTransform attributeName="transform" type="translate" values="40,135; 740,135; 40,135" dur="10s" repeatCount="indefinite"/>'
    
    # Animated Laser
    svg += '<rect x="14" y="-10" width="2" height="15" fill="#39d353">'
    svg += '<animate attributeName="y" from="-10" to="-130" dur="0.4s" repeatCount="indefinite"/>'
    svg += '<animate attributeName="opacity" values="1; 1; 0" keyTimes="0; 0.8; 1" dur="0.4s" repeatCount="indefinite"/>'
    svg += '</rect>'

    # Drawn Spaceship (No emoji)
    svg += '<path d="M15,-15 L0,10 L15,5 L30,10 Z" fill="#58a6ff"/>'
    svg += '</g>'
    svg += '</svg>'
    
    with open("contribution_shooter.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# Execute script
token = os.getenv("GH_TOKEN")
if token:
    generate_shooter_svg(get_contributions(token))
