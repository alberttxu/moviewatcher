#!/usr/bin/env python
import os
from os.path import getsize
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# watch for files with the following extensions
done_folder = "Cor"
extensions = [".tif", ".mrc"]

with open("command.txt") as commandfile:
    #lines = infile.read().splitlines()
    unparsed_command = " ".join(line.strip() for line in commandfile)

def parse_command(filename):
    # read parameters from file
    basename, ext = os.path.splitext(filename)
    command = unparsed_command.replace("(filename)", filename).replace("(basename)", basename)
    return command

def run_command(cmd):
    subprocess.call(cmd, shell=True)

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
        print filename
        run_command(parse_command(filename))
        run_command("mv %s %s" % (filename, done_folder))

class Handler(PatternMatchingEventHandler):
    patterns = ["*%s" % ext for ext in extensions]

    def on_created(self, event):
        process_file(event.src_path)


if __name__ == "__main__":
    for filename in os.listdir("."):
        process_file(filename)

    observer = Observer()
    observer.schedule(Handler(), path=".")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
