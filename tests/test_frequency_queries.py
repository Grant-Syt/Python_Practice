
import unittest
from frequency_queries import freqQuery
import frequency_queries

class TestSum(unittest.TestCase):

    def test_fq5(self):
        with open("./frequency_queries/input05.txt", "r") as input_file:
            queries = input_file.read()
        queries = queries.split()[1:] # list excluding size
        # group query pairs
        queries = [[int(queries[a]), int(queries[a+1])] for a in range(0, len(queries)-1, 2)]
        print(queries)
        
        with open("./frequency_queries/output05.txt", "r") as output_file:
            expected = output_file.read()
        expected = expected.split()
        print(expected)

        result = freqQuery(queries)
        print(result)
        with open("./frequency_queries/result.txt", "w") as result_file:
            for i in result:
                result_file.write(str(i) + "\n")

        self.assertEqual(result, expected, "Test 5 failed")


if __name__ == '__main__':
    unittest.main()
