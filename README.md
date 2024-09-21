# recommendation_engines
Various simple examples of how to make recommendation engines

## Main Idea
A recommendation engine should be able to make recommendations based on something's history. 
These recommendations are really just the best predictions of what something's future will look like. 
So we can think of recommendation engines as prediction engines, given something's history.

Recommendation engines are personalized to something out of all things and here we personalize 
the model's prediction by always supplying the model with something's history. 

The all things could be a binary matrix of somethings like users and somethings their watched movies. 
A users history in that case will be the column of movies actually watched, so just the list of movies 
for which that user has a 1 in the matrix (order of movies matters but not for this project). 

The all things could be just a single column of a stock's price. So the recommendation in that case 
would just be a prediction of the stock's price given some chunk of price history.

In this project we attempt to capture both use cases of making predictions, where the predictions could 
be for a specific column in a more than 1 column matrix or the prediction could be for a time-series 
type of data, like the price of a single stock.


