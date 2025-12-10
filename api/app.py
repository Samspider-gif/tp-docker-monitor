import os
import logging
import psycopg2
from flask import Flask

app = Flask(__name__)

# Création du dossier de logs s'il n'existe pas
if not os.path.exists('/app/logs'):
    os.makedirs('/app/logs')

# Config des logs vers le volume partagé
logging.basicConfig(filename='/app/logs/api.log', level=logging.INFO)

@app.route('/')
def home():
    logging.info("Requete recue sur /")
    return "API Operationnelle (Debian)!"

@app.route('/db')
def db_test():
    try:
        # Connexion à la DB via son nom DNS "db"
        conn = psycopg2.connect(
            host="db",
            database=os.environ.get('DB_NAME', 'mydb'),
            user=os.environ.get('DB_USER', 'user'),
            password=os.environ.get('DB_PASS', 'password')
        )
        logging.info("Succes connexion DB")
        return "Connexion Base de Donnees : REUSSIE"
    except Exception as e:
        logging.error(f"Erreur DB: {e}")
        return f"Echec connexion DB : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
