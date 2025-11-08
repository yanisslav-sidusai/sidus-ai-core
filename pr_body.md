## SIDUS AI Hackathon — CaOps (Causality Operations)

**Category:** Integrations (Plugins)  
**Author:** Yanislav Iliev (@yiliev)

### What this adds
Reusable SIDUS AI plugins for TON + social correlation:
- `caops_ton` — TON client (fixture-ready)
- `caops_x` — social fetcher (skeleton)
- `caops_correlator` — anomaly + Granger causality
- `caops_reporter` — signed JSON artifacts + chart PNG
- `caops_telegram` — Telegram UX (dry-run)

### How to run locally
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. python3 samples/run_demo.py --mode dry
	•	Artifacts are signed with SHA256 for reproducibility.
	•	SIDUS-themed dashboard: uvicorn dashboards.app:app --reload --port 8787.
	•	License: Apache-2.0
