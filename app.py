import os
import json
import logging
from datetime import datetime
from flask import Flask, render_template
import plotly
import plotly.graph_objects as go 


# -- Config --
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
app       = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
LOG_FILE  = os.path.join(BASE_DIR, "..", "Projects5", "integrity.log")

#-- Parse Log -- 
def parse_log():
    events = []

    if not os.path.exists(LOG_FILE):
        return events
        
    with open(LOG_FILE, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            if "[MODIFIED]" in line:
                event_type = "MODIFIED"
            elif "[DELETED]" in line:
                event_type = "DELETED"
            elif "[NEW FILE]" in line:
                event_type = "NEW FILE"
            elif "[RENAMED]" in line:
                event_type = "RENAMED"
            else:
                continue

            events.append({
                "timestamp": line.split(" — ")[0].strip(),
                "type":      event_type,
                "message":   line.split(" — ")[1].strip() if " — " in line else line
            })

    return events


# -- Build Charts --
def build_charts(events):
    counts = {"MODIFIED": 0, "DELETED": 0, "NEW FILE": 0, "RENAMED": 0}
    for event in events:
        if event["type"] in counts:
            counts[event["type"]] += 1

    COLOR_MAP = {
        "MODIFIED": "#e67e22",
        "DELETED":  "#e74c3c",
        "NEW FILE": "#3498db",
        "RENAMED":  "#9b59b6"
    }

    # Bar chart
    bar = go.Figure(go.Bar(
        x=list(counts.keys()),
        y=list(counts.values()),
        marker_color=[COLOR_MAP[k] for k in counts.keys()]
    ))
    bar.update_layout(
        title="Security Events by Type",
        xaxis_title="Event Type",
        yaxis_title="Count",
        plot_bgcolor="#1a1a2e",
        font_color="#ffffff",
        height=400
    )

    # Timeline chart
    timestamps = [e["timestamp"] for e in events]
    types      = [e["type"] for e in events]
    colors     = [COLOR_MAP.get(e["type"], "#ffffff") for e in events]

    timeline = go.Figure(go.Scatter(
        x=timestamps,
        y=types,
        mode="markers",
        marker=dict(size=10, color=colors)
    ))
    timeline.update_layout(
        title="Security Event Timeline",
        xaxis_title="Time",
        yaxis_title="Event Type",
        plot_bgcolor="#1a1a2e",
        font_color="#ffffff",
        height=400
    )

    return (
        json.dumps(bar,      cls=plotly.utils.PlotlyJSONEncoder),
        json.dumps(timeline, cls=plotly.utils.PlotlyJSONEncoder)
    )

#-- Routes --
@app.route("/")
def index():
    events = parse_log()
    bar_chart, timeline_chart = build_charts(events)

    total     = len(events)
    modified  = sum(1 for e in events if e["type"] == "MODIFIED")
    deleted   = sum(1 for e in events if e["type"] == "DELETED")
    new_files = sum(1 for e in events if e["type"] == "NEW FILE")
    renamed   = sum(1 for e in events if e["type"] == "RENAMED")

    return render_template(
        "index.html",
        events    = events[-20:],
        bar_chart = bar_chart,
        timeline_chart = timeline_chart,
        total = total,
        modified = modified,
        deleted = deleted,
        new_files = new_files,
        renamed = renamed,
        generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

#-- Run --
if __name__ == "__main__":
    app.run(debug=True)
