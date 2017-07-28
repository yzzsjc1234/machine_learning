#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
records_count = len(enron_data)
print("Size of the enron dataset:%i" %records_count)
print("Size of features for each person:%i" %len(enron_data["SKILLING JEFFREY K"]))


POI_count = 0
for key, value in enron_data.items():
    if(value["poi"]==1):
        POI_count += 1
print ("Count of POI in enron dataset:%i" %POI_count)

poi_names = open("../final_project/poi_names.txt")
lines = poi_names.readlines()
print ("Count of POI in poi_names list:%i" %(len(lines)-2))

print ("What is the total value of the stock belonging to James Prentice:%i" %enron_data["PRENTICE JAMES"]["total_stock_value"])
print ("Hom many messages do we have from Wesley Colwell to POIs:%i" %enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print ("What is the value of stock options exercised by Jeff Skilling:%i" %enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print ("The total of the one who took home the most money: %i" %max(enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"], enron_data["LAY KENNETH L"]["total_payments"]))

total_payments_nan_count = 0
for key, value in enron_data.items():
    if(value["total_payments"]=="NaN"):
        total_payments_nan_count += 1
print ("What percertage of people in the dataset have 'NaN' for their total payments:%.2f" %(total_payments_nan_count*100/records_count))

POI_total_payments_nan_count = 0
for key, value in enron_data.items():
    if (value["total_payments"]=="NaN" and value["poi"]==1):
        POI_total_payments_nan_count += 1
print ("What percertage of POIs in the dataset have 'NaN' for their total payments:%.2f" %(POI_total_payments_nan_count*100/POI_count))

POI_total_stock_value_nan_count = 0
for key, value in enron_data.items():
    if(value["total_stock_value"]=="NaN" and value["poi"]==1):
        POI_total_stock_value_nan_count += 1
print ("What percertage of POIs in the dataset have 'NaN' for their total stock value:%.2f" %((POI_total_payments_nan_count+10)*100/(POI_count+10)))
