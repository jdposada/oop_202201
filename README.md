# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON

This repository has all the code used as part of the 2022-01 OOP class offered at Universidad del Norte


## How to use this repo

To use this repo you need to following pre-requisites:

- Install Docker on your machine. [link](https://docs.docker.com/get-docker/) 
    - Check a small [introduction](https://www.youtube.com/watch?v=_dfLOzuIg2o) to Docker so you are somewhat familiar to what it is. You do no need to worry about technical details of Docker at the moment since I am providing everything ready to go for you. 
- Install VSCode. [link](https://code.visualstudio.com/download). VSCode is a free IDE that is very popular to this day with to9ns of feature a very lightweight. 
- Install the Remote-Containers extension [link] (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). This extension is required to use the Docker image I created for our use during this course.
- Download or clone this repository
- Open this repository folder on VScode
- Press `CTRL + Shift + P`. A Menu on the top part of VSCode will appear. Type `Remote-Containers: Open Workspace in Container`. This will start the process of opening this repo inside a container.
    - At this moment VScode will automatically download the latest Docker image. This will take a while depending on your local connection since it is about 1.12GB
    - After the download is complete a process that starts the container will kick in. This process may take a while and depends on your local resources. **PLEASE CLOSE ALL WINDOWS IN YOUR COMPUTER TO FREE-UP RESOURCES FOR THIS PROCESS GOES SMOOTHLY**
    - After the container starts you will see a VSCode window that opened inside a container. This container is running a different OS than your local one and it is based on Ubuntu Linux. Your work inside the repo is safe but teh work in other directories in the repo will be lost when you close the connection or kill the running container. 

## Support Material

We will be using material from several places, but mostly the material created by the authors of our main textbook. The code can be found in this [link](https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition). Portions of such code will be available in this repo with the proper attributions and modifications. 
