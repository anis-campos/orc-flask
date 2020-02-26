import unittest

from fbapp.utils import OpenGraphImage


class UtilsTest(unittest.TestCase):

    def test_image_creation(self):
        description = "Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, " \
                      "tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du " \
                      "caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, " \
                      "tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? " \
                      ";-) "
        opi = OpenGraphImage('test', 'Céline', description)
        opi.image.show()
