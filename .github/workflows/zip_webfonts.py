import os
from fontTools.ttLib import TTFont

for folder in ['LXGWBright', 'LXGWBrightGB', 'LXGWBrightTC']:
    for file in os.listdir(folder):
        if file.lower().endswith('.ttf'):
            print(f"Converting {file}")
            fullpath = os.path.join(folder, file)
            filename, ext = os.path.splitext(fullpath)

            ttfont = TTFont(fullpath)
            ttfont.flavor = 'woff'
            ttfont.save(filename + '.woff')
            ttfont.flavor = 'woff2'
            ttfont.save(filename + '.woff2')