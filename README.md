# Project 5: Interst Points

A simple web server giving locations of interest points (I chose pizza places ), but can easily be changed by changing the interestpoints/interestpoints.txt. A credentials skeleton file is included in the repo, change to your specific information and rename to credentials.ini

 Uses leaflet and flask to send data between client and server. 
 
 Features include: Customizable interest points (parsed in python, served in JSON) 
 Search Bar, search for an address and add a marker to it
 Address information where a user clicks (Using Esri geocoding)

## Install
  make
  pip3 -r requirements.txt
  ./start.sh
  
  Zachary Bower
  zbower@uoregon.edu
