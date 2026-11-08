# Contributing

Keep this toolkit original and game-neutral. Do not submit code, assets, tokens, Roblox place IDs or private data from another game without explicit authorization and appropriate licenses.

If proposing a new practice, first provide a reproducible agent-use failure scenario, then write a narrow original playbook with activation trigger, procedure, evidence and guardrail. Add its mapping to `references/coverage.json` only if it has actually been sourced and audited. Update static package tests when the fixed 41-playbook inventory changes.

For changes to the starter or verification scripts, run `python3 -m unittest discover -s scripts/tests -v` and `python3 scripts/verify_package.py`. Record a real-agent baseline and skill-enabled trial in `AGENT_VALIDATION_SCENARIOS.md` before claiming behavior validated. Public publishing/marketplace listing is a separate approval.
