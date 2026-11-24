from pathlib import Path

LINE = "My LiDAR mapped that crumb pile for 72 hours, matched its motion log to yours on the couch, and classified it as a second homeowner."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
