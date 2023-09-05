import os
import git
from datetime import datetime

# Chemin du répertoire racine contenant les dossiers Git
racine = './'

# Parcours des dossiers dans le répertoire racine
for dossier in os.listdir(racine):
    chemin_dossier = os.path.join(racine, dossier)

    # Vérifier si le chemin est un dossier
    if os.path.isdir(chemin_dossier):
        try:
            repo = git.Repo(chemin_dossier)
            dernier_commit = repo.head.commit
            date_commit = dernier_commit.committed_date
            message_commit = dernier_commit.message

            # Formater la date au format JJ/MM/AAAA
            date_formattee = datetime.utcfromtimestamp(date_commit).strftime('%d/%m/%Y')

            # Afficher les informations du dernier commit avec la date formatée
            print(f'Dossier : {dossier}')
            print(f'Date du dernier commit : {date_formattee}\n')
            # print(f'Message du dernier commit : {message_commit}\n')

        except git.exc.InvalidGitRepositoryError:
            print(f'Le dossier {dossier} n\'est pas un dépôt Git.')
