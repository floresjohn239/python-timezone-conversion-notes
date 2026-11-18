# Convert a fixed-offset instant to UTC: implementation

## What the example does

An explicit source offset is required. Naive datetimes are rejected rather than assuming the computer timezone.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"2026-01-01T08:00:00+08:00"
```

Expected result:

```json
"2026-01-01T00:00:00+00:00"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
