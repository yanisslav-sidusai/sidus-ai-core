
import os, json
from typing import List, Dict, Any

class TonClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def get_transactions(self, address: str, limit: int = 50) -> List[Dict[str, Any]]:
        if not self.api_key:
            return self._load_fixture("txs_sample.json")
        return []

    def get_volume(self, token: str, window_hours: int = 24) -> Dict[str, Any]:
        if not self.api_key:
            return {"token": token, "volume": 12345, "window_hours": str(window_hours)}
        return {"token": token, "volume": None, "window_hours": str(window_hours)}

    def _load_fixture(self, name: str):
        here = os.path.dirname(__file__)
        fixdir = os.path.join(here, "fixtures")
        os.makedirs(fixdir, exist_ok=True)
        fpath = os.path.join(fixdir, name)
        if not os.path.exists(fpath):
            sample = [{"hash": "0xabc", "amount": 10, "ts": 1700000000}]
            with open(fpath, "w") as f:
                json.dump(sample, f)
        with open(fpath) as f:
            return json.load(f)
