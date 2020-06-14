from path import Path

d = Path('./')
files = d.walkfiles('*.jpg')

for file in files:
    file.remove()
