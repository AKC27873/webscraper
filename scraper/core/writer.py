import json
from datetime import datetime

def write_json(target, depth, pages, outfile):
    data = {
        "target": target, 
        "depth": depth,
        "timestamp": datetime.utcnow().isoformat(),
        "pages": pages
    }

    with open(outfile, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

