import unittest
def replaceWords(dict,sentence):
    def prefix(s,dict):
        for word in dict:
            if s.find(word)==0:
                return word
        return s
    
    dict.sort()
    sl = sentence.split(" ")
    r=[]
    for s in sl:
        r.append(prefix(s,dict))
    return " ".join(r)

class TestMethod(unittest.TestCase):
    def test1(self):
        dict = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        expected = "the cat was rat by the bat"
        self.assertEqual(expected, replaceWords(dict,sentence))
unittest.main()
            