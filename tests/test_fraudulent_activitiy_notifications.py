
import unittest
from fraudulent_activity_notifications.fraudulent_activity_notifications import activityNotifications, activityNotifications2

class TestFA(unittest.TestCase):

    def test_fa1_1(self):

        with open("./fraudulent_activity_notifications/input1.txt", "r") as input_file:
            data = input_file.read()
        with open("./fraudulent_activity_notifications/output1.txt", "r") as output_file:
            expected = int(output_file.read())

        data = data.split("\n")
        header = data[0].split()
        body = list(map(int, data[1].split()))
        
        result = activityNotifications(body, int(header[1]))

        self.assertEqual(result, expected, "Test 1 failed")

    def test_fa2_1(self):

        with open("./fraudulent_activity_notifications/input1.txt", "r") as input_file:
            data = input_file.read()
        with open("./fraudulent_activity_notifications/output1.txt", "r") as output_file:
            expected = int(output_file.read())

        data = data.split("\n")
        header = data[0].split()
        body = list(map(int, data[1].split()))
        
        result = activityNotifications2(body, int(header[0]), int(header[1]))

        self.assertEqual(result, expected, "Test 1 failed")


if __name__ == '__main__':
    unittest.main()
