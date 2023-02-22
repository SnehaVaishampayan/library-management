import unittest
from ProjectModule import ProjectHandler
from tests.test_constants import error_msg_invalid_pName, result_query, fake_filters, fake_project_details_invalid_name, \
    fake_project_details_invalid_status, error_msg_invalid_status, fake_project_details_valid


class MyTestCase(unittest.TestCase):

    def test_get_query(self):
        expected = result_query
        self.assertEqual(expected, ProjectHandler.get_query(fake_filters))

    def test_validate_project_details(self):
        self.assertTrue(ProjectHandler.validate_project_details(fake_project_details_valid))

    def test_validate_project_details_validateName(self):
        expected = error_msg_invalid_pName
        with self.assertRaises(Exception) as e:
            ProjectHandler.validate_project_details(fake_project_details_invalid_name)
        self.assertEqual(expected, str(e.exception))

    def test_validate_project_details_status(self):
        with self.assertRaises(Exception) as e:
            ProjectHandler.validate_project_details(fake_project_details_invalid_status)
        self.assertEqual(error_msg_invalid_status, str(e.exception))


if __name__ == '__main__':
    unittest.main()
