import json

with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        src = ''.join(cell['source'])
        if 'Pertanyaan Bisnis' in src or 'Apakah' in src or 'Conclusion' in src:
            print(f'=== Cell {i} ===')
            print(src[:400])
            print()
