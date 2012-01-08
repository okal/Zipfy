import unittest
from zipfy import Corpus

class TestCorpus(unittest.TestCase):
   testdata = "The swift brown fox jumped over the lazy dog"
   testdata_freq_list = [
       ('the', 2), 
       ('swift', 1), 
       ('brown', 1), 
       ('fox', 1), 
       ('jumped', 1), 
       ('over', 1), 
       ('lazy', 1), 
       ('dog', 1)
   ]

   corpus = Corpus(testdata)

   def testFreqList(self):
       self.assertEqual(sorted(self.testdata_freq_list), sorted(self.corpus.freq_list))

if __name__ == '__main__':
    unittest.main()
