# Motivation

With the 2020 global pandemic we now have to take our classes online, which depending on your setup at home, is fine.
But the coolest part about it, is that if the professor so desires, he can record the class and people that couldn't attend, can watch it later on.

But imagine this scenario: Student A misses class, and so he goes to the Professor's website to watch it. 
There he manages to watch the class in a browser, however he can't download it, and even worse he has to watch it at 1x speed as the professor PAINFULLY and slowly reads from a slide, that he may or may not, have wrote it.

So what's student A to do? Suffer through the endless class at normal speed? Nope! 
The class is already recorded, so there's no reason for that other than *~professor doesn't feel like uploading standard video files~* (Or maybe he doesn't want to put a strain on his server, making people have to Download the entire video, and maybe just watch a couple minutes of it. If that's the case, I sure made the server work a lot during the writing of this tool. Whooooops ¯\\_(ツ)_/¯) 

So student A, creates a tool that downloads all the files, and converts it into a standard .mp4 file, that he can watch it in a video player with control speed (VLC player is super cool!), so he manages to watch it all up to 4x faster!

This is that tool. With it you only need to know the passwords to his websites, and you can save your precious time!
You're welcome! And if you find it useful, next time we meet, coffee is on you ;)

# Instalation

## Windows

The easiest way to install this tool is by using Conda

[Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Once you install it, you should be able to launch a Anaconda poweshell from the Windows menu

    git clone https://github.com/damianvaz/classDown.git
    cd classDown
    conda env create -f environment.yml

Now just run `python classDown.py`

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

Now let's make the new environment for the tool with
`cd classDown`
`conda env create -f environment.yml`

and run the script ´python classDown.py´

#### Python pip install route

If you don't have python 3.8 or higher

`sudo apt install python3.8`

If you already have python 3.8 or higher:
`cd classDown`
`pip install -r requirements.txt`

now just run the script:

`python3 classDown`

# After thoughts

If you run in trouble installing contact me through whatsapp

