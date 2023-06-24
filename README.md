# UrlShort

UrlShort est un simple raccourcisseur d'URL écrit en python. Il est écrit à l'aide du module flask. Vous pouvez facilement utiliser UrlShort comme modèle pour créer votre propre raccourcisseur d'URL en le déployant sur heroku. UrlShort est open source, vous êtes libre de l'utiliser comme vous le souhaitez. Si vous le souhaitez, vous pouvez cloner le référentiel github et le déployer directement. Tout ce que vous avez à faire est, dans le fichier details.txt, de changer le nom de l'application en votre domaine. UrlShort n'utilise aucun autre module externe à l'exception de flask. UrlShort génère une chaîne de caractères aléatoire à 8 chiffres et stocke la relation et s'il doit raccourcir la même URL, il renvoie la même chaîne.

J'ai écrit UrlShort pour pratiquer le développement web avec flask. Il s'agit d'un projet débutant. Vous pouvez parcourir le code sur github. Si vous voulez votre propre instance, clonez le référentiel et initialisez à l'aide de heroku

# API

L'API est assez simple et facile à utiliser. Il vous suffit de faire une demande à <https://url-short.herokuapp.com/api/v1/'url>'. Vous obtiendrez un json avec 3 paramètres : original_url, short_url, time_created. Utilisez-les comme bon vous semble.

# Hébergement

C'est facile de héberger UrlShort avec le serviceheroku cli. Il ne vous suffit que d'avoir un compte heroku pour le faire.

1. Clonez le repo sur Github  

`git clone https://github.com/Akon2020/UrlShort.git`

2. Connection à heroku cli

`heroku login`

3. Creation d'une nouvelle application heroku

`heroku create "app-name"`

4. Initialisation et ajout à Git

`git init
git add .`

5. Le Commit et Le Push

`git commit -m "Message du commit"
git push`

6. Patientez qu'Heroku finisse le build et votre application sera prête.

## Hope You Enjoy UrlShort

# Future

J'apprends encore flask et compte continuer pour rendre UrlShort encore mieux

- Ajouter un alias d'url [-]
- Ajouter un REST API [-]
- Concevoir un Backend plus rapidement
- Faire mieux en UI

Merci d'avoir utiliser UrlShort
Un Projet de akonkwaushindi

> akonkwaushindi
