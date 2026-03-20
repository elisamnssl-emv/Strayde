import os
import shutil
import re
import time
import sys

def build():
    start_time = time.time()
    
    # Configuration
    DIST_DIR = 'dist'
    PAGES_DIR = 'pages'
    FRAGMENTS_DIR = 'fragments'
    ASSETS_DIR = 'assets'
    
    # Ensure dist exists
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)
    
    # Load fragments
    try:
        with open(f'{FRAGMENTS_DIR}/head.html', 'r', encoding='utf-8') as f:
            head_frag = f.read()
        with open(f'{FRAGMENTS_DIR}/header.html', 'r', encoding='utf-8') as f:
            header_frag = f.read()
        with open(f'{FRAGMENTS_DIR}/footer.html', 'r', encoding='utf-8') as f:
            footer_frag = f.read()
    except FileNotFoundError as e:
        print(f"Erreur: Fragment manquant - {e}")
        return

    # Process pages
    for filename in os.listdir(PAGES_DIR):
        if filename.endswith('.html'):
            with open(f'{PAGES_DIR}/{filename}', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata
            meta_match = re.search(r'<!--\s*(.*?)\s*-->', content, re.DOTALL)
            metadata = {}
            if meta_match:
                meta_text = meta_match.group(1)
                for line in meta_text.split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        metadata[k.strip().lower()] = v.strip()
                
                # Remove meta comment from main content
                main_content = content.replace(meta_match.group(0), '').strip()
            else:
                main_content = content
            
            # Replace tokens in head
            title = metadata.get('title', 'Strayde — La plateforme tout-en-un pour organiser vos événements sportifs')
            description = metadata.get('description', 'Inscriptions, bénévoles, communication, administratif : Strayde est la plateforme 360° qui accompagne les organisateurs d\'événements sportifs outdoor de A à Z.')
            
            page_head = head_frag.replace('{{title}}', title).replace('{{description}}', description)
            
            # Assemble page
            full_html = f"<!DOCTYPE html>\n<html lang='fr'>\n<head>\n{page_head}\n</head>\n<body class='font-body antialiased'>\n{header_frag}\n<main>\n{main_content}\n</main>\n{footer_frag}\n</body>\n</html>"
            
            # Write to dist
            with open(f'{DIST_DIR}/{filename}', 'w', encoding='utf-8') as f:
                f.write(full_html)
            
            print(f"✔ Page générée: {filename}")

    # Copy assets
    if os.path.exists(ASSETS_DIR):
        shutil.copytree(ASSETS_DIR, f'{DIST_DIR}/assets', dirs_exist_ok=True)
        print("✔ Assets copiés")

    end_time = time.time()
    print(f"✨ Build terminé en {end_time - start_time:.3f}s")

if __name__ == "__main__":
    build()
