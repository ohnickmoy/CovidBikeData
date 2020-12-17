# Hello there!

This is a small project that sets out to do some data analysis of bike share data during the Covid-19 period, but also is a means of learning some new technologies as I grow as a software developer. 

## Project Aims

What this project sets out to do is take public bike share data, do some data analysis of them through Python scripts, and then put some visualizations on this site. The project also hopes to automate most of process, from the pulling, to the analysis, to finally, updating the site, through Github Actions. 

Data Visualizations so far are generated through the [matplotlib](https://matplotlib.org/) Python module. 

The site is generated using [Hugo](https://gohugo.io/) and hosted on [Netlify](https://www.netlify.com/). The site gets redeployed whenever an update to the repo occurs. 

### Github Repo

To take a look at the code for this project, you can access [this repo](https://github.com/ohnickmoy/CovidBikeData)

## The Story so far

So far, the project is taking data from [this s3 bucket](https://s3.amazonaws.com/tripdata/index.html) provided by Citibike in New York City. 

After New York is done, I'll probably set out to do similar analysis for other cities, like Boston or San Francisco. Each city will get their own page, which you can see on the menu above. 

## Collaboration 

If you want to help out on this project, just send a message to [covidbikedata@gmail.com](mailto:covidbikedata@gmail.com)!
