import os, json

#afficher le nombre total de services
def lookup():
	count = 0
	for path in os.listdir("services/logo"):
		if os.path.isfile(os.path.join("services/logo", path)):
			count += 1
	print(f"Services indexés: {count}")

#générer l'index au format json
def json_file(dossier_logo="services/logo", fichier_sortie="services.json"):
    structure_json = {"s": {}}
    for fichier in os.listdir(dossier_logo):
        nom_service, extension = os.path.splitext(fichier)
        structure_json["s"][nom_service] = {"p": extension[1:]}
    json_final = {"s": {"default": {"p": "svg"}}}
    json_final["s"].update(structure_json["s"])
    json_string = json.dumps(json_final, indent=2)
    print(json_string)
    with open(fichier_sortie, "w") as fichier_json:
        fichier_json.write(json_string)

if __name__ == "__main__":
	lookup()
	json_file()