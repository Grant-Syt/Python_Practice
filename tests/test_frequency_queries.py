
import unittest
from frequency_queries import freqQuery

class TestFQ(unittest.TestCase):

    def test_fq5(self):

        # queries
        with open("./frequency_queries/input05.txt", "r") as input_file:
            queries = input_file.read()
        queries = queries.split()[1:] # list excluding size
        # group query pairs
        queries = [[int(queries[a]), int(queries[a+1])] for a in range(0, len(queries)-1, 2)]
        # print(queries)
        
        # expected output
        with open("./frequency_queries/output05.txt", "r") as output_file:
            expected = output_file.read()
        expected = expected.split()
        expected = list(map(int, expected))
        # print(expected)

        # actaul output
        result = freqQuery(queries)
        # print(result)

        self.assertEqual(result, expected, "Test 5 failed")


if __name__ == '__main__':
    unittest.main()
