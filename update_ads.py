import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/a3e3860b8f453e1b1ddf9c8a8d57af79"></script>
<script data-cfasync="false" src="https://bauval.org/14/9ec7f4deedc109808367a910ceb09cdb"></script>
<script>
  atOptions = {
    'key' : '52eda60128d9b3f742594c66f105cb29',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/52eda60128d9b3f742594c66f105cb29"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-a3e3860b8f453e1b1ddf9c8a8d57af79"></div>
</div>'''

files = ['index.html', 'characters.html', 'tierlist.html', 'combos.html', 'story.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '52eda60128d9b3f742594c66f105cb29' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-a3e3860b8f453e1b1ddf9c8a8d57af79' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')