"""Metric helpers used by the compact reproducibility scripts."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    f1_score,
    precision_score,
    recall_score,
)


def binary_metrics(y_true, y_pred, y_score=None) -> dict[str, float]:
    """Return Task A binary harmful-content metrics in percentages."""

    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    out = {
        "accuracy": 100.0 * accuracy_score(y_true, y_pred),
        "precision": 100.0 * precision_score(y_true, y_pred, zero_division=0),
        "recall": 100.0 * recall_score(y_true, y_pred, zero_division=0),
        "f1": 100.0 * f1_score(y_true, y_pred, zero_division=0),
    }
    if y_score is not None:
        out["ap"] = 100.0 * average_precision_score(y_true, y_score)
    return out


def multilabel_metrics(y_true, y_pred, y_score=None) -> dict[str, float]:
    """Return Task B sample F1, macro F1, mAP, and per-category F1."""

    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    out = {
        "sample_f1": 100.0 * f1_score(y_true, y_pred, average="samples", zero_division=0),
        "macro_f1": 100.0 * f1_score(y_true, y_pred, average="macro", zero_division=0),
    }
    per_category = f1_score(y_true, y_pred, average=None, zero_division=0)
    for idx, value in enumerate(per_category, start=1):
        out[f"c{idx}_f1"] = 100.0 * float(value)
    if y_score is not None:
        out["map"] = 100.0 * average_precision_score(y_true, y_score, average="macro")
    return out

