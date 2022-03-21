# liquor_recommneder - Not really!

This repo was for an attempted project at building a liquor (specifically beer) recommending system using data scraped from a local liquor distributor's website.  My Sunday league team may still find it a valuable tool :) 


I used selenium for scraping. The plan was to use scrapy, which is much faster. It turns out the website in question is heavy on javascript. 
I have a bigger project that uses scrapy to to collect over thousands of  food recipe data. 

Everything is in the notebook beer_grabber.ipynb.

<h3>Results</h3>

- people don't seem to care about price when rating beer

- It appears people rate beers generously. The minimum is 3.5 stars. Maybe they do it when tipsy and in a good mood. I found out later on that I did sort the pages by ratings before scraping. So, I mostly did scrap the top rated beers. But I stand by my conclusion, without evidence, that people rate beers generously.

- Other more likely predictors of good ratings may be alcohol contents, which I did not scrap. Also, did not scrap number of ratings. <br>A five star from 1 consumer should not carry the same weight as a five star from 100 happy consumers. 

- When on sale, savings as a percentage of regular price are slightly higher for lower total volume of beer.

<h3>Conclusion </h3>
We just completed the most fun and simple data science project one can do on a vacation day. We scraped beer data (N = 240) from a website, and analysed it. The more ambitious goal of this exercise was to build a beer classifier model. It turns out beer ratings are not correlated with any of the features in our dataset. Maybe other factors such as alcohol content, and culture are better predictors of good beer. Until, if ever, come back to this project with more data, we can enjoy the basic metric we came up with to help us choose beer whenever we hit the liquor store!

<p> NB: This is a personal fun project. I tried to follow all the ethical web scraping protocol. Read the robots.txt file, gave ample time between requests and tried to represent myself to the server, in case the website owners did not like all of that and wanted to stop me.</p>
