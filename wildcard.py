import unittest
def match(s,p):
    sl=list(s)
    pl=list(p)
    try:
        card=pl.pop()
    except IndexError:
        return True

    while len(sl)>0:
        if card=="*":
            try:
                nextcard=pl.pop()
                if pl==[] and not nextcard=="*" and not sl==[]: return sl.pop()==nextcard
                while not sl.pop()==nextcard:
                    pass
                card=pl.pop()
            except IndexError:
                break
        elif sl.pop()==card or card=="?":
            try:
                card=pl.pop()
                if sl==[]: return False
            except IndexError:
                return sl==[]
        else:
            return False

    return pl==[]


class TestMethod(unittest.TestCase):
    def test1(self):
        self.assertEqual(False,match("aa","a"))
    
    def test2(self):
        self.assertEqual(True,match("aa","*"))

    def test3(self):
        self.assertEqual(False,match("cb","?a"))

    def test4(self):
        self.assertEqual(True,match("adceb","*a*b"))

    def test5(self):
        self.assertEqual(False,match("acdcb","a*c?b"))
    
    def test6(self):
        self.assertEqual(True,match("",""))

    def test7(self):
        self.assertEqual(True,match("aa","aa"))
    
    def test8(self):
        self.assertEqual(False,match("a","aa"))

    def test9(self):
        self.assertEqual(True,match("abefcdgiescdfimde","ab*cd?i*de"))

    def test10(self):
        self.assertEqual(False,match("aab","c*a*b"))

    def test11(self):
        self.assertEqual(True,match("aa","a*"))

unittest.main()