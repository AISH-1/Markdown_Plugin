# Markdown 2 Suite

A customized Dify plugin focused on 4 tools only:
- `markdown_2_docx`
- `markdown_2_csv`
- `markdown_2_pdf`
- `markdown_2_xlsx`

## Author
- `Aish`

## What This Plugin Does
- Convert Markdown text to DOCX.
- Convert Markdown tables to CSV.
- Convert Markdown text to PDF.
- Convert Markdown tables to XLSX.

## Dify Plugin Structure
- Provider config: `provider/markdown_2_suite.yaml`
- Tool definitions:
  - `tools/md_to_docx/md_to_docx.yaml`
  - `tools/md_to_csv/md_to_csv.yaml`
  - `tools/md_to_pdf/md_to_pdf.yaml`
  - `tools/md_to_xlsx/md_to_xlsx.yaml`

## Local Development
- Python 3.11+
- Install dependencies:
  - `uv sync`
  - or `pip install -r requirements.txt`

## Tests
- Run all:
  - `test/bin/run_all_tests.sh`
- Run one:
  - `test/bin/test_md_to_docx.sh`
  - `test/bin/test_md_to_csv.sh`
  - `test/bin/test_md_to_pdf.sh`
  - `test/bin/test_md_to_xlsx.sh`

## Notes
- This repository has been intentionally trimmed to only the 4 tools above.

