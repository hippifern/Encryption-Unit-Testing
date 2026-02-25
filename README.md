# Python Encryption – QA-Focused Unit Testing Example

## Overview

This project demonstrates **QA-oriented unit testing in Python**, with a focus on **behaviour validation, input contracts, and negative-path testing**, rather than algorithmic complexity.

The system implements a simple character-shift cipher (`encrypt` / `decrypt`) and a corresponding test suite designed to validate **correctness, constraints, and failure modes**.

The goal of this repository is to showcase **QA automation thinking**: defining clear requirements and writing tests that enforce them.

---

## Functionality

### Encryption Logic

- Each character is shifted forward by one position within a predefined character set:
  - Uppercase and lowercase letters
  - Punctuation
  - Digits
  - Space
- The cipher wraps around at the end of the character set.
- Decryption reverses the process.

This is **not intended to be a secure encryption algorithm** — it exists purely as a vehicle for testing behaviour.

---

## Defined System Constraints

The following rules are intentionally enforced and validated by tests:

1. **Minimum input length**
   - Messages must be at least 2 characters long
   - Shorter inputs raise a `ValueError`

2. **Supported characters only**
   - Any character not present in the allowed character set (e.g. `Ñ`) causes a `ValueError`
   - Prevents silent or undefined behaviour

3. **Length preservation**
   - Encrypted and decrypted messages must always match the original message length

4. **Non-identity encryption**
   - Valid input must not encrypt to itself

5. **Reversibility**
   - Decrypting an encrypted message must return the original input

---

## Test Coverage

The test suite is written using Python’s built-in `unittest` framework and focuses on **risk-based validation** rather than implementation details.

### Covered Scenarios

- ❌ Invalid input length raises an error  
- ❌ Unsupported characters raise an error  
- ✅ Encryption modifies the input  
- ✅ Output length is preserved  
- ✅ Known-value encryption correctness  
- ✅ Encryption → decryption round-trip integrity  

Each test is designed to map directly to a **specific system requirement or failure risk**.

---

## Why This Project Exists

This repository is intended as a **portfolio example for QA automation roles**, demonstrating:

- Explicit definition of system behaviour
- Defensive input validation
- Negative-path testing
- Behaviour-driven assertions
- Clear separation between implementation and verification

The emphasis is on **test intent and coverage**, not on building production-grade encryption.

---

## Running the Tests

From the project directory:

```bash
python encryption_test.py