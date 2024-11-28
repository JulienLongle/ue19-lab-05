# UE19-lab-05

## Description

Ce script Python utilise l'API Agify pour estimer l'âge d'une personne en fonction de son prénom et de son pays
de résidence. Le programme demande à l'utilisateur d'entrer son prénom et retourne un âge estimé pour le prénom donné 
en Belgique (code pays : BE).

## Prérequis

Pour exécuter ce script, vous devez avoir Docker installé sur votre système.


## Comment l'utiliser

1. Lancez le fichier Dockerfile.
2. Construisez l'image Docker :
docker build -t app .
3. Lancez le conteneur :
docker run -it app
4. Entrez votre prénom lorsque cela est demandé.

Le programme récupérera l'âge estimé pour votre prénom et affichera le résultat.

### Exemple

#### Entrée :

What's your name ? Julien

#### Sortie :

The estimated age for Julien is 52.

## Explication du code

Saisie utilisateur : L'utilisateur est invité à entrer son prénom via la fonction input().

Requête API : Le script effectue une requête GET à l'API Agify en utilisant le prénom entré et le code pays BE (Belgique).

Analyse de la réponse : La réponse est convertie au format JSON, et le champ age est extrait.

Affichage du résultat : L'âge estimé est affiché à l'utilisateur dans une chaîne de caractères formatée.

## Référence API

Endpoint de l'API Agify : https://api.agify.io

Paramètres de la requête :

name : Le prénom pour lequel l'estimation d'âge est demandée.

country_id : Le code du pays où la popularité du prénom est considérée (dans ce cas, BE pour la Belgique).

## Licence

Ce script est destiné à des fins éducatives et est distribué sans aucune garantie.

