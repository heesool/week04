import unittest
from unittest.mock import patch

from greetlab.cli import main


class TestCLI(unittest.TestCase):
    def test_normal_name_prints_greeting(self):
        with patch("sys.argv", ["sdt-greet", "--name", "Alice"]):
            with patch("builtins.print") as mock_print:
                main()

        mock_print.assert_called_once_with("Hello, Alice!")

    def test_whitespace_name_exits_with_2(self):
        with patch("sys.argv", ["sdt-greet", "--name", "   "]):
            with self.assertRaises(SystemExit) as cm:
                main()

        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
