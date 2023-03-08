import unittest
import os
import requests

class TestIA(unittest.TestCase):
    
    def test_resources_folder_exists(self):
        folder_path = '/IA/ia/resources'
        self.assertTrue(os.path.exists(folder_path))
        
    def test_grobid_is_running(self):
        url = 'http://grobid:8070/api/isalive'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
