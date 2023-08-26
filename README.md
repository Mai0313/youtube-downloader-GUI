# youtube-downloader-GUI
It is a simple youtube downloader

## Build

```bash
pyinstaller --onefile --icon=src/youtube.ico --noconsole --distpath=./dist main.py
mv dist/main.exe youtube-downloader.exe
rm dist
rm -r build
```
