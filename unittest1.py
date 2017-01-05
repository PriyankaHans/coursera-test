import unittest
from read1 import *
#from read1 import read_data
#from read1 import count_data


class CSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'incident.csv'

    def test_read_coloumns(self):
        self.assertEqual(
            read_data(self.data)[0],
            ["number","opened_at","short_description","caller_id","priority","state","category","assignment_group","assigned_to","sys_updated_on","sys_updated_by"]
            )

    def test_read_incident_number(self):
        self.assertEqual(read_data(self.data)[1][0], 'INC0010007')

    def test_read_cat(self):
        self.assertEqual(read_data(self.data)[1][6], 'Inquiry / Help')
		
    def test_read_count(self):
        self.assertEqual(count_data(self.data), 55)
	
    def test_db_count(self):
        self.assertEqual(db_data(), 6)


if __name__ == '__main__':
    unittest.main()