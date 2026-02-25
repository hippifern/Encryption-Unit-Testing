import subprocess
import sys
import unittest

def run_cli(args):
    return subprocess.run(
        [sys.executable, "cipher.py"] + args,
        capture_output=True,
        text=True
    )

class TestCLI(unittest.TestCase):
    def test_encrypt_cli(self):
        result = run_cli(["encrypt", "Dublin"])
        assert result.stdout.split("\n")[0] == "Evcmjo"
        assert result.returncode == 0

    def test_decrypt_cli(self):
        result = run_cli(["decrypt", "Evcmjo"])
        assert result.stdout.split("\n")[0] == "Dublin"
        assert result.returncode == 0

    def test_unknown_command_cli(self):
        result = run_cli(["banana", "Hello"])
        assert result.returncode != 0
        assert "Usage" in result.stdout

    def test_missing_arguments_cli(self):
        result = run_cli(["encrypt"])
        assert result.returncode != 0
        assert "Usage" in result.stdout

    def test_invalid_input_length(self):
        result = run_cli(["encrypt", "A"])
        assert result.returncode != 0
        assert "Message must be at least 2 characters" in result.stdout

    def test_unsupported_character(self):
        result = run_cli(["encrypt", "DublinÑ"])
        assert result.returncode != 0
        assert "Message contains invalid characters" in result.stdout


if __name__ == "__main__":
    unittest.main()