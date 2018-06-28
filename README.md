# TensorFlow Play ground
TensorFlow is an open source software library for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices. This project is a set of basic examples for learning TensorFlow. If you want to quickly learn the TensorFlow, follow the examples of this project.

##  Getting Started
TensorFlow is one of the many frameworks out there for you to learn more about Deep Learning. You can install TensorFlow on Windows and you wouldn’t be needing a Docker or any other virtual machines. Before you go on with the steps, make sure that your computer meets the requirements in order for TensorFlow to work on your computer.

### Requirement
- **TensorFlow only supports 64-bit Python 3.5.x on Windows**
- **pip3 package manager** (which is the program that you are going to need in order for you use to install TensorFlow on Windows)

### Installing TensorFlow on Windows 10

#### Step1:
Head over to  [Python 3.5.4 from python.org](https://www.python.org/downloads/release/python-354/)
#### Step2:
You will need to select either the x86-64 or amd64 installer.
The one I specifically recommend for now is the **Windows x86-64 executable installer**.
#### Step3:
After the download is complete, run it. choose **Add Python 3.5 to PATH**.
#### Step4:
Now you should be able to see a message saying **Setup was successful**.
A way to confirm that it has installed successfully is to open your Command Prompt and check the version.
Here's an example
```
C:\>python --version
Python 3.5.4
```
Great, you can now get onto installing TensorFlow with pip onto your Windows computer.
#### Step5:
To install TensorFlow, start a terminal.  Make sure that you run the cmd as an administrator!
Open up the Start menu, search for **cmd** and then right click on it and **Run as an administrator**.
#### Step6:
Now all you have to do is give just one simple little command for you to finish installing Tensorflow onto your Windows. 
Just enter this command:
```
C:\>pip3 install --upgrade tensorflow
```
Done! You’ll now notice to your top left hand corner with the command prompt saying ‘Administrator’ and that your installation completed successfully.
### Installing Spyder IDE 
I use spyder IDE for programming. if you want to use TensorFlow in spyder folow these steps.
#### Step1:
First install anaconda
Download Python3.6 version from [Anaconda windows installer](https://www.anaconda.com/download/)
#### Step2:
Anaconda has a really cool feature called ‘environments’ that allows more than version of Python to be installed in a different environments, each with different packages installed as you see fit.
To create the new environment called ‘tensorflow’ open up the Windows command prompt and type:
```
C:\>conda create -n tensorflow python=3.5 anaconda
```
#### Step3:
We can now start installing Spyder in the new environment. To do this, first activate the environment by typing the following into the command prompt:
```
C:\>activate tensorflow
```
The command prompt should now change to have a (tensorflow) at the beginning of each line. This indicates that we're working in the new tensorflow environment.
So we need to install Spyder within the new environment:
```
(tensorflow) C:\>conda install spyder
```
#### Step4:
Once spyder has been installed we can install the relevant packages. Again we need to be in the relevant environment, so type:
```
(tensorflow) C:\>conda install tensorflow
```
#### Step5:
Now you can use spyder for tensorflow. each time you want to use spyder, you should activate tensorflow and run spyder.
```
C:\>activate tensorflow
(tensorflow) C:\>spyder
```

