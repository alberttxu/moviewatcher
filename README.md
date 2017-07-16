# moviewatcher
Inspired by David Mastronarde's framewatcher.

moviewatcher monitors the current working directory for any files with the mrcs or tif/tiff extensions.

Download an example unaligned micrograph stack from the Relion 2.1 tutorial test data
https://drive.google.com/uc?export=download&id=0BwXH3eSej0nHam5jZWNuOHlxeWc

Usage: moviewatcher.py -c/--command COMMAND -d/--dest DEST
COMMAND  Command file for MotionCor2
DEST     Directory to move each initial mrcs/tif file after MotionCor2 finishes processing it. A new folder will be created if DEST does not already exist.

./moviewatcher.py --command command_file.txt --dest done_folder 

Command file syntax:
The syntax is sh shell with a few differences.
(filename)  is replaced with a discovered mrcs/tif file. e.g. Falcon_2012_06_12-15_56_10_0_movie.mrcs
(basename)  same as (filename) minus the extension. e.g. Falcon_2012_06_12-15_56_10_0_movie
(dest)      is replaced with the --dest argument in the moviewatcher command. e.g. done_folder
