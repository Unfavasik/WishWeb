import sys

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    content = content.replace(
        'linear-gradient(to right, transparent, rgba(76, 29, 149, 0.3), rgba(76, 29, 149, 0.6))',
        'linear-gradient(to right, transparent, rgba(248, 6, 18, 0.15), rgba(248, 6, 18, 0.35))'
    )
    content = content.replace(
        'border: 1px solid rgba(167, 139, 250, 0.25);',
        'border: 1px solid rgba(248, 6, 18, 0.4);'
    )
    content = content.replace(
        'linear-gradient(to right, #a78bfa, #c084fc)',
        'linear-gradient(to right, #F80612, #ff4b4b)'
    )
    content = content.replace(
        'background-color: #8b5cf6;',
        'background-color: #F80612;'
    )

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

process_file('products/index.html')
