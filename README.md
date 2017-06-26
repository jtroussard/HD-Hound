[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgoo.gl%2FRw2kZ2&text=Wanna%20known%20whens%20the%20best%20time%20to%20buy%20hard%20drive%20storage%3F%20Check%20out%20Hard%20Drive%20Hound%20&hashtags=python%2C%20webscraping%2C%20hdhound)
[![Twitter Follow](https://img.shields.io/twitter/follow/espadrine.svg?style=social&label=Follow)](https://twitter.com/TekkSparrow?lang=en)


# Hard Drive Hound (work in progress)
## Announcements
Project is temporarily on hold. I over looked the need to implement responsible metering mechanisms when making requests and ran into some trouble with the target sites administrator. I've been reading up on best practices and hope that the block will be removed soon. In the mean time I'll work on building a mock site to run my tests against.

## Description
A web scraper written to send simple but detailed microcenter pricing data on internal hard drives. Overall goal is to develop this into a program which will run on a home server and deliver alerts on good hard drive prices. Storing the data will allow for comparison of prices, which can lead to a better understanding if a sale is in fact a sale. Additionally, working with the data to discover not obvious correlations.

## Development Schedule
Initial versions will focus on just internal hard drives, without any other specifications. This is to avoid zeroing in on just one section of program. My idea is to get a board skeleton set up and than start adding in the details and extra functionality. Once the mechanism of gathering, cleaning, analyzing, storing/retrieving, and delivery of this narrow selection of data is completed and tested I can advance this project to the next stages.

## Technologies
I'm not entirely sure of all the tools that will be necessary for this project but these are the main technologies I will try to stick by for this project.
  * Python 3
  * MonogoDB
  * Pymongo

## To Do List
  1. ~~Get data~~
  2. ~~Clean and load data into a mongo db~~
  3. ~~Load project on home server~~
  4. Automate program to run at certain intervals (Daily? Weekly?)
      * I'm thinking this can be part of another sub analysis to determine what is the more optial setting for this automation
  3. Run analysis, and send alert when either;
      * The system detects possible erroneous data   (ex: 1,000 GB per dollar)
      * The system is triggered by user set rules    (ex: price point below $X.XX)
      * The system detects interesting data          (ex: ??? not sure yet exactly)
  4. Package project up into a simple to activate .exe
  5. **IMPORTANT** Need to design some metering mechanisms and take a look at the robot.txt
  
## Future features
  1. Add more categories and allow for filters
  2. Develop GUI


## LOG
  * Thu Jun 22 3:32PM:
    1. create html file from url request
    2. parce individual products into list object
    3. further parce product details into dict objects
  * Fri Jun 23 7:42PM:  
    1. fixed redundant appending of items
    2. attached mongo database
    3. wrote db functions
    4. completed db tests
  * Sat Jun 24 6:12PM:
    1. fix bugs found during first tests
  * Sun Jun 25 9:04PM:
    1. completely recoded database functions
        * hard coded db access
        * separated price per gb function
        * reworked insert to include document updating
        * created mech. for price history
    2. tested database functions
  * Mon Jun 26 10:34AM
    1. ran scraper this morning and got 503 error
    2. announce project hold
