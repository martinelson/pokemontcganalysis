# Pokemon Trading Card Game Price Analysis

## Description

This project consists of multiple facets of the data analysis life cycle centered around prices of the Pokemon trading
card game. See below for a details of each folder.

# data-collection folder
##main.py - 
This file holds the main URLs to pull via selenium which is used in the get_card_data function in scraping.py, and then
saves the data into a dataframe, adding to the dataframe each subcategory in the loop. The final dataframe is exported 
to pokemon-card-price.csv

##scraping.py - 
This file holds the function to retrieve data from the website via selenium. Data collected is the card type, the name
of the card, the market price, and which set the card came from.

## names.py - 
This file collects all pokemon names to then match with the card name of the Pokemon Card type. This is later used to
match the pokemon name to the card in main.py


# analysis folder

##analysis.py - 
This file takes the pokemon-card-price.csv and obtains various top 10 rankings of card prices, broken out by the
different categories of cards within the trading card game. 


##regression folder

##data-prep - 
outputs different files used in the regression file (rarity-card-type.csv, and rarity-card-type-v2.csv)

##pokemon-regression.Rmd - 
This R-script file performs a multi-linear regression analysis based on the files created in the data-prep file


##website - 
##used to display the findings in the analysis conducted in the above files 

