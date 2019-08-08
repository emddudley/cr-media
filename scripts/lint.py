"""
Normalize the data files.
"""

import json
from pathlib import Path


data_dir = Path(Path(__file__).parent, '..', '_data').resolve()

for data_path in data_dir.glob('*.json'):
    print(f'Normalizing {data_path}')

    with open(data_path, 'r') as f:
        data_json = json.load(f)

    with open(data_path, 'w') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=2, sort_keys=True)
