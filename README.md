# surfs_up
Module 9- Advanced Data Storage and Retrieval 

# Overview of the Analysis 
Thorough analysis had been done on the weather and location of a surf and ice creme shop with our business partner W. Avy. The investors love the idea, our analysis, and presentationo of the data on a webpage. However before opening day they wanted specific data for the months June and December.

# Results
See tables below. 
* The range of temperatures in December is larger compared to June. December has a 27 degree spead, whereas June has a 21 degree spead. This allows us to infer that in December there is the possibility of having more volitile weather of some oddly warm or cold days. 
* Furthermore we can also conclude June has more steady or consistant weather because the percentiles are closer together. The majority of temperatures would fall between 73 and 77 degrees, whereas December is 69 to 74 degrees. 
* There are almost 200 more weather observations or 200 more data points for June compared to December.
* Finally June is warmer than December by on average 3.9 degrees.  

[Dec_Temps.PNG](C:\Users\Sydney Kieswetter\Class\surfs_up\Reasources)
[June_Temps.PNG](C:\Users\Sydney Kieswetter\Class\surfs_up\Reasources)

# Summary 
When comparing the temperatures from June to December it would have been expected that the temperatures in June are more steady, consistant and warmer compared to December's cold and more volitile temperatures, because of the season, winter vs summer.   

## Additional Quieries 
Comparing the precipitation and temperatures would have been interesting: 
results = session.query(Measurement.tobs, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()

Selecting a specific station, for example USC00518838, because it only has 511 observations compared to others that have thousands of weather observations. It would be intersting to see what little data is there and maybe uncover why there such a small amount of data, i.e.) is the weather constantly cold, it rains often, etc. 
results = session.query(Measurement.tobs, Measurement.prcp).filter(Measurement.station == 'USC00518838').all()