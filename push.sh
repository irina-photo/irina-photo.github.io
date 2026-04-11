#!/bin/bash
cd "$(dirname "$0")"
git add -A
git commit -m "Обновление сайта $(date '+%d.%m.%Y %H:%M')"
git push
echo "✅ Сайт обновлён на GitHub!"
