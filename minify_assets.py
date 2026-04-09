import re
import os

def minify_js(content):
    # Remove single-line comments
    content = re.sub(r'//.*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove extra whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r' ?([{};,:=+-><]) ?', r'\1', content)
    return content.strip()

def minify_css(content):
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove extra whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r' ?([{};,:]) ?', r'\1', content)
    # Remove last semicolon in blocks
    content = re.sub(r';}', '}', content)
    return content.strip()

assets = ['assets/style.css', 'assets/app.js', 'assets/tailwind.config.js']

for asset in assets:
    if os.path.exists(asset):
        with open(asset, 'r') as f:
            content = f.read()
        
        if asset.endswith('.js'):
            minified = minify_js(content)
        elif asset.endswith('.css'):
            minified = minify_css(content)
        
        with open(asset, 'w') as f:
            f.write(minified)
        print(f"Minified {asset}")
