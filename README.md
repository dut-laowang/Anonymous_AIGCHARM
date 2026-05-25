# AIGenHarm-Video

Resources and code for the anonymous paper:

**AIGenHarm-Video: A Benchmark and Analysis of AI-Generated Harmful Video Understanding**

Project page: `https://anonymous.4open.science/r/Anonymous_AIGCHARM`

## Overview

`AIGenHarm-Video` is a public-platform benchmark for downstream moderation of AI-generated harmful videos. The benchmark contains 1,808 videos collected from TikTok and Bilibili, including 993 harmful and 815 safe videos, with hierarchical annotations for harmfulness, six harm categories, and explicit or implicit presentation.

The repository provides:

- a static project website in `index.html`, `annotation.html`, and `cases.html`;
- compact annotation guidelines and access instructions;
- case-study examples aligned with the paper;
- lightweight evaluation utilities in `src/aigcharm` and `scripts`.

Raw videos are not redistributed in this anonymous repository. Access to annotations, metadata, derived features, and raw-video review materials requires a controlled-access request.

## Dataset Access

Dataset access request form:

`[Google Form link to be added]`

The form will collect reviewer or researcher information, intended use, agreement to safety handling requirements, and confirmation that the data will be used only for research and benchmark evaluation.

## Repository Layout

```text
Anonymous_AIGCHARM/
  index.html                 # project home page
  annotation.html            # annotation guide and data-access console
  cases.html                 # qualitative case-study page
  assets/                    # website CSS, JS, and paper figures
  src/aigcharm/              # compact schema, metrics, and prompts
  scripts/                   # small reproducibility scripts
  docs/                      # extra notes for controlled release
```

## Quick Start

The website is static and can be opened directly:

```bash
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000
```

For the lightweight evaluation utilities:

```bash
pip install numpy pandas scikit-learn
python scripts/evaluate_features.py --help
```

## Citation

Citation information will be added after the review process.

