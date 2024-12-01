# UE19-lab-05

## Description

Ce script Python utilise l'API Agify pour estimer l'âge d'une personne en fonction de son prénom et de son pays
de résidence. Le programme demande à l'utilisateur d'entrer son prénom et retourne un âge estimé pour le prénom donné 
en Belgique (code pays : BE).

## Prérequis

Pour exécuter ce script, vous devez avoir Docker installé sur votre système.


## Comment l'utiliser

1. Construisez l'image Docker :
docker build -t app .
2. Lancez le conteneur :
docker run -it app
3. Entrez votre prénom lorsque cela est demandé.

Le programme récupérera l'âge estimé pour votre prénom et affichera le résultat.

### Exemple

#### Entrée :

What's your name ? Julien

#### Sortie :

The estimated age for Julien is 52.

## Référence API

Endpoint de l'API Agify : https://api.agify.io

Paramètres de la requête :

name : Le prénom pour lequel l'estimation d'âge est demandée.

country_id : Le code du pays où la popularité du prénom est considérée (dans ce cas, BE pour la Belgique).
