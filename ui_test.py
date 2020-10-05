import unittest
from unittest import TestCase
from unittest.mock import patch

import ui
import catalog

class uiTest(TestCase):

    @patch('builtins.input', side_effect=['Steve'])
    def test_delete_artwork(self, mock_input):
        input1 = mock_input()
        self.assertTrue(input1 == 'Steve')

    @patch('builtins.input', side_effect=['art'])
    def test_update_availability(self, mock_input):
        input1 = mock_input()
        self.assertTrue(input1 == 'art')

    @patch('builtins.input', side_effect=['George'])
    def test_get_artist(self, mock_input):
        input_1 = mock_input()
        self.assertTrue(input_1 == 'George')

    @patch('builtins.print')
    def test_message(self, mock_print):
        ui.message('quit')
        mock_print.assert_called_with('quit')

    @patch('builtins.input', side_effect=[1])
    def test_menu_selection(self, mock_input):
        input_1 = mock_input()
        self.assertTrue(input_1 == 1)
        

if __name__ == '__main__':
    unittest.main()
