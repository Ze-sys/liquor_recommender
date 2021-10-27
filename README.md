# liquor_recommneder
This is an attempt at building  a liquor (specifically beer) recommending system using web scraping of a local liquor distributor's website.  My Sunday league team may find it a valuable tool :) 


I used selenium for scraping. The plan was to use scrappy, which is much faster,  but it turns out the website in question is heavy on javascript. 
I have a bigger project that used scrapy to to collect over five thousand  food recipe data from around the web and analyze it. 

Everything is in the notebook beer_grabber.ipynb.

<h3>Results</h3>

- people don't seem to care about price when rating beer

- It appears people rate beers generously. The minimum is 3.5 stars. Maybe they do it when tipsy and in a good mood

- Other more likely predictors of good ratings may be alcohol contents, which I did not scrap. Also, did not scrap number of ratings. <br>A five star from 1 consumer should not carry the same weight as a five star from 100 happy consumers.

- When on sale, savings as a percentage of regular price are slightly higher for lower total volume of beer.

- Keep in mind product ratings are not correlated with price or volume of beer. But the following information is maybe useful 

<h3>Conclusion </h3>
This was a basic data science. We scrapped beer data (N = 240) from a major liquor distributor's website, and did some basic analysis like correlation calculations. The overarching goal of this exercise was to build a beer classifier model based on ratings. It is now clear that ratings are not correlated with any of the features in our dataset. Along the way, though, we came up with basic metrics to help us choose beer next time we hit the liquor store.
Maybe other factors such as alcohol content, and culture are better predictors. 

<p> NB: This is a personal fun project. I tried to follow all the ethical web scraping methods. Read the robots.txt file, gave ample time between requests and tried to represent myself to the server in case the website owners did not like all of that and wanted to stop me.</p>
