import os
import json

# Chemin vers votre dossier de recettes générées
# (Ajustez le chemin si le script n'est pas dans le même dossier que "generated_recipes")
RECIPES_DIR = os.path.join(os.path.dirname(__file__), '')

def convert_recipe_file(file_path):
    try:
        # 1. Lire le fichier JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            recipe = json.load(f)
        
        # 2. Effectuer les simplifications de structure si les clés existent sous forme de dictionnaire
        keys_to_simplify = ['base', 'addition', 'template']
        modified = False
        
        for key in keys_to_simplify:
            if key in recipe and isinstance(recipe[key], dict) and 'item' in recipe[key]:
                recipe[key] = recipe[key]['item']
                modified = True
                
        # 3. Réécrire le fichier uniquement s'il y a eu des modifications
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(recipe, f, indent=2, ensure_ascii=False)
            return True
            
    except Exception as e:
        print(f"Erreur lors du traitement de {os.path.basename(file_path)} : {e}")
    return False

def main():
    if not os.path.exists(RECIPES_DIR):
        print(f"Erreur : Le dossier {RECIPES_DIR} n'existe pas.")
        return

    print(f"Début de la conversion dans : {RECIPES_DIR}")
    converted_count = 0
    total_files = 0

    for root, _, files in os.walk(RECIPES_DIR):
        for file in files:
            if file.endswith('.json'):
                total_files += 1
                file_path = os.path.join(root, file)
                if convert_recipe_file(file_path):
                    converted_count += 1

    print(f"Conversion terminée ! {converted_count}/{total_files} fichiers JSON ont été simplifiés.")

if __name__ == "__main__":
    main()