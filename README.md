# a2psms
This App is to demo A2P SMS API


## Clone the Repo

`git clone https://github.com/dibyenduroy/a2psms/`


## Install the Dependency

`pip install ringcentral`


## Configure the Config.py file based on your App and Enviornment

### Run the below command

`python a2psms.py`

### Various Scenarios
You can play with the code by testing/commenting various scenarios
    #broadcastsmsbatch() -> To send a Broadcast message to Multiple numbers
    #customizesmsbatch() -> To send a Personalized message to Multiple numbers
    #getbatchstatus("0ab4f3d1-9ee6-4d3f-accd-4b0567eb2992") -> To get the status of a Batch
    #getmessagestatus("0ab4f3d1-9ee6-4d3f-accd-4b0567eb2992") -> To get the status of 1 or ALL batches
    getmessagestatusById('40146') -> To fetch the status of a specific SMS
    #Sample Batch Response
