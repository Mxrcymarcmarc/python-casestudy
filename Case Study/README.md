# python-casestudy

A small, config-driven data pipeline for ingesting, transforming, analysing, and reporting on CSV data.

## Getting started (very quick)

These steps get you up and running in a Windows PowerShell environment.

```powershell
# create and activate a virtual environment (PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run the pipeline
python src\main.py

# run tests
pip install pytest; pytest -q
```

## Features

### Config-driven pipeline
- Files: `config_default.json`, `config.json`
- What: Behaviour (paths, thresholds, output options) is controlled via configuration so you can reuse the pipeline without editing source code.

### Data ingestion
- Files: `src/ingest.py`
- What: Loads raw input from `data/input.csv` into a dataframe or structured records and performs basic validation.

### Data transformation & cleaning
- Files: `src/transform.py`
- What: Cleans, type-casts, and derives features needed for analysis. Handles missing values and simple coercions.

### Analysis & metrics
- Files: `src/analyze.py`
- What: Computes summary statistics and domain-relevant metrics used to drive reports.

### Reporting and export
- Files: `src/reports.py`
- What: Produces human-readable console summaries and optional CSV/text exports (configurable output folder).

### CLI / orchestrator
- Files: `src/main.py`
- What: Entry point that runs the pipeline end-to-end: ingest → transform → analyze → report.

### Tests
- Files: `tests/test_main.py`
- What: Basic tests that validate the main flow and key behaviours.

## Quick usage notes

- Input: `data/input.csv` by default — change in `config.json`.
- Output: Reports are written to a configurable output folder (see `config.json`).
- Reproducibility: If `config.json` is missing keys, `config_default.json` provides sensible defaults.

## Configuration (where to look)

Open `config_default.json` to see all available configuration keys. Typical keys include:
- `input_path` — path to the CSV input
- `output_dir` — directory to write reports/exports
- `report_format` — (e.g., `text` or `csv`)

Note: I inferred these example keys for clarity — check `config_default.json` for the exact keys used by this project.

## Running tests

The project uses pytest for basic testing. From the project root:

```powershell
pytest -q
```

## Troubleshooting

- Empty or missing `data/input.csv`: The ingestion step will report the missing file — ensure the path in `config.json` is correct.
- Missing columns or wrong types: Check the validation messages emitted during `ingest`/`transform` and fix the source CSV or update transformation rules.
- Large files: This project loads data into memory. For very large datasets, consider adding chunked ingestion in `src/ingest.py`.

## Where are the important files?

- Source: `src/` (ingest, transform, analyze, reports, main)
- Config: `config.json`, `config_default.json`
- Data: `data/input.csv`
- Tests: `tests/`

## Next steps (suggested)

- Add a short example report output to the repo so users know what to expect.
- Add a focused unit test for a small transform function (happy path + missing value case).
- Document exact `config.json` keys in a dedicated `Configuration` section if you want more discoverability.

If you'd like, I can add this Features/Getting Started content directly into `README.md` (already done) and open a follow-up change to include a sample output or a dedicated Configuration section with exact keys.