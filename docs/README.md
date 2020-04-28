# [Project-CovidRecon](https://vppexis.github.io/CPE106L-ProjectCovidRecon/)

### Project Members

    1. Cinco, Cedrick
    2. Directo, Claudee Khiarra
    3. Bake, Seungyoon
    4. Navarro, Laurence Kobe
    5. Panugan, Van Philip
    6. Tipan, Ivan Patrick


### Requirements
- Python 3.7
- PyQT5
- Tweepy

### Running the Program

1. Install al the requirements
2. Run in terminal 'python main.py'


<br>
<br>

# Project Documentation


Written by: Laurence Kobe Navarro, Claudee Directo & Cedrick Cinco


# Introduction
Data Science and mathematical models can help in shedding light on the evolution of the novel Coronavirus pandemic. By predicting, visualizing, and analyzing the virus, we will be able to put up an immunity against it through the help of data and information. This is an application that can forecast real-time COVID-19 data that can fill the gap between users and various sources of information in order to produce reliable data.  As the world plunged into a pandemic caused by COVID-19, both technology and medical field tries to understand how the virus had spread exponentially across the globe as well as on how to cure it. As people get wary about the health implications this pandemic poses on their health, economic, and social activity – they also want to gain information. However, to this day, there isn't a well-centered outlet to get data visualization and prediction of COVID-19, false information might constitute to the delay of the dissection of current data. With this application, it aims to bridge the user and the different sources of data that could visualize it for beneficiaries – not just for the people, but for health workers, and even for the common knowledge of the government. It delivers visualized data, its analysis, and the prediction of the movement of the virus. 

## Purpose
The purpose of the program is as follows:
    
* To gather COVID-19 data cases and its location
    
*  To visualize the data into charts.
    
* To predict the logarithmic and exponential pattern
    
* To show the geographical status of each province.





## Scope

The scope of this software is limited to the Philippines. To be specific the NCR Region and its cities only since the data is readily available due to the different sources and the increase of production of test kits. The software does not gather the user's data since it does not need it. The software will only gather source from 


## Definitions, Acronyms, and Abbreviations
* **Tweepy** – Tweepy is a Python library to access the Twitter API. It is usually used for simple automation and creating twitter function and bots. With Tweepy, developers can accumulate tweets, create and delete tweets, and follow or unfollow users. 
    
* **Twitter API** – The Twitter API allows the access and use of Twitter without having to go through its interface. This access is helpful when performing various automated tasks such as collecting tweets through writing a series of script codes. 
    
* **RDS** – RDS or Relational Database Services


## Reference 
The Software Design Document is divided into 11 sections with various subsections. The sections of the Software 
    


Design Document is:
1. Introduction
2. Use Cases
3. Design Overview
4. System Object Model
5. Object Descriptions
6. Object Collaborations
7. Data Design
8. Dynamic Model
9. Non-function Requirements
Supplementary Documentation    


<<<<<<< HEAD
<<<<<<< HEAD
# [Use Case](https://mymailmapuaedu-my.sharepoint.com/:b:/g/personal/vpmpanugan_mymail_mapua_edu_ph/EYXU1spIrMJHhMdwh3PTaxQB_mQ30y2tDTq4hT5FtrIBbg?e=yOU3CJ)
=======


## Overview

# Use Cases

## Actors
1. **Customer User** - The customer is the user who uses or benefit from the software application. This is an abstraction or generalization of the users as they all perform similar actions but for different reasons. The actions that they may perform are: (1) to show or display the overview of the status of COVID-19 in Metro Manila, (2) visualize the data into charts for demonstrating the relationships, increments, and decrements as well as the patterns in each data points through a pie chart, bar chart and line charts, (3) show the geographical location of the cases in Metro Manila by the whole region or a specific city, (4) and predict the number of cases/growth through logarithmic and exponential models.

2. **Software Developer** - 

## List of Use Case
* Customer Use Cases
    - Display Status (Overview)
        - Show Total Cases
        - Show Total Deaths
        - Show Total Recovered

    - Visualize Data through Charts (Details)
        - Display Pie Chart(Detail)
        - Display Bar Chart(Detail)
        - Display Line Chart(Detail)

    - Show Geographical Location of Data (Overview)
        - Show all cities (Detail)
        - Show a specify city (Detail)

    - Predict Information
        - Exponential Model (Detail)
        - Logarithmic Model (Detail)

    - Display Developer Team Informations (Detail)

## Use Case Diagram
* CovidRecon Monitoring App - Entire Use Cases in the Software Application
![alt text](UseCaseDiagram.png)

* Customer - Essential Use Cases
![alt text](Customer-EssentialUseCases.png)

* Software Developer - Essential Use Cases
![alt text](SoftwareDeveloper-EssentialUseCases.png)


## Use Cases
* Customer Use Cases: Display (Overview)

    | **Use case name**: Display Status (Overview)  | **ID**: DO                | **Priority**: High  |   |   |
    |-------------------------------------------|-----------------------|-----------------|---|---|
    | **Primary Actor**: Customer (Client)          | **Use Case Type**: System | **Level**: Overview |   |   |

    **_Brief Description_**
    
    This use case describes the main interface of the software application in a workflow. It shows the current status and the percentile of the total number of the case, the total number of deaths and the total number of recovered patients limited only in the National Capital Region (NCR) in the Philippines. The cities covered in the statistical overview in this window are Manila, Quezon City, Caloocan, Las Piñas, Makati, Malabon, Mandaluyong, Marikina, Muntinlupa, Navotas, Parañaque, Pasay, Pasig, San Juan, Taguig, and Valenzuela. The data stored in the database reflects in this use case since all of the information regarding the latest number of COVID-19 patients is updated from time to time through scraping.

    **_Goal_**

    To deliver the latest statistical number of COVID-19 patients in Metro Manila accurately and precisely to the client with a friendly interface.

    **_Sucess Measurement:_**
=======
>>>>>>> 1cf18a818cf447488ecb4ce0de4f42d7397ba9c4



# [Use Case](https://mymailmapuaedu-my.sharepoint.com/:b:/g/personal/vpmpanugan_mymail_mapua_edu_ph/EYXU1spIrMJHhMdwh3PTaxQB_mQ30y2tDTq4hT5FtrIBbg?e=yOU3CJ)




<<<<<<< HEAD
In this section, we will discuss the design overview of the application. The application will have an Interface, Interaction, Database, WebScrapper, StreamListener, and IOAuthenticator. The Interface is the main control of the application where the user can interact with the software through the interaction façade. Thus, access to the database. Furthermore, the database can be modified by both the WebScrapper and TweppyStreamListener which can use the TwitterAPIAuthenticator to authenticate the API.

>>>>>>> 0bd9d925fd7cf92027b206c40448cfe86072efc4
=======
>>>>>>> 1cf18a818cf447488ecb4ce0de4f42d7397ba9c4

## System Architecture



## System Interfaces
<<<<<<< HEAD
<<<<<<< HEAD
=======
- **User Interfaces**

The user interface for the system allows the user to get the latest updates regarding the COVID-19 cases in the NCR Region. The user can also access and visualize the data regarding the COVID-19 in the NCR region. It also shows a graph of the progress of the COVID-19 in the NCR. Lastly, it also shows the cases per each city in the NCR. The interface has buttons according to the data it needs to visualize. This allows for ease of navigation using only the mouse.

- **Software Interfaces**

## Constraints and Assumptions

- **List Assumptions**
    
    1. It assumed that the database is in MySQL format.

- **List of Dependencies**
=======
>>>>>>> 1cf18a818cf447488ecb4ce0de4f42d7397ba9c4


<<<<<<< HEAD
>>>>>>> 0bd9d925fd7cf92027b206c40448cfe86072efc4
=======
>>>>>>> 1cf18a818cf447488ecb4ce0de4f42d7397ba9c4


# System Object Model

