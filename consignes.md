# Intro

Flash back quelques années en arrière, Padam vient de lever des fonds ! Il faut maintenant transformer le prototype en une base viable pour les futurs développements. Conscient qu'il s'agit d'un MVP développé à la va vite  par des stagiaires, et de l'importance de contenir la dette technique dès le départ, le CTO accepte de retarder les fonctionnalités business et vous accorde généreusement...30 minutes.
Ce n'est bien entendu pas suffisant, et la nuit même, vous cauchemardez qu'un bus à une roue, sans volant ni chauffeur, cherche à vous écraser tandis que vous essayez de lui rajouter un minuscule boulon. Vous vous réveillez en sueur et sur les quelques heures qu'il vous reste avant de partir au travail, vous décidez de limiter les dégâts.


# Exercice :

- Pour vous faire gagner du temps, et parce que vous n'arriverez pas sur un projet vierge, nous vous fournissons un système de réservation très simplifié permettant à un client de réserver une voiture pour effectuer un trajet.
- Le code est de mauvaise qualité, et vous avez carte blanche pour l'améliorer et le rendre 'production ready'. Ce refactoring est le coeur de l'exercice.
- Listez les présupposés dans le code qui rendent impossible de s'en servir réellement. Par exemple, il n'y a pas de système de paiement...
- Bonus : corrigez ces simplifications ;-)


## A propos du code que nous vous fournissons:

### Il est censé permettre à un client de :

- s'inscrire, se connecter, se déconnecter.
- créer, voir, et supprimer des réservations.
- connaître le temps de parcours de sa réservation


# Instructions et conseils généraux :

- Un projet Django, hébergé sur Github, avec une BDD sqlite (commitée), est attendu.
- Il n'y a pas de deadline, mais idéalement le projet ne devrait pas prendre plus de 2 jours à réaliser.
- Mettre l'accent sur le back-end. Le front-end est moins important pour le poste en question.
- Ne pas hésiter à utiliser des mécanismes propres à Django si besoin (ex : signaux, override de save(), CBVs, extensions, etc.).
- Ne pas hésiter à laisser des commentaires (ou un document) pour expliquer les choix techniques (eg: expliquer les bénéfices / contraintes de telle ou telle solution)
- Certains aspects sont volontairement vagues pour vous laisser une liberté de choix.
- Si vous ne disposez que de peu de temps pour réaliser l'exercice, concentrez-vous sur la qualité plutôt que la quantité. A l'inverse, si vous avez du temps, tout bonus sera apprécié.
- Ne pas hésiter à nous poser des questions si besoin (rafik@padam.io et/ou nathan@padam.io).
