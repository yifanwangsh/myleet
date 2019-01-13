import unittest
def licenseKeyFormatting(S,K):
    S=S.upper()
    S=S.replace("-","")
    r=""
    while len(S)>0:
        r="-"+S[-K:]+r
        S=S[:-K]
    return r.replace("-","",1)

class TestFunc(unittest.TestCase):
    def test1(self):
        S = "5F3Z-2e-9-w"
        K = 4
        expected = "5F3Z-2E9W"
        self.assertEqual(expected,licenseKeyFormatting(S,K))

unittest.main()