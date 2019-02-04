First, it is a good idea to create a directory for the virtual environment outside of where your project lives. In this example, we have an envs directory on the Desktop. This directory will hold any virtual environment configurations we decide to make. Let’s create a new directory within envs for CST 205 and call it cst205env. In other words, our current directory structure is:

~/dev/envs/cst205env

Important Note:  venv is sensitive to folders with spaces. If you put your envs directory elsewhere, make sure the path to it does not contain folders with spaces or you will get errors. (Ref)

#Creation

To create a virtual environment, navigate into the envs directory

    cd envs

and then execute:

    # Mac
    python3.7 -m venv cst205env

#Activation

The next step is to activate the virtual environment. From within your envs directory:

    # Mac
    source cst205env/bin/activate

You should notice the name of the newly-activated environment in your terminal emulator application.

#Alias

Create an alias to make activation easier

    proj=cst205
    mkdir ~/dev/$proj
    alias ${proj}env="source ~/dev/envs/$proj/bin/activate;cd ~/dev/$proj"

and add to ~/.bash_profile

    alias ${proj}env >> ~/.bash_profile
