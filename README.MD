# SOC Security Dashboard

A Security Operations Center dashboard that visualizes file integrity 
monitoring logs in real time using Flask and Plotly.

---

## Features
- Visualizes security events from File Integrity Checker
- Bar chart showing event frequency by type
- Timeline chart showing when events occurred
- Color coded event table with last 20 alerts
- Summary cards for quick threat overview

---

## Security Events Tracked
| Event | Color | Description |
|-------|-------|-------------|
| MODIFIED | Orange | File content changed |
| DELETED | Red | File removed |
| NEW FILE | Blue | Unknown file added |
| RENAMED | Purple | File identity changed |

---

## Built With
- Python 3.13
- Flask - web framework
- Plotly - interactive charts

---

## How to Run
1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Run File Integrity Checker first to generate logs
4. Run the dashboard:
   python app.py
5. Open browser at http://127.0.0.1:5000

---

## Technical Challenge Solved
Parsing unstructured log files into structured data for visualization.
Each log line is parsed by event type, timestamp and message then 
fed into Plotly charts with color coded markers per event type.

---

## Part of a Larger System
This dashboard connects directly to the File Integrity Checker project.
Together they form a complete file monitoring and visualization pipeline.