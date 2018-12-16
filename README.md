# RDV-Pref-Bob
Recevez un mail dès que la prise de RDV à la préfecture de Bobigny (en ligne) est disponible.

## Problème

Pour obtenir un rendez-vous à la préfecture de Bobigny il est nécessaire de s'inscrire sur un formulaire en ligne ([ici](http://www.seine-saint-denis.gouv.fr/booking/create/9829/0)), qui n'est acccessible que de manière aléatoire et pour de courte durée chaque jour. L'exercice de ses droits devient donc une lotterie.

## Solution

Un script python qui vérifie, toutes les 60 sec., si le formulaire d'inscription est disponible. Si c'est le cas un mail vous est envoyé, depuis votre adresse Gmail vers cette adresse. Un compte Gmail est donc obligatoire.

Lancez l'application et passez à autre chose.

## Utilisation

Pour autoriser l'application à se connecter à votre compte Gmail vous devez d'abord effectuer les simples opérations suivantes:

1. Autoriser les applications moins sécurisées à accéder à votre compte : [sur cette page](https://support.google.com/accounts/answer/6010255);
2. Si vous avez autorisé l'authentification à 2 facteurs (recommandé) vous devez générer un mot de passe spécifique à l'application : [sur cette page](https://security.google.com/settings/security/apppasswords). Notez ce mot de passe quelque part : à chaque fois que vous lancerez l'application

Quand vous lancez le programme, le mot de passe qui vous est demandé sera celui qui est soit votre mot de passe principal, soit le mot de passe spécifique.
