# SOC Security Dashboard

A Security Operations Center dashboard that visualizes file integrity
monitoring logs in real time using Flask and Plotly.

Designed to work alongside the
[File Integrity Checker](https://github.com/JeanMrc/file-integrity-checker)
project — together they form a complete file monitoring and visualization
pipeline.

---

## Features

- Visualizes security events from File Integrity Checker
- Auto refreshes every 30 seconds — always shows latest events
- Bar chart showing event frequency by type
- Timeline chart showing when events occurred
- Color coded event table with last 20 alerts
- Summary cards for quick threat overview
- Configurable log file path via environment variable

---

## Security Events Tracked

| Event    | Color  | Description            |
|----------|--------|------------------------|
| MODIFIED | Orange | File content changed   |
| DELETED  | Red    | File removed           |
| NEW FILE | Blue   | Unknown file added     |
| RENAMED  | Purple | File identity changed  |

---

## Built With

- Python 3.13
- Flask - web framework
- Plotly - interactive charts

---

## How to Run

1. Clone both repos into the same parent directory
projects/
├── file-integrity-checker/
└── soc-security-dashboard/

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run File Integrity Checker first to generate logs
```bash
   cd ../file-integrity-checker
   python integrity_checker.py
```

4. Run the dashboard
```bash
   cd ../soc-security-dashboard
   python app.py
```

5. Open browser at `http://127.0.0.1:5000`

---

## Custom Log File Path

By default the dashboard reads logs from:
../file-integrity-checker/integrity.log

To use a different path set the `LOG_FILE` environment variable:
```bash
LOG_FILE=/path/to/your/integrity.log python app.py
```

---

## Technical Challenge Solved

Parsing unstructured log files into structured data for visualization.
Each log line is parsed by event type, timestamp and message then
fed into Plotly charts with color coded markers per event type.

CSS class names cannot contain spaces so event types like NEW FILE
are normalized to NEW-FILE using Jinja2's replace filter before
being applied as HTML classes.

---

## Part of a Larger System

This dashboard connects directly to the
[File Integrity Checker](https://github.com/JeanMrc/file-integrity-checker).
Run both projects together for a complete file monitoring and
visualization pipeline.
