# Motivation


With the 2020 global pandemic we now have to take our classes online, which depending on your setup at home, is fine. But the coolest part about it, is that if the professor so desires, he can record the class and people that couldn't attend, can watch it later on.

Imagine this scenario: Student A misses a class, which is unfortunate, but thankfully they aren't out of luck. They head to their professor's website where, fortunately, their professor uploaded a video of the lecture. Unfortunate for them though, they are forced to watch it in browser. They also can't download the video and are forced to watch it at 1x speed. This makes it tough for someone who might be trying to find the couple of slides they missed without watching the entire lecture back.

So what's student A to do? Suffer through the endless class at normal speed? Nope! The class is already recorded, so there's no reason for that other *~than professor doesn't feel like uploading standard video files~* (Or maybe he doesn't want to put a strain on his server, making people have to Download the entire video, and maybe just watch a couple minutes of it. If that's the case, I sure made the server work a lot during the writing of this tool. Whooooops ¯\\(ツ)/¯)

Student A could just use a tool that downloads all the files, and converts it into a standard .mp4 file. This way they are able to use a video player with speed control (I recommend my personal favorite; VLC Player for up to 4x speed)

This is that tool. With it you only need to know the passwords to their Professor's websites. It'll save you precious time! You're welcome ;)

# Installation 
## Windows

The easiest way to install this tool is by using Conda

[Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Once you install it, you should be able to launch a Anaconda poweshell from the Windows menu. Enter on the terminal these commands in order

    git clone https://github.com/damianvaz/classDown.git
    cd classDown
    conda env create -f environment.yml
    conda activate classDown
    python classDown.py

## Linux

### Debian Systems

Here we have a couple options. You can use conda, or just python 3.8 or higher
But first let's install git if you don't already have it:
Enter on the terminal `sudo apt install git`

Now Download the files of this repository by entering `git clone https://github.com/damianvaz/classDown.git`

#### Miniconda route

Download the latest install of miniconda by entering on the terminal:

`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

Run the installer:

`bash Miniconda3-latest-Linux-x86_64.sh`

Now run these commands in order

    cd classDown
    conda env create -f environment.yml
    conda activate classDown


and run the script 

`python classDown.py`

#### Python pip install route

If you don't have python 3.8 or higher

`sudo apt install python3.8`

If you already have python 3.8 or higher:

Now install ffmpeg:

`sudo apt install ffmpeg`

`cd classDown`

`pip install -r requirements.txt`

now just run the script:

`python3 classDown.py`
-
or if you only have one version of python installed:

`python classDown.py`

# After thoughts

If you run in trouble installing contact me through whatsapp

