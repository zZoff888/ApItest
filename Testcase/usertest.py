import unittest
from pages.UserAPI import User

class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        User.set_token()
        User.set_header()

    #
    def test01(self):
        value=User.getSysUserLoginList()
        print(value)
        self.assertIn("成功", value)


    #
    def test02(self):
        value=User.getSysJobLogsList()
        print(value)
        self.assertIn("成功", value)

    def test03(self):
        value=User.getUserList()
        print(value)
        self.assertIn("成功", value)

    #
    def test04(self):
        value=User.admin_register()
        print(value)
        self.assertIn("成功", value)

    #
    def test05(self):
        value=User.setUserAuthority()
        print(value)
        self.assertIn("成功", value)
        # print(value)

    #
    def test06(self):
        value=User.resetPassword()
        print(value)
        self.assertIn("成功", value)
        # print(value)
#
    def test07(self):
        value=User.deleteUser()
        print(value)
        self.assertIn("成功", value)
        # print(value)
#
    def test08(self):
        value=User.getAuthorityList()
        print(value)
        self.assertIn("成功", value)

    def test09(self):
        value=User.setDataAuthority()
        print(value)
        self.assertIn("成功", value)

    def test10(self):
        value=User.getAuthority()
        print(value)
        self.assertIn("成功", value)

    def test11(self):
        value=User.getAuthoritySourceList()
        print(value)
        self.assertIn("成功", value)


if __name__ == '__main__':
    unittest.main()