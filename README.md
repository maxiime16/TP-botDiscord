# TP : Développement d’un BOT avec l’API discord

## Documentation des Bots
### Bot 1 :

Ce bot répond aux commandes et réagit à certains messages sur le serveur Discord où il est connecté.
Il propose les fonctionnalités suivantes :

Commande !ping : Répond avec "pong 🏓".

Commande !touché : Répond avec "coulé ! 💥".

Commande !members : Envoie la liste des membres du serveur avec leurs pseudonymes et leurs rôles.

Réaction aux messages : Réagit avec un emoji de salutation 👋 lorsque quelqu'un écrit "bonjour".

Commande !joke : Envoie une blague aléatoire.

Commande !welcome : Envoie un message de bienvenue pré-défini lorsqu'un nouvel utilisateur rejoint le serveur.

Commande !parle : Envoie un message "Ça va être tout noir".

Fonctionnalité de bannissement : Bannit automatiquement un utilisateur qui utilise le mot spécifique "negro".


### Bot 2 :

Ce bot réagit à certains messages sur le serveur Discord où il est connecté.
Il propose les fonctionnalités suivantes :

Réaction aux messages :Réagit avec
- "ping 🏓" lorsque le message "pong 🏓" est détecté 
- "TA GUEULE !!" lorsque le message "Ça va être tout noir !" est détecté.

## Comment ils ont été configuré :

Les deux bots utilisent le préfixe "!" pour reconnaître les commandes.

Tous les intents sont activés pour permettre aux bots de fonctionner correctement.

Commande !help : Affiche toutes les commandes disponibles.
