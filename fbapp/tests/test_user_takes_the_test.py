from os import environ

from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import create_app
from .. import models


class TestUserTakesTheTest(LiveServerTestCase):
    def create_app(self):
        if environ.get('FLASK_ENV') is None:
            environ["FLASK_ENV"] = "testing"
        return create_app()

    # Méthode exécutée avant chaque test
    def setUp(self):
        """Setup the test driver and create test users"""
        # Le navigateur est Firefox
        self.driver = webdriver.Firefox()
        # Ajout de données dans la base.
        models.init_db()

    # Méthode exécutée après chaque test
    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        # On ouvre le navigateur avec l'adresse du serveur.
        self.driver.get(self.get_server_url())
        # L'adresse dans l'url doit être celle que l'on attend.
        assert self.driver.current_url == 'http://localhost:8943/'
