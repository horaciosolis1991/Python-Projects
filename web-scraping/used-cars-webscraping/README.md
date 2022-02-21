# Scraping used-cars data using selenium

This projects acts like a proof of concept of the power of functionalities of web scraping, as webpages are getting more and more dynamic selenium+requests is used to accurately retrieve
all the data instead of retrieving javascript code that will not add any information.
As this projects is just a proof of concept, we just pull partial data from the website, in this case wolkswagen cars, is not neccesary to retrieve the whole webpage information, as retrieving s
some records is enough to prove that more criterias can be added to retrieve more data, if needed.
After succesfully run the script you should have a dataset as the one below. <br /><br />


<p align="center">
<img src="https://github.com/horaciosolis1991/Python-Projects/blob/main/web-scraping/res/used-cars-ws.png" >
</p>





Varibles are:


|  Variable    |                  Description                        |
| -----------  | --------------------------------------------------- |
| brand        | Brand of the car, in this case only volkswagen cars |
| model        | Model of the car                                    |
| year         | Year in which the car was manufactured              |
| price        | Current sell price for the car                      |
| miles        | Miles travelled by the car                          |
| car_location | Car location                                        |
| car_state    | State of the car location                           |




After retrieving the dataset many interesting things can be answered with it like:

* Cheapest car in US? <br />
* Cheapest state to buy a used cars?<br />
* Price comparison among states.<br />

Also, this web scraping can be run on a daily basis storing its information on a local/cloud databases to do further analysis such as:

* Best moment to buy a car?<br />
* Car price evolution (daily, weekly, monthly basis)<br />