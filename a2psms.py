#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

from ringcentral.http.api_exception import ApiException
from ringcentral import SDK
from config import USERNAME, EXTENSION, PASSWORD, APP_KEY, APP_SECRET, SERVER


def main():




    sdk = SDK(APP_KEY, APP_SECRET, SERVER)
    platform = sdk.platform()
    platform.login(USERNAME, EXTENSION, PASSWORD)
    TF_NUMBER = '18883303674'

    def customizesmsbatch():
        #POST Body
        print("Starting to Compose the SMS Body")
        requestBody = {
            'from': TF_NUMBER,
            'text': 'Broadcast SMS',
            'messages': [{'to':["+14083388064"],'text': 'This is for Dibyendu, stay safe'},{"to":["+14087187847"],'text': 'This is for Baisakhi, stay safe'}]
        }
        print("########SMS Body Composed #############")
        try:


            print("#########Just Before Sending SMS###############")
            response =  platform.post('/account/~/a2p-sms/batch', requestBody)
            print(response.json())
            print("############SMS sent. Batch id: " + response.json().id)
            resp = platform.get('/restapi/v1.0/account/~/a2p-sms/batch/' + response.json().id)
            print(resp.text())

        except ApiException as e:
            print("Error while Sending SMS" + e)


   # This is to Send SMS in a Batch
    def broadcastsmsbatch():
        #POST Body
        print("Starting to Compose the SMS Body")
        requestBody = {
            'from': TF_NUMBER,
            'text': 'Broadcast SMS',
            'messages': [{'to':["+14083388064"]},{"to":["+14083388064"]}]
        }
        print("########SMS Body Composed#############")
        try:


            print("#########Just Before Sending SMS###############")
            response =  platform.post('/account/~/a2p-sms/batch', requestBody)
            print("############SMS sent. Batch id: " + response.json().id)
            resp = platform.get('/restapi/v1.0/account/~/a2p-sms/batch/' + response.json().id)
            print(resp.text())

        except ApiException as e:
            print("Error while Sending SMS" + e)
  #######################################################################################################
    def getbatchstatus(id):





        print("Starting to get SMS Batch Status")

        try:

            batchId = id
            print("#########Getting Batch Status###############")
            response =  platform.get('/restapi/v1.0/account/~/a2p-sms/batch/' +  batchId)
            print(response.text())


        except ApiException as e:
            print("Error while Getting batch Status" + e)

###################################################################

  #######################################################################################################
    def getmessagestatus(id):





        print("Starting to get SMS Message Status")

        try:

            batchId = id
            print("#########Getting SMS Status###############")
            endpoint = '/restapi/v1.0/account/~/a2p-sms/messages?batchid=' +  batchId
            print(endpoint)
            response =  platform.get('/restapi/v1.0/account/~/a2p-sms/messages?batchId=' +  batchId)
            print(response.text())


        except ApiException as e:
            print("Error while Getting Message Status" + e)

###################################################################

    def getmessagestatusById(id):





        print("Starting to get SMS Message Status")

        try:

            messageId = id
            print("#########Getting SMS Status###############")
            response =  platform.get('/restapi/v1.0/account/~/a2p-sms/messages/' +  messageId)
            print(response.text())


        except ApiException as e:
            print("Error while Getting Message Status" + e)

###################################################################

    #broadcastsmsbatch()
    #customizesmsbatch()
    #getbatchstatus("0ab4f3d1-9ee6-4d3f-accd-4b0567eb2992")
    #getmessagestatus("0ab4f3d1-9ee6-4d3f-accd-4b0567eb2992")
    getmessagestatusById('40146')
    #Sample Batch Response
    #{
 #  "id":"0ab4f3d1-9ee6-4d3f-accd-4b0567eb2992",
 #  "from":"+18883303674",
 #  "batchSize":2,
 #  "processedCount":0,
#   "status":"Processing",
  # "createdAt":"2020-03-31T21:51:42.682Z",
 #  "lastUpdatedAt":"2020-03-31T21:51:42.682Z"
#}


if __name__ == '__main__':

    main()
