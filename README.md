# Transcodin

## Examples used

### Print tasks list:
```bash
python3 transcoding.py -t
```

### Create gif frame:
```bash
python3 transcoding.py -t gif-frame -i ./resources/24cbad87b8d4496acb.mp4 -o ./resources/test.gif -s 240x240 -ss 10 -d 10 -cf 10
```

### Key frame:
```bash
 python3 transcoding.py -t key-frame -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -o ./resources/test.jpg -s '240x240' -v=1 -ss 0
```

### Add overlay:
```bash
python3 transcoding.py -t overlay -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -io ./resources/png-2093542_960_720.png -o ./resources/test.mp4 -p '100:100'
```

### Create preview video:
```bash
python3 transcoding.py -t preview-video -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -o ./resources/test-2.mp4 -s '240x240' -v 1 -ss 0 -cf 25 -d 10 -v 250
```

### Transcoding mov to mp4:
```bash
python3 transcoding.py -t transcoding -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -o ./resources/test-3.mp4
```

### Create multi bitrate video:
```bash
python3 transcoding.py -t multi-bitrate -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -o ./resources/test-4.mp4 -s '240:480:720'
```

## Полезные ссылки

* [Erlyvideo. Транскодирование файлов](https://erlyvideo.ru/doc/vod-veschanie-faylov/transkodirovanie-faylov)
* [Конвертация видео и настройка сервера (HLS, DASH и MP4) - Помощь - PlayerJS - Конструктор видео и аудио плееров.pdf](https://yadi.sk/i/xLq_mcUFRkIX0Q)
* [Пример на php](https://yadi.sk/d/NZPdXNoVHPjEfA)