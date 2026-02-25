# Test Strategy – Python Encryption Project

## Project Overview

This project implements a simple character-shift cipher with an accompanying test suite and CLI interface.  
The purpose of this project is to demonstrate **QA-focused testing practices**, including:

- Behaviour-driven validation
- Negative-path / edge-case testing
- Interface-level testing (CLI)
- Risk-based test coverage

The project is not intended for production-grade encryption — its value lies in **demonstrating QA skills**.

---

## Objectives

1. Verify that encryption and decryption behave according to system rules.
2. Ensure that invalid input is handled gracefully and predictably.
3. Test both functional behavior (unit tests) and user-facing interface behavior (CLI).
4. Document risks and testing approach in a clear, professional format.

---

## Scope

### In Scope

- Unit testing of `encrypt` and `decrypt` functions
- Negative-path testing for invalid inputs:
  - Input length < 2
  - Unsupported characters
- Round-trip encryption → decryption integrity
- CLI interface:
  - Command parsing
  - Input validation
  - Error reporting
- Known-value test for encryption output

### Out of Scope

- Production-grade cryptography
- Performance testing for large-scale input
- Multi-language / Unicode support (outside ASCII + basic punctuation + digits + space)
- Multi-threaded execution

---

## Test Approach

| Test Type | Target | Objective | Method |
|-----------|--------|-----------|--------|
| Unit | `encrypt` function | Correctly shifts characters | `unittest` assertions |
| Unit | `decrypt` function | Correctly reverses shifts | `unittest` assertions |
| Unit | Negative inputs | Input < 2 chars / unsupported chars | `assertRaises(ValueError)` |
| Unit | Round-trip | `decrypt(encrypt(msg)) == msg` | Deterministic assertion |
| Unit | Known-value encryption | Validate predictable output | Compare against precomputed string |
| CLI | Command parsing | Correct command execution | `subprocess` tests, exit codes |
| CLI | Input validation | Detect invalid inputs | Capture stdout/stderr, check for `Error` |
| CLI | Unknown commands | Fail gracefully | Capture usage output and non-zero exit code |

---

## Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Unsupported characters | Incorrect encryption / crash | Unit test raises `ValueError` |
| Short inputs | Silent failure / incorrect output | Unit test raises `ValueError` |
| Encryption equals input | Data not transformed | Assert `encrypt(msg) != msg` |
| Decryption fails | Data loss | Round-trip unit test |
| CLI misbehaves | Poor user experience | CLI tests with invalid inputs and unknown commands |
| Regression | Bugs in updates | Separation of CLI, core logic, and tests |

---

## Assumptions

- All input messages are ASCII letters, digits, punctuation, or space
- Messages < 2 characters or containing unsupported characters are invalid
- CLI will be run in Python 3.x environment
- Test suite is run in the same environment as code execution

---

## Deliverables

- `encryption.py`: Core logic functions
- `cipher.py`: CLI interface
- `encryption_test.py`: Unit tests for core logic
- `cli_test.py`: Tests for CLI behaviour
- `README.md`: Overview and usage instructions
- `TEST_STRATEGY.md`: Documentation of QA approach and risks

---