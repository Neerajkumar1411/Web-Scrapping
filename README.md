Overview


This project demonstrates how to perform web scraping using Python, Requests, and BeautifulSoup. It extracts book details (title, price, and rating) from Books to Scrape, a website designed for practicing scraping techniques. The script loops through multiple pages, collects data, and saves it into a structured CSV file.

Features


Scrapes book data (title, price, rating) from 5 pages.

Handles HTTP requests with error checking.

Uses BeautifulSoup for HTML parsing.

Stores results in a clean CSV file (books.csv).

Includes polite scraping practices (1-second delay between requests).

Tech Stack

Python 3

Requests – for sending HTTP requests

BeautifulSoup (bs4) – for parsing HTML

CSV module – for saving data into a CSV file

Time module – for adding delays between requests

How It Works


The script dynamically builds URLs for the first 5 pages of the catalogue.

For each page:

Sends a GET request.

Parses the HTML content.

Extracts book details:

Title

Price

Rating (converted from CSS class to readable format)

Appends all data into a list.

Writes the collected data into books.csv.
