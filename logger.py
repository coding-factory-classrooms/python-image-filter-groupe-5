from _datetime import datetime
import sys

args = sys.argv

print(f"args={args}")

log_file = "image.log"


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


def dump_log():
    try:
        with open(log_file, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError as e:
        print(f"Fichier {log_file} impossible à ouvrir. Error={e} ")