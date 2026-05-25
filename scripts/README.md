# Scripts

`evaluate_features.py` trains standardized logistic-regression probes on released frozen features.

Example:

```bash
PYTHONPATH=src python scripts/evaluate_features.py \
  --csv released_features_taskA.csv \
  --mode binary \
  --label-col label
```

For Task B:

```bash
PYTHONPATH=src python scripts/evaluate_features.py \
  --csv released_features_taskB.csv \
  --mode multilabel
```

Expected Task B label columns are `C1`, `C2`, `C3`, `C4`, `C5`, and `C6`.

