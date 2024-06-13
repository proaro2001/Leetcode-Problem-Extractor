# Leetcode-Problem-Extractor

## Introduction

Are you looking for a solution to extract the most updated list of Leetcode problems for either job hunting or school research ba ba ba?
This tool is built to help you extract the list of Leetcode problems and visualize your work.

## Disclaimer

This project is only created for visualizing my academic project and practicing my web scraping techniques.

Please don't use it for any other purpose.

## Work Logs

- 2024/06/11 
    - This project is initialized. Some messy documentation of my thoughts is written down.
    - Confirmed another scraping framework [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) doesn't work in this case since Leetcode is dynamic loading their properties into their website.

- 2024/06/12 
    - Implemented the web scraping function using Selenium that successfully extracted [Leetcode](https://leetcode.com/) information.
    - Connected extracted Data with [MongoDB](https://www.mongodb.com).
    - Program generally crashed every 4th page in search attemps. Successfully searched 18 pages by adding timer.
    - Successfully solved the crashing problem and now the program can extracted 3183 [Leetcode](https://leetcode.com/) problem information stably.

## Tech Stack used in this project

- [Leetcode](https://leetcode.com/)
- [Python](https://www.python.org)
- [Selenium](https://www.selenium.dev)
- [MongoDB](https://www.mongodb.com)

<!-- - Vite
- MongoDB
- Express js
- React js
- Node js
- RabbitMQ -->
