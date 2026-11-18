from datetime import datetime, timezone

def solve(value):
    return (lambda d: d.astimezone(timezone.utc).isoformat() if d.tzinfo else (_ for _ in ()).throw(ValueError("timezone offset required")))(datetime.fromisoformat(value))
