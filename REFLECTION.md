Reflection — Part A (brief)

1) Describe the red–green–refactor cycle and why tests first
- Red: write a small failing test that specifies desired behaviour.
- Green: write the smallest change to make the test pass (can be fake).
- Refactor: clean up design while keeping tests green.
- Writing tests first forces small steps, provides a safety net for refactoring, and makes design evolve from real usage.

2) Choices made during implementation
- Used Fake It and Triangulate for early steps (hard-coded value then generalised).
- Adopted value-object style for `Quantity` so operations return new objects.
- Deferred addition evaluation via `Sum` and used `Converter` to reduce expressions to a unit.

3) Difficulties and learning
- Converting units required deciding where conversion logic should live; tests drove the decision to introduce `Sum.reduce` and `Converter.rate`.
- Keeping tests small and focused made incremental commits straightforward.
