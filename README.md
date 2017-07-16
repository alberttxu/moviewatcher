# moviewatcher
Inspired by David Mastronarde's framewatcher. moviewatcher monitors the current working directory for any files with the mrcs or tif/tiff extensions.

A quick example

1. Download this repository
2. Download an example unaligned micrograph stack from the Relion 2.1 tutorial test data
https://drive.google.com/uc?export=download&id=0BwXH3eSej0nHam5jZWNuOHlxeWc

3. ```./moviewatcher.py --command command_file.txt --dest done_folder```


### Usage: moviewatcher.py -c/--command COMMAND -d/--dest DEST

COMMAND  Command file for MotionCor2

DEST     is the directory to move each initial mrcs/tif file after MotionCor2 finishes processing it. A new folder will be created if DEST does not already exist.


### Command file syntax:

The syntax is sh shell with a few differences.

  - (filename)  is replaced with a discovered mrcs/tif file. e.g. *Falcon_2012_06_12-15_56_10_0_movie.mrcs*

  - (basename)  is the same as (filename) without the extension. e.g. *Falcon_2012_06_12-15_56_10_0_movie*

  - (dest)      is replaced with the --dest argument in the moviewatcher command. e.g. *done_folder*
