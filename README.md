# Web-crawler-for-Baidu-2021 #
This is a project I have done to get data from a Chinese search engine `Baidu` (www.baidu.com) using Python Scrapy with a man-made ad filter. The main concept of this crawler is to enter a keyword in the search
box of the search engine and crawl as many pages as you want to get the information of the links appeared.

## File introduction ##
Here I will write an introduction to every file and its function. Here is the structure of this package:


### BaiduResult.xlsx ###
This is the file contains the result the scrapy code get from the search engine. Here is a list of columns:

Column Name   | Discription
------------- | -------------
`Search Request`  | The keyword you want to enter in the search engine's search box to get more info about it.
`Detailed url` | The link to every website appeared when you search the search engine using keyword in `Search Request`
`Title` | The title of the link
`Source` | The source of the link. (Currently unavailable)
`Publish Time` | The date the link is published. (Currently unavailable)
`Introduction` | The introduction to the content of the information the link is directing to.

### scrapy.cfg ### 
(Automatically created by: scrapy startproject)

`[settings]` section specifies the default settings module for the Scrapy project, and `[deploy]` section provides deployment-related settings. By having a centralized configuration file like scrapy.cfg, you can easily manage and share your Scrapy project settings across different environments and deployments.

