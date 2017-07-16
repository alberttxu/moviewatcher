# moviewatcher
Inspired by David Mastronarde's framewatcher. moviewatcher monitors the current working directory for any files with the mrcs or tif/tiff extensions. While moviewatcher is running, any new files that appear in the running directory will automatically be processed by a command specified in a command file.


### Requirements
1. Python
2. The Python package, Watchdog
```
pip install watchdog
```


### Getting Started

1. Download the repository and cd into it.
```
git clone https://github.com/alberttxu/moviewatcher
cd moviewatcher
```
2. Download an example unaligned micrograph stack from the Relion 2.1 tutorial test data; https://drive.google.com/uc?export=download&id=0BwXH3eSej0nHam5jZWNuOHlxeWc

3. Start moviewatcher. Done. The original movie and all the output files will end up in *done_folder*.
```
./moviewatcher --command command_file.txt --dest done_folder
```
Add moviewatcher anywhere in your PATH to install.
```
sudo mv moviewatcher /usr/local/bin
```


### Usage: moviewatcher.py -c/--command COMMAND -d/--dest DEST
#### Warning! Do not make DEST the same as the current working directory. This will cause an infinite loop.

COMMAND  Command file for MotionCor2

DEST     is the directory to move each initial mrcs/tif file after MotionCor2 finishes processing it. A new folder will be created if DEST does not already exist.

### Command file syntax:

The syntax is sh shell with a few differences. Multiple lines are joined together with spaces. To add comments, use *#* as the first non-whitespace character of a line.

  - (filename)  is replaced with a discovered mrcs/tif file. e.g. *Falcon_2012_06_12-15_56_10_0_movie.mrcs*

  - (basename)  is the same as (filename) without the extension. e.g. *Falcon_2012_06_12-15_56_10_0_movie*

  - (dest)      is replaced with the --dest argument in the moviewatcher command. e.g. *done_folder*


### Tips
  - If you just want to move the raw files without processing, leave the command file blank.
  - The MotionCor2 output files don't have to go in the same folder as the DEST folder for the original data.
  - You can use other programs to align such as Unblur and alignframes.
