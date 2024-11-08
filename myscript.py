import os
import sys

# Récupérer les arguments des hachages de commits
if len(sys.argv) < 3:
    print("Usage: python myscript.py <badhash> <goodhash>")
    sys.exit(1)

badhash = sys.argv[1]
goodhash = sys.argv[2]

# Exécuter les commandes de git bisect
os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
