
import hashlib, json, os, time
from typing import Dict, Optional
import matplotlib.pyplot as plt

def make_signed_artifact(payload: Dict, outdir: str = "artifacts"):
    os.makedirs(outdir, exist_ok=True)
    ts = int(time.time())
    raw = json.dumps({"ts": ts, **payload}, sort_keys=True, indent=2).encode("utf-8")
    sha = hashlib.sha256(raw).hexdigest()
    jpath = os.path.join(outdir, f"artifact_{ts}_{sha[:8]}.json")
    with open(jpath, "wb") as f:
        f.write(raw)
    return {"json_path": jpath, "sha256": sha}

def save_chart(series_x, series_y, outdir: str = "artifacts", name: Optional[str] = None):
    os.makedirs(outdir, exist_ok=True)
    if name is None:
        name = f"chart_{int(time.time())}.png"
    cpath = os.path.join(outdir, name)
    plt.figure()
    plt.plot(series_x, label="X (social)")
    plt.plot(series_y, label="Y (on-chain)")
    plt.legend()
    plt.title("CaOps Demo Series")
    plt.tight_layout()
    plt.savefig(cpath)
    plt.close()
    return cpath
