# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON

This repository has all the code used as part of the 2022-01 OOP class offered at Universidad del Norte


## How to use this repo

To use this repo you need to following pre-requisites:

- Install Docker on your machine. [link](https://docs.docker.com/get-docker/) 
    - Check a small [introduction](https://www.youtube.com/watch?v=_dfLOzuIg2o) to Docker so you are somewhat familiar to what it is. You do no need to worry about technical details of Docker at the moment since I am providing everything ready to go for you. 
- Install VSCode. [link](https://code.visualstudio.com/download). VSCode is a free IDE that is very popular to this day with tons of feature a very lightweight. 
- Install the Remote-Containers extension [link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). This extension is required to use the Docker image I created for our use during this course.
- Download or clone this repository
- Open this repository folder on VScode
- - Press `CTRL + Shift + P`. A Menu on the top part of VSCode will appear. Type `Remote-Containers: Open Workspace in Container`. Select the file `oop_202201.code-workspace` and this will start the process of opening this repo inside a container.
    - At this moment VScode will automatically download the latest Docker image. This will take a while depending on your local connection since it is about 1.12GB
    - After the download is complete a process that starts the container will kick in. This process may take a while and depends on your local resources. **PLEASE CLOSE ALL WINDOWS IN YOUR COMPUTER TO FREE-UP RESOURCES FOR THIS PROCESS**
    - After the container starts you will see a VSCode window that opened inside a container. This container is running a different OS than your local one and it is based on Ubuntu Linux. Your work inside the repo is safe but teh work in other directories in the repo will be lost when you close the connection or kill the running container. 

## Support Material

We will be using material from several places, but mostly the material created by the authors of our main textbook. The code can be found in this [link](https://github.com/PacktPublishing/Python-Object-Oriented-Programming---4th-edition). Portions of such code will be available in this repo with the proper attributions and modifications. 

## Remote Development Environment on Cloud

### Azure setup and VM

- Open an [Azure Student Account](https://azure.microsoft.com/en-us/free/students/) using your Uninorte email. This will give you 100 USD in credits
- Start a VM with 2 Cores and 4GB of RAM. If possible select `Standard_B2s`, this specific VM has those characteristics and cost about ~0.04USD/hour. We will cover how to do this in class. We will use Ubuntu 20.04. Here some [instructions](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal) for you to peek
- Connect to the VM using SSH. If you are in windows you will need to use a [compatible SSH client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client). if you are in Ubuntu you are all set. the command you will need to run is something like this `ssh oopclass@10.1.1.1`. In this command oopclass is the user that was created during the VM creation and the IP is assigned automatically by Azure.
- Install Docker and Git **inside the VM**
    - [Docker instructions](https://docs.docker.com/engine/install/ubuntu/)
    - [Git Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Add current users to sudoers to use Docker as current user **inside the VM**
    - `sudo groupadd docker`
    - `sudo usermod -aG docker $USER`
    - `newgrp docker`
    - Check that you everything is ok by running `docker run hello-world`
    - **Turn off** the VM for the changes to have effect and **Turn on** again
- *Optional*
    - If you want to login on Github and you have two factor authentication enabled you need to first
        - [Generate a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
        - Run this command so your Git credentials are stored `git config --global credential.helper store`
- Clone our course repository on /home/$USER **inside the VM**. `git clone https://github.com/jdposada/oop_202201.git`
    - *Optional*
        - You could decide to [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the main repo so you have minor changes and other files in it. If that is the case you could keep it private. If you made this decision you should clone your fork instead of the class repo. Keep in mind you need to [keep your fork updated](https://stackoverflow.com/questions/39819441/keeping-a-fork-up-to-date)

### Locally

- On your **local** VSCode instance the following extension need to be installed
    -  [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- Here some summary on the instructions [here](https://code.visualstudio.com/docs/remote/ssh) to connect to our VM using SSH through VS Code. Press `CTRL + Shift + P` and:
    - Type `Remote-SSH: Connect to Host`
    - Select `Add New SSH host`
    - Type in your user and IP from the VM. It should be something like this `oopclass@10.1.1.1`. The user (oopclass) was created during the VM creation and the IP is assigned automatically by Azure.
    - Type the password that was defined during the creation of the VM.
- Now your VS Code should be connected to the VM. Now you should open the workspace inside the container.
    - Press `CTRL + Shift + P`. A Menu on the top part of VSCode will appear. Type `Remote-Containers: Open Workspace in Container`. Select the file `oop_202201.code-workspace` and this will start the process of opening this repo inside a container.
