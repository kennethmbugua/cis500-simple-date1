import unittest
import my_date


class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    def test_ordinal_date1(self):
        self.assertEqual(my_date.ordinal_date(2020, 3, 1), 61)

    def test_ordinal_date2(self):
        self.assertEqual(my_date.ordinal_date(2023, 3, 1), 60)

    def test_days_elapsed1(self):
        self.assertEqual(my_date.days_elapsed(2020, 11, 30, 2021, 1, 2), 33)

    def test_days_elapsed2(self):
        self.assertEqual(my_date.days_elapsed(2019, 11,30,2020,3,2),93)
    def test_day_of_week1(self):
        self.assertEqual(my_date.day_of_week(2019,1,12), "Saturday")

    def test_day_of_week2(self):
        self.assertEqual(my_date.day_of_week(2019, 2, 20), "Wednesday")

    def test_to_str1(self):
        self.assertEqual(my_date.to_str(2019, 2, 20), "Wednesday, 20, February, 2019")

    def test_to_str2(self):
        self.assertEqual(my_date.to_str(2019,1,12),"Saturday, 12, January, 2019")

    def test_to_str3(self):
        self.assertEqual(my_date.to_str(2019,12,25),"Wednesday, 25, December, 2019")
    def test_to_str4(self):
        self.assertEqual(my_date.to_str(1833,3,7),"Thursday, 07, March, 1833")
    def test_to_str5(self):
        self.assertEqual(my_date.to_str(1290,5,13),"Saturday, 13, May, 1290")


if __name__ == '__main__':
    unittest.main()
