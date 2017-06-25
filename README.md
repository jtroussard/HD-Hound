[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgoo.gl%2FRw2kZ2&text=Wanna%20known%20whens%20the%20best%20time%20to%20buy%20hard%20drive%20storage%3F%20Check%20out%20Hard%20Drive%20Hound%20&hashtags=python%2C%20webscraping%2C%20hdhound)
[![Twitter Follow](https://img.shields.io/twitter/follow/espadrine.svg?style=social&label=Follow)](https://twitter.com/TekkSparrow?lang=en)


# Hard Drive Hound (work in progress)
A web scraper written to gather hard drive pricing data
## LOG
  * Thu Jun 22 3:32PM:
    1. create html file from url request
    2. parce individual products into list object
    3. further parce product details into dict objects
  * Fri Jun 23 7:42PM:  
    1. fixed redundent appending of items
    2. attached mongo database
    3. wrote db functions
    4. completed db tests
  * Sat Jun 24 6:12PM:
    1. fix bugs found during first tests
  * Sun Jun 25 6:02PM:
    1. completely recoded database functions
        * jhg
      * hard coded db access
      * separated price per gb function
      * reworked insert to include document updating
      * created mech. for price history
    2. tested database functions
