# Markdown 2 Suite Skill

description: Markdown exporter skill limited to 4 tools: DOCX, CSV, PDF, XLSX.

## Tools
- `md_to_docx`: Convert Markdown text to `.docx`
- `md_to_csv`: Convert Markdown tables to `.csv`
- `md_to_pdf`: Convert Markdown text to `.pdf`
- `md_to_xlsx`: Convert Markdown tables to `.xlsx`

## Requirements
- Python 3.11+
- `uv` preferred, or `pip`

## Usage

```bash
scripts/md-exporter md_to_docx <input.md> <output.docx>
scripts/md-exporter md_to_csv <input.md> <output.csv>
scripts/md-exporter md_to_pdf <input.md> <output.pdf>
scripts/md-exporter md_to_xlsx <input.md> <output.xlsx>
```

## Notes
- This skill intentionally excludes all other historical converters.
