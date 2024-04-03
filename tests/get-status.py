import unittest
from unittest.mock import patch
from immortal_client.client import ImmortalClient

class TestImmortalClient(unittest.TestCase):
    @patch('requests.get')
    def test_get_status_success(self, mock_get):
        # Arrange
        base_url = 'http://localhost:3312'
        expected_status = {'status': 'running'}
        mock_get.return_value.json.return_value = expected_status
        client = ImmortalClient(base_url)
        # Act
        status = client.get_status("localhost:9092")
        print(status)
        # Assert
        self.assertEqual(status, expected_status)

    @patch('requests.get')
    def test_get_status_failure(self, mock_get):
        # Arrange
        base_url = 'http://localhost:3312'
        mock_get.return_value.status_code = 500
        client = ImmortalClient(base_url)

        # Act & Assert
        with self.assertRaises(Exception):
            client.get_status("localhost:9093")

if __name__ == '__main__':
    unittest.main()