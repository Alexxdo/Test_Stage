# Test_Stage
Test Technique - Data engineer


Difficultés rencontrées :

L'import des données depuis Github a été relativement complexe, les extractions sont limités à un certain nombre de données par page (pagination de l'api github) en raison de performances. J'ai pu obtenir les données de chacun des contributeurs du repository Facebook/react en parcourant de manière peu orthodoxe ces différentes pages. Cependant, concernant l'historique des commits, je n'ai pas trouvé de solutions pour en récupérer la totalité.
De plus, n'ayant pas bien compris la consigne : Produire une visualisation, pour chaque nombre de contributions, la proportion des contributeurs qui ont réalisé ce nombre de contributions, je n'ai pu remplir cette tâche.

Visualisation de données :

Le fichier script.py permet la génération d'un graphique représentant l'historique des commits en monitorant les jours où moins de 2 commits ont été effectués (affichage d'une couleur différente). Ce script génère aussi un fichier csv contenant les différents contributeurs classés par nombre de contributions et en signifiant leur anonymat/bot.
