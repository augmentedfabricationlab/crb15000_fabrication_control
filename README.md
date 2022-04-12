# ABB crb15000 Simulation and Control Environment

**Quick links:** [compas docs](https://compas-dev.github.io/main/) | [compas_fab docs](https://gramaziokohler.github.io/compas_fab/latest/) | [compas_rrc_docs](https://compas-rrc.github.io/compas_rrc/latest/reference/index.html) | [rrc github repository](https://github.com/compas-rrc/compas_rrc) | [overview compas extensions](https://compas.dev/extensions.html) | [urdf and moveit tutorials](https://gramaziokohler.github.io/compas_fab/latest/examples/03_backends_ros/07_ros_create_urdf_ur5_with_measurement_tool.html) | [troubleshooting](#docker-troubleshooting)

## Requirements

* Operating System: **Windows 10 Pro** <sup>(1)</sup>.
* [Rhinoceros 3D 7.0](https://www.rhino3d.com/)
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* [Docker Community Edition](https://www.docker.com/get-started): Download it for [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows). Leave "switch Linux containers to Windows containers" disabled.
* X11 Server: On Windows use [XMing](https://sourceforge.net/projects/xming/), on Mac use [XQuartz](https://www.xquartz.org/) (see details [here](https://medium.com/@mreichelt/how-to-show-x11-windows-within-docker-on-mac-50759f4b65cb)).
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))
* [ABB RobotStudio](https://new.abb.com/products/robotics/robotstudio/downloads): 6.08 (only available for Windows). After install, **make sure you add the latest RobotWare, 6.12.00 or newer** (`Add-Ins` -> `RobotApps` -> `Filter for RobotWare` and add the version `6.12.00` or newer in the drop-down menu to the right). Please find further instructions for the installation [here](README_ROBOTSTUDIO.md).
* [VS Code](https://code.visualstudio.com/) with the following `Extensions`:
  * `Python` (official extension)
  * `EditorConfig for VS Code` (optional)
  * `Docker` (official extension, optional)
  * `RAPID ABB` (Syntax highligher for RAPID files in VS Code, optional)

<sup>(1): Windows 10 Home does not support running Docker.</sup>


## Dependencies

* [COMPAS RRC](https://github.com/compas-rrc/compas_rrc)


## Getting Started

### 1. Setting up the Anaconda environment with all dependencies

Execute the commands below in Anaconda Prompt:

#### Install Compas & Compas Fab
 
    (base) conda config --add channels conda-forge
    (base) conda create -n ffc compas_fab --yes
    (base) conda activate ffc

#### Install Compas RRC

    (ffc) conda install compas_rrc
    
#### Install on Rhino
    
    (ffc) python -m compas_rhino.install -v7.0
    
#### Verify Installation

    (ffc) pip show compas_fab
    
    Name: compas-fab
    Version: 0.XX.X
    Summary: Robotic fabrication package for the COMPAS Framework
    ....

    
### 2. Cloning and installing the repository

#### Repository Cloning

* Create a workspace directory: C:\Users\YOUR_USERNAME\workspace
* Open Github Desktop and clone the repository [this repository](https://github.com/augmentedfabricationlab/fabtory_fabrication_control) into you workspace folder.


### 3. Simulation & Control

#### Robot Artist

* Open the file [rhino/fabtory_artist.ghx](rhino/fabtory_artist.ghx) and load the robot model, you can then visualize the robot and move the axis and joints with forward kinematics.

#### Moveit Simulation Playground

* Once you opened the file [rhino/fabtory.3dm](rhino/fabtory_simulation.3dm) and [rhino/fabtory_simulation.ghx](rhino/fabtory_simulation.ghx) and loaded the robot model, you can start the Docker ROS moveit simulation environment and connect your ROS client to it.
* For starting the __Docker ROS moveit simulation environment__, go to VS code and start the docker containers by:
  * __Running Docker images__: Run the docker image for the moveit simulation [`docker/ros-systems/moveit_simulation/docker-compose.yml`](docker/ros-systems/moveit_simulation/docker-compose.yml) via 
    * right-click on the file `Compose-up` or 
    * type `docker-compose up -d` in the Terminal (cd to folder) to start it.
    * when ending, don't forget to stop the image via `docker-compose down -d`
* For access to the __web UI of the docker image__, start your browser and go to:<br/>
`http://localhost:8080/vnc.html?resize=scale&autoconnect=true`
* In Rhino, you can now __connect the ROS client to the rosbridge__ and query all moveit related services (compute_ik, trajectory planning, etc.)

#### Robotstudio Simulation & Control Playground

* Once you opened the file [rhino/fabtory.3dm](rhino/fabtory_simulation.3dm) and [rhino/fabtory_control.ghx](rhino/fabtory_control.ghx) and loaded the robot model, you can start the Docker ROS control environment and connect your ROS client to it.
* For starting the __Docker ROS control environment__, go to VS code and start the docker containers by:
  * __Running Docker images__: Run the docker image for the robot control [`docker/ros-systems/virtual_controller/docker-compose.yml`](docker/ros-systems/virtual_controller/docker-compose.yml) via 
    * right-click on the file `Compose-up` or 
    * type `docker-compose up -d` in the Terminal (cd to folder) to start it.
    * when ending, don't forget to stop the image via `docker-compose down -d`
* In Robotstudio, first, open the FlexPendat view Controller > FlexPendant > IRC5 FlexPendant, and then start the simulation via Simulation > Play
* For first testing, open and run the [tests/welcome_tum.py](tests/welcome_tum.py) file in VS Code
* In Grasshopper, you can now __connect the ROS client and the ABB client to the rosbridge__  and query all control related services (MoveToJoints, MoveToFrame, etc.)
