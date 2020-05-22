This is a django app. API end points are created using django rest frameowork. Mobile apps like Android or IOS apps can interact
with these apis to fetch data from the database or to update or delete data (based on privilge assigned to user).

Various models are created for storing different type of information about a user. API end points are designed using DRF for each model
(A table in MySQL Database). Users using an app can modify their personalized data (their profile) by modifying entries of a data model.
App will communicate with backend server through rest apis (developed using django rest framework)

API end points created in this project will power a flutter application.

To see how various apis are desigend, 

GO TO api/rest_apis/api and then explore each API file(one corresponding to each model).

To see how serializers are serializing or deserializing the data

GO TO api/rest_apis/serializers.py.

To see how models are designed and database schema is implemented,

GO TO api/rest_apis/profileimage.vuerd.json or api/rest_apis/models.py

For database visualization,

GO TO api/schema_for_all_apps_combined.svg

(ALL APIS ARE TESTED USING POSTMAN)

