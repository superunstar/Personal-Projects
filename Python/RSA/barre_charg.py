import time
import sys

# Fonction pour afficher une barre de chargement
def afficher_barre_de_chargement(duration):
    # Temps écoulé en secondes
    elapsed_time = 0
    # Caractères pour l'animation de la barre de chargement
    animation = "|/-\\"
    idx = 0

    while elapsed_time < duration:
        # Calcul du pourcentage de complétion
        percent = (elapsed_time / duration) * 100

        # Affichage de la barre de chargement
        sys.stdout.write("\r[{}] {:.2f}%".format(animation[idx % len(animation)], percent))
        sys.stdout.flush()

        # Mise à jour de l'indice pour l'animation
        idx += 1

        # Attente d'une petite durée pour simuler le chargement
        time.sleep(0.1)

        # Mise à jour du temps écoulé
        elapsed_time += 0.1

    # Affichage de la barre de chargement à 100% une fois terminée
    sys.stdout.write("\r[{}] 100.00%\n".format(animation[idx % len(animation)]))

# Durée totale de la barre de chargement en secondes
duree_barre_chargement = 1

# Appel de la fonction pour afficher la barre de chargement
afficher_barre_de_chargement(duree_barre_chargement)
