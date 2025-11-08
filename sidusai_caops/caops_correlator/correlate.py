
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

def zscore_anomaly(series: pd.Series, window: int = 24, threshold: float = 3.0):
    rol_mean = series.rolling(window=window, min_periods=1).mean()
    rol_std = series.rolling(window=window, min_periods=1).std().replace(0, 1)
    z = (series - rol_mean) / rol_std
    return z.abs() > threshold, z

def granger_test(series_x: pd.Series, series_y: pd.Series, maxlag: int = 6):
    df = pd.concat([series_y, series_x], axis=1).dropna()
    if df.shape[0] < maxlag + 2:
        return {"ok": False, "reason": "not enough data"}
    try:
        res = grangercausalitytests(df, maxlag=maxlag, verbose=False)
        pvals = {lag: res[lag][0]['ssr_ftest'][1] for lag in res}
        bestlag = min(pvals, key=pvals.get)
        return {"ok": True, "bestlag": int(bestlag), "pvalue": float(pvals[bestlag])}
    except Exception as e:
        return {"ok": False, "reason": str(e)}

def explain_causality(x_ts, y_ts):
    g = granger_test(x_ts, y_ts, maxlag=6)
    if not g["ok"]:
        return f"Insufficient data / error: {g.get('reason')}"
    return f"Granger causality: X -> Y best lag={g['bestlag']} p={g['pvalue']:.4f}"
