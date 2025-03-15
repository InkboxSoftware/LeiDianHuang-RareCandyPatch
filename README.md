# LeiDianHuang-RareCandyPatch
Rare Candy patch for 雷电皇：比卡丘 (Pokémon Yellow for the NES). 
This script works for both the original title and the English translation. 

### How to Patch
 - In the getRareCandy.py file change the input and output file names on lines 1 and 2
```
inputFilePath = 'pathToGameSave.sav'
outputFilePath = 'newPathToGameSave.sav'
```
If inputFilePath is equal to outputFilePath the file will be automatically overwritten.

 - Run the script via the command line:
```
py getRareCandy.py
```
