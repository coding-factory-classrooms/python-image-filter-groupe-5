from _datetime import datetime
import sys

args = sys.argv

log_file = "image.log"


# Enregistre les logs dans le fichier avec la date et l'heure
def log(Message):
    f"""
    Enregistrer un message dans un fichier log {log_file} et affiche le message en console
    :param Message: Le message ajouté dans le fichier log
    """
    now = datetime.now()
    timetamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timetamp} - {Message}'
    with open(log_file, "a") as f:
        f.write(str(formatted + "\n"))


# Lis le fichier
def dump_log():
    try:
        with open(log_file, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError as e:
        print(f"Fichier {log_file} impossible à ouvrir. Error={e} ")
