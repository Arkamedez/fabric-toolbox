import json
import os

file_path = 'CS_Wholesale_Theme.json'
with open(file_path, 'r', encoding='utf-8') as f:
    theme = json.load(f)

# 1. Add "fill" to "shape" > "*"
if "visualStyles" in theme and "shape" in theme["visualStyles"] and "*" in theme["visualStyles"]["shape"]:
    shape_card = theme["visualStyles"]["shape"]["*"]
    shape_card["fill"] = [
        {
            "show": True,
            "fillColor": { "solid": { "color": "#1282C6" } }
        }
    ]

# 2. Find and replace all #1E9FD3 with #1282C6 EXCEPT inside dataColors
def replace_color(obj, parent_key=None):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'color' and isinstance(v, str) and v.upper() == '#1E9FD3' and parent_key != 'dataColors':
                obj[k] = '#1282C6'
            elif k == 'good' and getattr(obj, k, "") == '#1E9FD3':
                pass # not an object, but a direct string in root
            elif isinstance(v, (dict, list)):
                replace_color(v, k)
    elif isinstance(obj, list):
        # We don't want to replace inside the direct dataColors string list
        if parent_key != 'dataColors':
            for item in obj:
                replace_color(item, parent_key)

# Specifically for the root properties 'good' and 'neutral'
if theme.get('good', '').upper() == '#1E9FD3':
    theme['good'] = '#1282C6'
if theme.get('neutral', '').upper() == '#1E9FD3':
    theme['neutral'] = '#1282C6'

# Traverse the rest
replace_color(theme)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(theme, f, indent=2)

print("Successfully injected shape fills and replaced headers/titles to #1282C6")
