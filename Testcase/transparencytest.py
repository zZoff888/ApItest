import unittest
from pages.TransparencyAPI import Transparency

class AnnouncingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Transparency.set_token()

    #
    def test01(self):
        value=Transparency.getTransparency()
        print(value)
        self.assertIn("成功", value)
#
    def test02(self):
        value=Transparency.getNetworth()
        print(value)
        self.assertIn("成功", value)


if __name__ == '__main__':
    unittest.main()