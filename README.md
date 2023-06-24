# UrlShort

UrlShort est un simple raccourcisseur d'URL écrit en python. Il est écrit à l'aide du module flask. Vous pouvez facilement utiliser UrlShort comme modèle pour créer votre propre raccourcisseur d'URL en le déployant sur heroku. UrlShort est open source, vous êtes libre de l'utiliser comme vous le souhaitez. Si vous le souhaitez, vous pouvez cloner le référentiel github et le déployer directement. Tout ce que vous avez à faire est, dans le fichier details.txt, de changer le nom de l'application en votre domaine. UrlShort n'utilise aucun autre module externe à l'exception de flask. UrlShort génère une chaîne de caractères aléatoire à 8 chiffres et stocke la relation et s'il doit raccourcir la même URL, il renvoie la même chaîne.

J'ai écrit UrlShort pour pratiquer le développement web avec flask. Il s'agit d'un projet débutant. Vous pouvez parcourir le code sur github. Si vous voulez votre propre instance, clonez le référentiel et initialisez à l'aide de heroku

# API

L'API est assez simple et facile à utiliser. Il vous suffit de faire une demande à <https://noob-short.herokuapp.com/api/v1/'url>'. Vous obtiendrez un json avec 3 paramètres : original_url, short_url, time_created. Utilisez-les comme bon vous semble.


# Deploying

It is quite easy to deploy UrlShort with heroku cli. You have to have a heroku account for this though.

1. Clone the Github Repository  

`git clone https://github.com/newtoallofthis123/UrlShort.git`

2. login to heroku cli

`heroku login`

3. Create a new heroku app

`heroku create "app-name"`

4. Initialize Git and Add

`git init
git add .`

5. Commit and Push

`git commit -m "Commit Message"
git push`

6. Wait for Heroku to build and Done.

## Hope You Enjoy UrlShort

# Future

I am still learning flask and in the future, I hope to make UrlShort better

- Add Url Alias [-]
- Add a REST API [-]
- Make Backend Faster
- Improve the UI

Merci d'avoir utiliser UrlShort
Un Projet de akonkwaushindi

> akonkwaushindi
