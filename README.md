Project: itds362-tdd

Contents
- `kitchen.py` — production code
- `test_kitchen.py` — pytest tests covering Part A
- commit history on branch `tdd-sequence-commits` demonstrates TDD red/green steps

How to run
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Submission notes
- The TDD rhythm (red → green → refactor) is recorded as individual commits on branch `tdd-sequence-commits`.
- Please use that branch when reviewing commit history; the tests pass (7 passed).
