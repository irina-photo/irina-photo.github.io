#!/bin/bash
cd ~/Documents/Irina_Site/_irina-photo.github.io
git add -A
git commit -m "Обновление сайта $(date '+%d.%m.%Y %H:%M')" 2>/dev/null || echo "Нечего обновлять"
git push && echo "✅ Сайт опубликован! Откроется через 1-2 минуты." || echo "❌ Ошибка публикации"
echo ""
echo "Нажми Enter чтобы закрыть..."
read
