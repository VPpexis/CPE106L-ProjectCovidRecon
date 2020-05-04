# COVIDRecon
![GitHub Logo](https://github.com/VPpexis/CPE106L-ProjectCovidRecon/blob/master/Images/logo-github.jpg) <br />

### Project Members

    1. Cinco, Cedrick
    2. Baek, Seungyoon 
    3. Directo, Claudee Khiarra 
    4. Navarro, Laurence Kobe
    5. Panugan, Van Philip
    6. Tipan, Ivan Patrick

## Table of Contents

- [Overview](#overview) <br />
  - [Purpose](#purpose) <br />
- [Introduction](#introduction) <br />
  - [Scope](#scope) <br />
  - [Requirements](#requirements) <br />
  - [Definitions] (definitions-acronyms-and-abbreviations)
 - [Target Audience](#target-audience) <br />
 - [Focus Areas](#focus-areas) <br />
    - [Scenarios](#scenarios) <br />
    - [Languages](#languages) <br />
 - [User Stories](#user-stories) <br />
 - [System Architecture](#system-architecture) <br />
  - [User Stories](#user-stories) <br />
 - [Sample Screenshots](#sample-screenshots) <br />

## Overview
Project-CovidRecon is a software application based from PyQt5 and Tweepy that tracks statuses of the number of Coronavirus Disease 2019 in National Captional Region in the Philippines. Through data science and mathematical models, the cases can be predicted and visualized through charts and tables. The application also provides prediction to the number of cases in the next days through logarithmic and exponential plotting.

## Purpose
The purpose of the program is as follows:
* To gather COVID-19 data cases and its location
* To visualize the data into charts.
* To predict the logarithmic and exponential pattern
* To show the geographical status of each province.

# Introduction
Data Science and mathematical models can help in shedding light on the evolution of the novel Coronavirus pandemic. By predicting, visualizing, and analyzing the virus, we will be able to put up an immunity against it through the help of data and information. This is an application that can forecast real-time COVID-19 data that can fill the gap between users and various sources of information in order to produce reliable data.  As the world plunged into a pandemic caused by COVID-19, both technology and medical field tries to understand how the virus had spread exponentially across the globe as well as on how to cure it. As people get wary about the health implications this pandemic poses on their health, economic, and social activity – they also want to gain information. However, to this day, there isn't a well-centered outlet to get data visualization and prediction of COVID-19, false information might constitute to the delay of the dissection of current data. With this application, it aims to bridge the user and the different sources of data that could visualize it for beneficiaries – not just for the people, but for health workers, and even for the common knowledge of the government. It delivers visualized data, its analysis, and the prediction of the movement of the virus. 

## Scope

The scope of this software is limited to the Philippines. To be specific the NCR Region and its cities only since the data is readily available due to the different sources and the increase of production of test kits. The software does not gather the user's data since it does not need it. The software will only gather source from 

Type CD Python <version> in the Terminal window and press Enter so that the terminal changes its directory to the Python folder on the system.
  
Type and press enter:
```
./configure
```
The script begins by checking the system build type and then performs a series of tasks based on the system you’re using. This process can require a minute or two because there is a large list of items to check.

Type the command below and press Enter:
```
sudo make altinstall
```
The system may ask you for your administrator password. Type your password and press Enter. At this point, a number of tasks take place as the system installs Python on your system.


### Requirements
* **An IDE** <br />
The developers used Visual Studio Code. Download it by going to the VS Code website https://code.visualstudio.com/, and choose what works for your system.

* **Python** <br />
Python is an interpreted, high-level, general-purpose programming language. The official website of Python is https://www.python.org/. After navigating the download site with your Linux browser, click the appropriate link for your version of Linux you wish to install, then click SAVE. <br />
Run the following commands to install Python. 
  ```
  $ sudo apt update
  $ sudo apt install python3 python3-pip3
  ```
  And to verify, run:
  ```
  $ python3 --version
  ```

  ##### Packages:
* **Pandas** <br />
  - Run the following command to install pandas using pip
    ```
    $ pip install pandas 
    ```
    
* **Numpy** <br />
  - Run the following command to install numpy using pip
    ```
    $ pip install numpy
    ```

* **PyQt** <br />
  - To install PyQt, type in the terminal:
    ```
    $ pip3 install --user pyqt5  
    $ sudo apt-get install python3-pyqt5  
    $ sudo apt-get install pyqt5-dev-tools
    $ sudo apt-get install qttools5-dev-tools
    ```
    **Modules used in the program:**
    ```
    from PyQt5 import QtCore, QtGui, QtWidgets
    ```

## Definitions, Acronyms, and Abbreviations
* **Tweepy** – Tweepy is a Python library to access the Twitter API. It is usually used for simple automation and creating twitter function and bots. With Tweepy, developers can accumulate tweets, create and delete tweets, and follow or unfollow users. 
    
* **Twitter API** – The Twitter API allows the access and use of Twitter without having to go through its interface. This access is helpful when performing various automated tasks such as collecting tweets through writing a series of script codes. 
    
* **RDS** – RDS or Relational Database Services

## User Manual

**Instructions:**

## Target Audience

## Focus Areas

### Scenarios

### Languages

## User Cases

1. Actors
     * **Customer User** <br />
        1.1 Customer is a user who works with the features of the program. The program consist of different tabs such as 'to look overall status of cases, deaths and recovered patients', view the cases in graph form, 'to view latest Department of Health news', and 'to look information about the developers redirecting to Github Repository'.

        All of these aforementioned actions of use cases are all the features that the customer may access in the entire program.
         
     * **Software Developer** <br />
        1.2 The main role of a software developer is to identify, test and maintain the database where the sources come from and the future bugs that the customer user may experience from the application.

        The developer gets data from the following sources such as Department Health Offical and trusted Twitter news accounts by using Tweepy webscraping. The developer is the one who will normalize data storing it to the database. These data will be the sole basis in the overall functionality of the tracker program.
        
2. List of Use Cases
     * **Customer User Cases** <br />
        2.1 Display Status (Overview)
          2.1.2 Show Total Cases (Detail)
          2.1.3 Show Total Deaths (Detail)
          2.1.4 Show Total Recoveries (Detail)
        2.2 Visualize Data through Charts (Overview)
          2.2.1 Display Graph
        2.3 Show Geographical Location of Data (Overview)
        2.4 Preview Latest Updates (Detail)
        2.5 Predict Cases (Overall)
        2.6 Display Developer Team Informations (Detail)

     * **Software Developer Case** <br />
        2.1 Show Status (Detail)
        2.2 Show Stored Data (Detail)
        2.3 Save Data in Database (Detail)
        2.4 Show Geographical Data (Overview)
  
## System Architecture
* **Case Diagram**

## Sample Screenshots
