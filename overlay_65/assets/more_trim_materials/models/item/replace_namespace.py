from pathlib import Path

count = 0

for file in Path(".").rglob("*.json"):
    content = file.read_text(encoding="utf-8")

    # Modifie uniquement la ligne layer0
    new_content = content.replace(
        '"layer0": "minecraft:item/',
        '"layer0": "more_trim_materials:item/',
        1
    )

    if content != new_content:
        file.write_text(new_content, encoding="utf-8")
        print(f"Modifié : {file}")
        count += 1

print(f"\n{count} fichier(s) modifié(s).")