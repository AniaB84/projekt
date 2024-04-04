import os

class Config:
    # Klucz sekretny dla zabezpieczenia sesji i innych
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'trudno-mi-zgadnąć-coś-bardzo-tajnego'

    # Konfiguracja bazy danych - tu zakładam użycie bazy SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
