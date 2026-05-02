import requests
import os

USERNAME = "CODERUDRA-X"

def get_contributions(token):
    query = """
    query($userName:String!) {
      user(login: $userName) {
        contributionsCollection {
          contributionCalendar {
            weeks { contributionDays { contributionCount color } }
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
    total_dur = 10 
    sweep_dur = 8  
    laser_speed = 0.3 # Laser ko niche se upar jaane mein laga waqt

    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#0d1117" rx="10"/>'

    # Draw Boxes with Precision Kill Logic
    for x, week in enumerate(weeks[-52:]):
        col_hit_time = (x / 51) * sweep_dur
        
        for y, day in enumerate(week['contributionDays']):
            color = day['color'] if day['contributionCount'] > 0 else "#161b22"
            # Row delay: Niche wale boxes pehle hit honge (y=6 is bottom, y=0 is top)
            row_delay = ((6 - y) / 7) * laser_speed
            final_hit_time = col_hit_time + row_delay
            
            # Box Drawing
            svg += f'<rect x="{x*14 + 45}" y="{y*14 + 25}" width="10" height="10" rx="2" fill="{color}">'
            # Disappear precisely when laser hits
            svg += f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;{final_hit_time/total_dur};{(final_hit_time+0.05)/total_dur};0.95;1" dur="{total_dur}s" repeatCount="indefinite" />'
            svg += '</rect>'

            # Impact Effect (Chhota blast har box par)
            if day['contributionCount'] > 0:
                svg += f'<circle cx="{x*14 + 50}" cy="{y*14 + 30}" r="0" fill="#ffcc00">'
                svg += f'<animate attributeName="r" values="0;5;0" begin="{final_hit_time}s" dur="0.2s" repeatCount="indefinite" />'
                svg += f'<animate attributeName="opacity" values="0;1;0" begin="{final_hit_time}s" dur="0.2s" repeatCount="indefinite" />'
                svg += '</circle>'

    # Moving Group (Ship + Laser)
    svg += '<g>'
    svg += f'<animateTransform attributeName="transform" type="translate" values="40,135; 745,135; 745,135; 40,135" keyTimes="0;0.8;0.9;1" dur="{total_dur}s" repeatCount="indefinite"/>'
    
    # Advanced Glowing Laser
    svg += '<rect x="14" y="-10" width="3" height="15" fill="#39d353" filter="drop-shadow(0 0 2px #39d353)">'
    svg += f'<animate attributeName="y" from="-10" to="-130" dur="{laser_speed}s" repeatCount="indefinite"/>'
    svg += f'<animate attributeName="opacity" values="1;1;0" keyTimes="0;0.8;1" dur="{laser_speed}s" repeatCount="indefinite"/>'
    svg += f'<animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.8" dur="{total_dur}s" repeatCount="indefinite"/>'
    svg += '</rect>'

    # Sleek Interceptor Ship
    svg += '<path d="M15,-20 L0,5 L7,12 L15,7 L23,12 L30,5 Z" fill="#58a6ff" stroke="#ffffff" stroke-width="1"/>'
    svg += '</g>'
    svg += '</svg>'
    
    with open("contribution_shooter.svg", "w", encoding="utf-8") as f:
        f.write(svg)

token = os.getenv("GH_TOKEN")
if token:
    generate_shooter_svg(get_contributions(token))
