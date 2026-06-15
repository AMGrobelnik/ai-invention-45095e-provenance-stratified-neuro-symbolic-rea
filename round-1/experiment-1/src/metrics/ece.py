"""Expected Calibration Error (ECE) for L3 confidence scores."""
import numpy as np


def compute_ece(confidences: list[float], labels: list[int], n_bins: int = 10) -> float:
    """Compute ECE: weighted average |avg_conf - fraction_positive| per bin."""
    if not confidences:
        return 0.0
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    n = len(confidences)
    for b in range(n_bins):
        lo, hi = bins[b], bins[b + 1]
        mask = [lo <= c < hi for c in confidences]
        if not any(mask):
            continue
        bin_confs = [c for c, m in zip(confidences, mask) if m]
        bin_labels = [l for l, m in zip(labels, mask) if m]
        avg_conf = float(np.mean(bin_confs))
        frac_pos = float(np.mean(bin_labels))
        ece += (len(bin_confs) / n) * abs(avg_conf - frac_pos)
    return ece
