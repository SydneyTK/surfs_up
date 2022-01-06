# import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#9.5.1 now begin setting up DB
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

#9.5.1 set up Flask 
app = Flask(__name__)
#all routes need to go after this line or else code may not run properly 

#9.5.2 welcome root
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/endcd class
    ''')

 #9.5.3 precipitation route    
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year=dt.date(2017,8,23)- dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip) 

#9.5.4 stations route 
@app.route("/api/v1.0/stations")
def stations():
    results= session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    #the stations=stations is what needs to be denoted to format the list into a JSON file 

#9.5.5 monthly temperature route 
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)

#9.5.6 Statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    #create a list 
     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

     #query the DB for that list of start and end dates 
     if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    #create the query to produce stats
     results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
     temps = list(np.ravel(results))
     return jsonify(temps)