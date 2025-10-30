import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace image extensions
    content = re.sub(r'(imagenes_hospedaje[\\/][^"\'\.]+)\.(jpeg|jpg|png)', r'\1.webp', content, flags=re.IGNORECASE)

    # Add lazy loading for images inside the gallery
    def add_lazy(m):
        gallery_html = m.group(1)
        gallery_html = re.sub(r'<img(?![^>]*loading="lazy")', r'<img loading="lazy"', gallery_html)
        return '<div class="gallery">' + gallery_html + '</div>'

    content = re.sub(r'<div class="gallery">(.*?)</div>', add_lazy, content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html successfully updated.")

if __name__ == '__main__':
    update_html()
