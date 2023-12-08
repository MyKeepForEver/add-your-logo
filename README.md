# KeepForEver - Intégration Logo Open Source

## Bienvenue sur le Dépôt KeepForEver 🚀

Ce projet open source invite les entreprises à intégrer leurs logos de manière transparente dans la plateforme KeepForEver. En contribuant avec votre logo, vous améliorez l'attrait visuel et la personnalisation de l'expérience de legs numérique.

## Comment contribuer

1. **Faites un Fork du Dépôt 🍴** Commencez par faire un fork de ce dépôt vers votre compte.
2. **Ajoutez Votre Logo 🖼️** Localisez le répertoire `services/logo` et téléversez votre logo d'entreprise en utilisant le format recommandé (PNG, JPG, SVG ou WebP). Assurez-vous que le nom de fichier est en minuscules et correspond au nom de votre entreprise.
3. **Mettez à Jour services.json 📝** Exécutez le script `main.py` pour mettre à jour automatiquement l'index. Cela inclut votre logo dans l'index [service.json](https://github.com/MyKeepForEver/add-your-logo/blob/main/service.json) de KeepForEver.
4. **Soumettez une Pull Request 🚢** Une fois que vous avez ajouté votre logo, soumettez une pull request. Nous le réviserons rapidement et, une fois approuvée, votre logo fera partie intégrante de la collection de logos de KeepForEver.

## Structure de services.json

```json
{
  "s": {
    "service1": {
      "p": "svg"
    },
    "service2": {
      "p": "png"
    },
    "service3": {
      "p": "webp"
    },
    "service4": {
      "p": "jpg"
    }
}
```

## Notes Importantes

- Assurez-vous que votre logo respecte nos directives de qualité et de taille.
- Nous apprécions votre contribution à la communauté KeepForEver ! 🌐

Merci de faire partie de l'héritage KeepForEver ! Si vous avez des questions ou avez besoin d'aide, n'hésitez pas à nous contacter.
