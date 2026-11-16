"Passed": passed,
        "Failed": failed,
        "Blocked": blocked,
        "Not Run": not_run,
    }

    missing = [name for name, count in counts.items() if count is None]
    if missing:
        return f"UNABLE TO VERIFY: Missing {', '.join(missing)}."

    total = passed + failed + blocked + not_run
    difference = total - planned

    if difference == 0:
        return f"PASS: All {planned} planned tests are accounted for."

    direction = "below" if difference < 0 else "above"
    return (
        f"FAIL: Planned {planned}, calculated total {total}. "
        f"The total is {abs(difference)} {direction} plan."
    )
