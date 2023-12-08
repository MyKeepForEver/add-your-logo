import os

# Chemin vers le répertoire des logos
logo_directory = 'services/logo'

# Liste des fichiers dans le répertoire
logo_files = [f for f in os.listdir(logo_directory) if os.path.isfile(os.path.join(logo_directory, f))]

# Ouverture du fichier README en mode append
with open('README.md', 'a') as readme_file:
    # Ajout de la section des logos sous forme de tableau
    readme_file.write("\n\n---\n\n")
    readme_file.write("\n## Services déjà intégrés\n\n")
    readme_file.write("| Service 1 | Service 2 | Service 3 | Service 4 | Service 5 |" + "\n")
    readme_file.write("| --- " * 5 + "|" "\n")
    
    for i in range(0, len(logo_files), 5):
        # Construction des balises Markdown pour les logos dans la ligne
        logos_in_row = [
            f'<img src="{os.path.join(logo_directory, logo_file)}" alt="{os.path.splitext(logo_file)[0]}" style="width: 56px; height: 56px; border-radius: 12px;" />'
            for logo_file in logo_files[i:i+5]
        ]
        
        # Ajout de la ligne dans le tableau
        readme_file.write("| " + " | ".join(logos_in_row) + " |\n")

# Ouverture du fichier README en mode append
with open('README-en.md', 'a') as readme_file:
    # Ajout de la section des logos sous forme de tableau
    readme_file.write("\n\n---\n\n")
    readme_file.write("\n## Services already integrated\n\n")
    readme_file.write("| Service 1 | Service 2 | Service 3 | Service 4 | Service 5 |" + "\n")
    readme_file.write("| --- " * 5 + "|" "\n")
    
    for i in range(0, len(logo_files), 5):
        # Construction des balises Markdown pour les logos dans la ligne
        logos_in_row = [
            f'<img src="{os.path.join(logo_directory, logo_file)}" alt="{os.path.splitext(logo_file)[0]}" style="width: 56px; height: 56px; border-radius: 12px;" />'
            for logo_file in logo_files[i:i+5]
        ]
        
        # Ajout de la ligne dans le tableau
        readme_file.write("| " + " | ".join(logos_in_row) + " |\n")