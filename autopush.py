#!/usr/bin/env python3
import os, time, subprocess, hashlib

folder = os.path.dirname(os.path.abspath(__file__))

def get_hash():
    h = ""
    for f in sorted(os.listdir(folder)):
        if f.endswith(('.html','.css','.js','.json')):
            try:
                h += str(os.path.getmtime(os.path.join(folder, f)))
            except: pass
    return h

last = get_hash()
print("👀 Слежу за изменениями... (Ctrl+C чтобы остановить)")

while True:
    time.sleep(5)
    current = get_hash()
    if current != last:
        last = current
        print("📤 Изменения найдены, публикую...")
        subprocess.run(['git','-C',folder,'add','-A'])
        subprocess.run(['git','-C',folder,'commit','-m','автообновление'])
        result = subprocess.run(['git','-C',folder,'push'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Опубликовано!")
        else:
            print("❌ Ошибка:", result.stderr[:100])
