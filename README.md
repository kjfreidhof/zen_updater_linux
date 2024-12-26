# Zen updater Script for Linux

# Reason for creation

I wanted a simple universal way to update the zen browser in linux that automated the proccess. Therefore the Zen updater script was born. 

## What is there and what is this? 
There are two versions of this script the x64 version and the arm64 version. Choose the one that is correct for the archietecture you are using. This is a shell script that uses a python program in conjunction to update the browser. The python script will download the web browser. And then shell script will simply perform the update in the background. This shows no output upon doing the update. So if you get no ooutput and shell prompt in return then that means this worked. If doesnt then there is something wrong with script.  

## What do you need to use this

- git 

- python3-wget

This are the pieces of software that are used with this script. Git obivously to clone the repo and use it. 
And python3-wget is a python library that is used to download the zen tarball from the zen github repo. 

## How use this script.
- clone the repo

- Then copy the correct files to /usr/local/bin
`cp browser.py /usr/local/bin && cp zen_updater /usr/local/bin`
- What i usally do is create a directory in my downloads directory called zen.
`mkdir -p /home/user/Downloads/zen`

- Then i change to that path 
`cd /home/user/Downloads/zen`

- Then run 
`zen_updater`

* Just to note this will download the tarball to the current directory so you might want to create a directory to store all the tarballs in*


