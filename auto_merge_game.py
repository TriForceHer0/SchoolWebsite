# auto_merge_game.py

import re
import os

# Filenames
game_file = "game.html"
index_file = "index.html"

# Read the game.html content
with open(game_file, "r", encoding="utf-8") as f:
    game_content = f.read()

# Extract head content
head_match = re.search(r"<head.*?>(.*?)</head>", game_content, flags=re.IGNORECASE | re.DOTALL)
head_content = head_match.group(1).strip() if head_match else ""

# Extract body content
body_match = re.search(r"<body.*?>(.*?)</body>", game_content, flags=re.IGNORECASE | re.DOTALL)
body_content = body_match.group(1).strip() if body_match else ""

# Prepare the new index.html template
index_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Game</title>

    <!-- ===== Merged game.html head content ===== -->
    {head_content}
    <!-- ===== End of game head ===== -->
</head>
<body>
    <!-- ===== Merged game.html body content ===== -->
    {body_content}
    <!-- ===== End of game body ===== -->
</body>
</html>
"""

# Write the new index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_template)

print(f"Successfully merged {game_file} into {index_file}!")
