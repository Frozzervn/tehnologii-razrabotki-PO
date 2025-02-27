import Test_2

def test_stroka():
    if Test_2.back_string("Hello boy") == "yob olleH":
        print("Test stroka(Hello boy) is OK ")
    else:
        print("Test stroka(Hello boy) is Fail")

def test_stroka():
    if Test_2.back_string("Car") == "raC":
        print("Test stroka(Car) is OK ")
    else:
        print("Test stroka(Car) is Fail")

def test_stroka():
    if Test_2.back_string("Tools") == "slooT":
        print("Test stroka(Tools) is OK ")
    else:
        print("Test stroka(Tools) is Fail")

def test_stroka():
    if Test_2.back_string("World") == "dlroW":
        print("Test stroka(World) is OK ")
    else:
        print("Test stroka(World) is Fail")

def test_stroka():
    if Test_2.back_string("Wolf") == "floW":
        print("Test stroka(Wolf) is OK ")
    else:
        print("Test stroka(Wolf) is Fail")


#------------------------------------------------------------------------------
def test_polindrome():
    if Test_2.polindrome("Anastasia") == "Anastasia":
        print("Test polindrome(Anastasia) is OK")
    else:
        print("Test polindrome(Anastasia) is Fail")

def test_polindrome():
    if Test_2.polindrome("stats") == "stats":
        print("Test polindrome(stats) is OK")
    else:
        print("Test polindrome(stats) is Fail")

def test_polindrome():
    if Test_2.polindrome("refer") == "refer":
        print("Test polindrome(refer) is OK")
    else:
        print("Test polindrome(refer) is Fail")

def test_polindrome():
    if Test_2.polindrome("madam") == "madam":
        print("Test polindrome(madam) is OK")
    else:
        print("Test polindrome(madam) is Fail")

def test_polindrome():
    if Test_2.polindrome("levels") == "levels":
        print("Test polindrome(levels) is OK")
    else:
        print("Test polindrome(levels) is Fail")
#------------------------------------------------------------------------------
def test_voweles():
    if Test_2.vowels("Шишка") == 1 :
        print("Test vowels(Шишка) is OK")
    else:
        print("Test vowels(Шишка) is Fail")

def test_voweles():
    if Test_2.vowels("Машинка") == 3 :
        print("Test vowels(Машинка) is OK")
    else:
        print("Test vowels(Машинка) is Fail")

def test_voweles():
    if Test_2.vowels("Собачка") == 3 :
        print("Test vowels(Собачка) is OK")
    else:
        print("Test vowels(Собачка) is Fail")

def test_voweles():
    if Test_2.vowels("Моль") == 2 :
        print("Test vowels(Моль) is OK")
    else:
        print("Test vowels(Моль) is Fail")

def test_voweles():
    if Test_2.vowels("Универ") == 2 :
        print("Test vowels(Универ) is OK")
    else:
        print("Test vowels(Универ) is Fail")
#------------------------------------------------------------------------------
def test_duplicate():
    if Test_2.remove_duplicates("Hello world") == "Helo wrd":
        print("Test duplicate(Hello world) is OK")
    else:
        print("Test duplicate(Hello world) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("he knows Inglish") == "he knows gli":
        print("Test duplicate(he knows Inglish) is OK")
    else:
        print("Test duplicate(he knows Inglish) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("qweqweqwe") == "qwe":
        print("Test duplicate(qweqweqwe) is OK")
    else:
        print("Test duplicate(qweqweqwe) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("sjkdghkjsd") == "asd":
        print("Test duplicate(sjkdghkjsd) is OK")
    else:
        print("Test duplicate(sjkdghkjsd) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("lklklklklkA") == "zxc":
        print("Test duplicate(lklklklklkA) is OK")
    else:
        print("Test duplicate(lklklklklkA) is Fail")
#-----------------------------------------------------------------------------
test_stroka()
test_polindrome()
test_voweles()
test_duplicate()