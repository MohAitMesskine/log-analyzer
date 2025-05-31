#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def analyser_log(fichier_log: str):
    """
    Lit le fichier de log donné et compte le nombre de lignes contenant
    ERROR, WARNING et INFO. Renvoie un dictionnaire avec ces compteurs.
    """
    compteurs = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    try:
        with open(fichier_log, "r", encoding="utf-8") as f:
            for ligne in f:
                # On cherche les mots-clés en majuscules dans la ligne
                if "ERROR" in ligne:
                    compteurs["ERROR"] += 1
                if "WARNING" in ligne:
                    compteurs["WARNING"] += 1
                if "INFO" in ligne:
                    compteurs["INFO"] += 1
    except FileNotFoundError:
        print(f"Le fichier {fichier_log} n'existe pas.", file=sys.stderr)
        sys.exit(2)

    return compteurs

def ecrire_rapport(compteurs: dict, fichier_rapport: str):
    """
    Génère un rapport dans le fichier spécifié.
    """
    try:
        with open(fichier_rapport, "w", encoding="utf-8") as f:
            f.write("=== Rapport d'analyse des logs ===\n")
            f.write(f"Nombre de lignes ERROR   : {compteurs['ERROR']}\n")
            f.write(f"Nombre de lignes WARNING : {compteurs['WARNING']}\n")
            f.write(f"Nombre de lignes INFO    : {compteurs['INFO']}\n")
        print(f"Rapport généré dans {fichier_rapport}")
    except Exception as e:
        print(f"Erreur lors de l'écriture du rapport : {e}", file=sys.stderr)
        sys.exit(3)

def main():
    """
    Point d'entrée du script. Usage : python log_analyzer.py [chemin_vers_log.txt]
    """
    # Si aucun argument, on suppose que le fichier s'appelle log.txt dans le dossier courant
    if len(sys.argv) >= 2:
        fichier_log = sys.argv[1]
    else:
        fichier_log = "log.txt"

    if not os.path.isfile(fichier_log):
        print(f"Le fichier de log spécifié ({fichier_log}) n'existe pas.", file=sys.stderr)
        sys.exit(1)

    compteurs = analyser_log(fichier_log)
    ecrire_rapport(compteurs, "rapport.txt")
    # On pourra éventuellement afficher aussi les stats à l’écran :
    print("=== Statistiques (affichage console) ===")
    print(f"ERROR   : {compteurs['ERROR']}")
    print(f"WARNING : {compteurs['WARNING']}")
    print(f"INFO    : {compteurs['INFO']}")

if __name__ == "__main__":
    main()
