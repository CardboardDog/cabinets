pyinstaller -F src/main.py -n cabinets --add-data="./data/*:." --icon=data/icon.png
rm -rf build
rm *.spec
mv dist/cabinets ./cabinets
rm -rf dist
