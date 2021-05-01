# LinkedIn Scraper

**Version 1.0.0**

## Description
Scrapes 10 LinkedIn Profiles based on Google search results and writes the results into a CSV file.
Requires LinkedIn Login.
Scrapes: Name, headline, company, position, school, program, location and URL. 

V1.0.0 works for basic profiles with experience and education listed as one position per company. If a profile lists a company with multiple positions that experience is skipped over for the next company & position pairing that is 1:1. Working on a new version that will identify multiple jobs @ one company and properly pull that company and most recent position.



## How to Use

You will need to edit the "parameters.py" file to add your LinkedIn username and password and to customize the Google search query used to develop the list of profiles. You can also change the output filename here. 

