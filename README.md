# ILMT-Telugu

- crawl.py would crawl for all wikipedia related links that will be cleaned and stored as a csv file.
- getWikiLinks.py would then use the links from the csv files to test whether they are links of categories or articles and creates a final list of articles that we can extract information from
- extractInfo.py would then use these final article links to scrape required information from these and store them as needed (which can be changed from code).