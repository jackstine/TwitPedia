# TwitPedia
Twitter and Wikipedia Web Page.

I used https://github.com/reivaj05/Kabbage  as a reference, just noting that since I was not used to 
Django that much

Performance:
    A lot can be done to increase the performance,  have a threading service call on both or any list of given services, to retrieve the data asynchronously. We could put it on a websocket and then just give the client the data.  With some javascript this would just react to the data on the socket.


    Another thing that can be cool to do is to expand the HTMLTable a lot, so that it can handle multiple lists, and change the bootstrap spacing to that amount.  As well have a separate pager for each list, meaning that going to page 2 will not do both Twitter and Wikipedia.  They would act like separate entities.
