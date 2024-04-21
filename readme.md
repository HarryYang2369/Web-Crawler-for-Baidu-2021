# Web-crawler-for-Baidu-2021 #
This is a project I have done to get data from a Chinese search engine `Baidu` (www.baidu.com) using Python Scrapy with a man-e ad filter. The main concept of this crawler is to enter a keyword in the search
box of the search engine and crawl as many pages as you want to get the information of the links appeared.

## File introduction ##
Here I will write an introduction to every file and its function.


### BaiduResults.xlsx ###
This is the file contains the result the scrapy code get from the search engine.

Column Name   | Discription
------------- | -------------
`Search Request`  | The keyword you want to enter in the search engine's search box to get more info about it.
`Detailed url` | The link to every website appeared when you search the search engine using keyword in `Search Request`
`Title` | The title of the link
`Source` | The source of the link. (Currently unavailable)
`Publish Time` | The date the link is published. (Currently unavailable)
`Introduction` | The introduction to the content of the information the link is directing to.

### config_baidu.ini ###
In this file you can customise the number of keywords you want to search. For each `[keyword]` section, you will need to modify 3 sections: `keyword`, `pages` and `page`. They correspond to the keyword you want to search, at which page you want to stop crawling and at which page you want to start crawling.

### scrapy.cfg ### 
(Automatically created by: scrapy startproject)

`[settings]` section specifies the default settings module for the Scrapy project, and `[deploy]` section provides deployment-related settings. By having a centralized configuration file like scrapy.cfg, you can easily manage and share your Scrapy project settings across different environments and deployments.

### Baidu/... ###
The files in this folder is all automatically created by the `scrapy startproject` command apart from `Du.py` in Baidu/spiders directory. In each file there is/are link(s) that explain the purpose of this file and its codes. But the following readme file is still going to explain a little more about these files. The following are the files in `Baidu` folder:

- ### items.py ###
    It initialled an `scrapy.Item` class called `BaiduItem` which defin the fields for my data structure.

- ### middlewares.py ###
    All automatically created when creating a new scrapy project using `scrapy startproject` command.

- ### pipelines.py ###
    It's used to store the results you get from the search engine. I set the pipelines to store all the data in a `.xlsx` file which has name `BaiduResults.xlsx` which is mentioned above. It also sets the names for the columns and write data line by line and finally save to a single file. An ads filter is added which save a blank line if words that related to ads, for example, delivery or discount, appear in `item[brief]`.

- ### settings.py ###
    It's the scrapy settings for my web crawler peoject. It initiallise names, modules and scrapy pipelines. Links are in the file for user to learn more.
- ### spiders/... ###
    The `spiders` folder contains spiders for defining how to extract data from specific websites. Each Python spider file is designed to target a specific website or set of websites.

    - ### Du.py ###
        The file is designed to target the `Baidu` search engine (www.baidu.com). A Scrapy spider is a Python class that defines how to navigate a website and extract data from it. It includes methods for sending HTTP requests and parsing HTTP responses. It is designed to return the contents under the tags we want it to search and return. It reads data from `config_baidu.ini` about what keywords we want to search and how many page we want to crawl. The extracted data would then be processed and stored according to the pipelines defined in `pipelines.py`.
    

