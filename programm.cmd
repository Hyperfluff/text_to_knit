@echo on

python vorformatierung.py
del input.txt
ren input1.txt input.txt

python convert.py

python imagegenerator.py
del outputimage.txt

mkdir output
move output.txt output/output.txt
move output.png output/output.png

exit