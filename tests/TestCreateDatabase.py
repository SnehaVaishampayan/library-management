import unittest
from unittest.mock import Mock
from unittest.mock import patch
from database import CreateDatabase
from tests.test_constants import fake_result_commit, fake_result_query_data

myMock = Mock()
from database import CreateDatabase


class TestCreateDatabase(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_connect_to_db(self, mock_connect):
        mock_connect.return_value = "a"
        res = CreateDatabase.connect_to_db()
        self.assertEqual("a", res)

    @patch('sqlite3.connect')
    def test_get_cursor(self, mock_connect):
        mock_connect.return_value.cursor.return_value = 'fake_cursor_object'
        result = CreateDatabase.get_cursor()
        self.assertEqual(result, "fake_cursor_object")

    @patch('database.CreateDatabase.connect_to_db')
    def test_create_db_table(self, mock_connect_to_db):
        mock_connect_to_db.return_value.execute.return_value = fake_result_query_data
        mock_connect_to_db.return_value.commit.return_value = fake_result_commit
        CreateDatabase.create_db_table()

if __name__ == '__main__':
    unittest.main()
