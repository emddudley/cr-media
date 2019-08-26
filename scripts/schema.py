"""
Validate data against schema.
"""

import json
from jsonschema import validate
from pathlib import Path


data_dir = Path(Path(__file__).parent, '..', '_data').resolve()

for schema_path in data_dir.glob('*.schema.json'):
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    data_path = Path(data_dir, schema_path.stem[:-len('.schema')] + '.json')

    with open(data_path, 'r') as f:
        data = json.load(f)

    print(f'Validating {data_path} against {schema_path}\n')
    validate(instance=data, schema=schema)
