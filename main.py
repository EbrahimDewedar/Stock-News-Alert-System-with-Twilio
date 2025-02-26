import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY= "5VSZBEIAYD28TGK0"
NEWS_API_KEY= "6a752d5ddb6a47788efb937ce3661125"

TWILIO_SID= "481jfghw84b7e964c7eac4f37a77"
TWILIO_AUTH_TOKEN= "31reyef9b43609b3145a220f"

stock_params= {'function':"TIME_SERIES_DAILY",'symbl':STOCK_NAME,'apikey':STOCK_API_KEY}

response= requests.get(url=STOCK_ENDPOINT, params= stock_params)
data= response.json()["Time Series (Daily)"]


data_list= [value for (key,value) in data.items()]

yesterday_data= data_list[0]
yesterday_closing_price= yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data= data_list[1]
day_before_yesterday_closing_price= day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference= float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down= None
if difference > 0:
    up_down= "🔺"
else:
    up_down= "🔻"

diff_percent= (difference/float(yesterday_closing_price)) * 100
print(diff_percent)

if abs(diff_percent) > 1:
    print("Get News")
    news_params= {'qInTitle':COMPANY_NAME, 'apikey':NEWS_API_KEY}
    news_response= requests.get(url= NEWS_ENDPOINT, params=news_params)
    articles=news_response.json()["articles"]

    three_articles= articles[:3]

    formatted_articles= [f"last Feedback\n{STOCK_NAME}:{up_down}{diff_percent}%\nHEADLINE:{article['title']}\nBRIEF:{article['description']}"
                          for article in three_articles]

    for article in formatted_articles:
        client= Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message= client.messages.create(
            from_= "whatsapp:+141538886",
            body= article,
            to= "whatsapp:+201134966730"
        )
        print(message)










    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

