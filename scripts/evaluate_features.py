"""Train simple linear baselines on frozen features.

Expected CSV columns:
  - binary mode: label plus feature columns.
  - multilabel mode: C1..C6 plus feature columns.

This compact script mirrors the paper's use of standardized frozen features and
logistic regression. It is intended for reviewer sanity checks on released
features, not for redistributing raw videos.
"""

from __future__ import annotations

import argparse
import json

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from aigcharm.metrics import binary_metrics, multilabel_metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Feature CSV path.")
    parser.add_argument("--mode", choices=["binary", "multilabel"], default="binary")
    parser.add_argument("--label-col", default="label")
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def feature_columns(df: pd.DataFrame, excluded: set[str]) -> list[str]:
    return [c for c in df.columns if c not in excluded and pd.api.types.is_numeric_dtype(df[c])]


def run_binary(df: pd.DataFrame, args: argparse.Namespace) -> dict[str, float]:
    y = df[args.label_col].astype(int).to_numpy()
    cols = feature_columns(df, {args.label_col, "video_id", "platform"})
    x = df[cols].to_numpy()
    splitter = StratifiedKFold(n_splits=args.folds, shuffle=True, random_state=args.seed)
    rows = []
    for train_idx, test_idx in splitter.split(x, y):
        model = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=1000))
        model.fit(x[train_idx], y[train_idx])
        pred = model.predict(x[test_idx])
        score = model.predict_proba(x[test_idx])[:, 1]
        rows.append(binary_metrics(y[test_idx], pred, score))
    return {key: sum(row[key] for row in rows) / len(rows) for key in rows[0]}


def run_multilabel(df: pd.DataFrame, args: argparse.Namespace) -> dict[str, float]:
    label_cols = ["C1", "C2", "C3", "C4", "C5", "C6"]
    y = df[label_cols].astype(int).to_numpy()
    cols = feature_columns(df, set(label_cols) | {"video_id", "platform"})
    x = df[cols].to_numpy()
    stratify = (y.sum(axis=1) > 0).astype(int)
    splitter = StratifiedKFold(n_splits=args.folds, shuffle=True, random_state=args.seed)
    rows = []
    for train_idx, test_idx in splitter.split(x, stratify):
        model = make_pipeline(
            StandardScaler(),
            OneVsRestClassifier(LogisticRegression(C=1.0, max_iter=1000)),
        )
        model.fit(x[train_idx], y[train_idx])
        pred = model.predict(x[test_idx])
        score = model.predict_proba(x[test_idx])
        rows.append(multilabel_metrics(y[test_idx], pred, score))
    return {key: sum(row[key] for row in rows) / len(rows) for key in rows[0]}


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.csv)
    result = run_binary(df, args) if args.mode == "binary" else run_multilabel(df, args)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

