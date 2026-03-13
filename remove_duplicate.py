# Remove duplicate block: lines 1178-1299 (0-indexed: 1177-1298)
path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
# Keep lines 1-1176 (index 0-1176) and from 1300 onward (index 1299)
new_lines = lines[:1177] + lines[1299:]
with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Removed lines 1178-1299 (duplicate Organización block).")
