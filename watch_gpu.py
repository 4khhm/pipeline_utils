
import sys, os, time
import subprocess

# -------------------------------------
# gnome watch gpu use, on off switches
# -------------------------------------
def on(): os.system("gnome-terminal --window-with-profile=gpu -x watch -n 1 nvidia-smi")
def off(): os.system("gnome-terminal -- killall watch -n 1 nvidia-smi") 