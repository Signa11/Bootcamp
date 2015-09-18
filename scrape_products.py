import requests
import pandas as pd
import json
import matplotlib.pyplot as plt


#Import Best Buy API

#t = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id=abcat0101000))?apiKey=g82m86t7tdzw2mau9qvtud9b&sort=bestSellingRank.asc&show=bestSellingRank,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,inStoreAvailabilityText,longDescription,manufacturer,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,preowned,regularPrice,salePrice,shipping,shippingCost,shortDescription,sku,type,upc,url&pageSize=100&format=json")
df =pd.read_json("https://api.bestbuy.com/v1/products((categoryPath.id=abcat0101000))?apiKey=g82m86t7tdzw2mau9qvtud9b&sort=bestSellingRank.asc&show=sku,bestSellingRank,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,inStoreAvailabilityText,longDescription,manufacturer,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,preowned,regularPrice,salePrice,shipping,shippingCost,shortDescription,sku,type,upc,url&pageSize=100&format=json")
#g = pd.read_json(str(t))


# Load in Panda
dd = pd.DataFrame(df)
products = dd["products"]

# Create list with all columns
columns=['SKU', 'Manufacturer', 'Model', 'Price', 'Reviews', 'Color', 'Savings', 'Best Selling Rank',
         'Review', 'Screen Size Class', 'HDMI Ports', 'Product Weight', 'USB Ports', 'Network', 'Speaker Output',
         'Product Depth', 'Electricity Use', 'Display Type', '3D', 'Screen Size', 'Refresh Rate']

# Initialize 2 dictionaries to do the work
intprod = []
totprod = []

for i in products:
    intprod.append(i['sku'])
    intprod.append(i['manufacturer'])
    intprod.append(i['modelNumber'])
    intprod.append(i['salePrice'])
    intprod.append(i['customerReviewCount'])
    intprod.append(i['color'])
    intprod.append(i['dollarSavings'])
    intprod.append(i['bestSellingRank'])
    intprod.append(i['customerReviewAverage'])
    for y in i["details"]:
        if y["name"] == "Screen Size Class":
            intprod.append(y['value'])
        if y["name"] == "Number Of HDMI Inputs":
            intprod.append(y['value'])
        if y["name"] == "Product Weight With Stand":
            intprod.append(y['value'])
        if y["name"] == "Number Of USB Port(s)":
            intprod.append(y['value'])
        if y["name"] == "Network Compatibility":
            intprod.append(y['value'])
        if y["name"] == "Speaker Output":
            intprod.append(y['value'])
        if y["name"] == "Product Depth With Stand":
            intprod.append(y['value'])
        if y["name"] == "Estimated Annual Electricity Use":
            intprod.append(y['value'])
        if y["name"] == "Display Type":
            intprod.append(y['value'])
        if y["name"] == "3D Technology":
            intprod.append(y['value'])
        if y["name"] == "Screen Size":
            intprod.append(y['value'])
        if y["name"] == "Refresh Rate":
            intprod.append(y['value'])

    totprod.append(intprod)
    newDf = pd.DataFrame(totprod, columns=columns)
    print(newDf)
    intprod = []

    newDf.to_excel("test_csv.xlsx")
