#!/usr/bin/env python

### Customize
# watch for files with the following extensions
extensions = [".tif", ".tiff", ".mrcs"]
###

import argparse
import os
from os.path import getsize
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

### globals
parser = argparse.ArgumentParser(description="")
parser.add_argument("-c", "--command",
                    help="command file",
                    required=True
                    )
parser.add_argument("-d", "--dest",
                    help="destination folder of processed files",
                    required=True
                    )
args = vars(parser.parse_args())
dest_dir = args["dest"]
if dest_dir[-1] == "/":
    dest_dir = dest_dir[:-1]
with open(args["command"]) as commandfile:
    unparsed_command = " ".join(line.strip() for line in commandfile
                                              if line.strip()[0] != "#")
###

### helper functions
def parse_commandfile(filename):
    # read parameters from file
    basename, ext = os.path.splitext(filename)
    command = unparsed_command.replace("(filename)", filename)
    command = command.replace("(basename)", basename)
    command = command.replace("(dest)", dest_dir)
    return command

def run_command(cmd):
    return subprocess.call(cmd, shell=True)

def wait_until_done_growing(filename):
    size = getsize(filename)
    time.sleep(1)
    while getsize(filename) - size:
        size = getsize(filename)
        time.sleep(1)

def process_file(filename):
    if filename[:2] == "./":
        filename = filename[2:]
    ext = os.path.splitext(filename)[1]
    if ext in extensions:
        wait_until_done_growing(filename)
        start = time.time()
        print "started processing %s" % filename
        if run_command(parse_commandfile(filename)):
            print "Error from command file, exiting..."
            raise KeyboardInterrupt
        else:
            end = time.time()
            print "finished processing %s in %.3f s" % (filename, end - start)
            print "moving %s to %s" % (filename, dest_dir)
            run_command("mv %s %s" % (filename, dest_dir))
###

# watchdog handler
class Handler(PatternMatchingEventHandler):
    patterns = ["*%s" % ext for ext in extensions]

    def on_created(self, event):
        process_file(event.src_path)


def main():
    if not os.path.isdir(dest_dir):
        print "directory %s does not exist" % dest_dir
        print "creating directory %s" % dest_dir
        if run_command("mkdir %s" % dest_dir):
            print "error creating directory"
            sys.exit()
    print "destination folder: %s" % dest_dir

    # process existing files in current working directory
    for filename in os.listdir("."):
        process_file(filename)

    # watchdog
    observer = Observer()
    observer.schedule(Handler(), path=".")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()

if __name__ == "__main__":
    main()
