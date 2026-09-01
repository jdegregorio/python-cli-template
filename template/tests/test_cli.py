from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from {{PROJECT_MODULE}}.cli import main


class CliTest(unittest.TestCase):
    def test_greets_requested_name(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = main(["agent"])
        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "Hello, agent!\n")


if __name__ == "__main__":
    unittest.main()
