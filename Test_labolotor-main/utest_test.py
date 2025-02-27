import unittest
import Test_2
# вывести сроку в обратном порядке
class py_test(unittest.TestCase):
    def test_string(self):
       self.assertEqual(Test_2.back_string('Hello boy'),'yob olleH')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Cars'),'sraC')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Users'),'sresU')

    def test_string(self):
       self.assertEqual(Test_2.back_string('World'),'dlroW')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Ket'),'teK')
#-------------------------------------------------------------------------
# Полиндром
    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('Anastasia'),('Anastasia'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('stars'),('srats'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('referall'),('referall'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('med'),('med'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('level'),('level'))
#---------------------------------------------------------------
    # проверяет количество гласных
    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Ехал'),1)

    def test_vowels(self):
        self.assertEqual(Test_2.vowels('Дом'), 3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Кошка'),3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Универ'),2)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Собака'),2)

    #def test_symbols(self):
     #   self.assertEqual(Test_2.symbol('Hello world'),('Helo wrd')
#-------------------------------------------------------------------------
    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("Hello world"), "Helo wrd")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("he knows Inglish"), "he knows gli")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("qweqweqwe"), "qwe")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("asdasdasd"), "asd")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("zxczxczxc"), "zxc")


if __name__ == 'main':
    unittest.main()