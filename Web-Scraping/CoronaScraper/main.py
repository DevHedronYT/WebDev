import requests, kivy, time, os, datetime
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config

os.chdir('/Users/mali/Desktop/Dev/Develop/FavThings/WebDev/PyWeb/WebScrapers/CoronaScrape/V2/')

link = requests.get('https://www.worldometers.info/coronavirus/').text

soup  = BeautifulSoup(link, 'lxml')

title = str(soup.title.text)
new_title = title.split(':')

print(new_title[0], 'from https://www.worldometers.info/coronavirus/')

country_data = []
main_data = soup.find('div', {'class':'main_table_countries_div'})
main_data = main_data.text
country_data.append(main_data)

file = open('COVID.txt', 'w')
file.write(country_data[0])
file.close()

print('\n')

time.sleep(0.15)

file = open('COVID.txt', 'r')
contents = file.readlines()


# Worldwide

Total = []

for i in range(4456, 4462):
    Total.append(contents[i - 1])


Total.pop(1)
Total.pop(2)
Total.pop(3)

Info = ['This Web Scraper Only Tells You The Continental And Worldwide Cases of COVID-19 and Today is ' + str(datetime.date.today())]

Total = ['\n\nThese are the worldwide cases\n', 'Total Cases Are: ' + Total[0], 'Total Deaths Are: ' + Total[1], 'Total Recoveries Are: ' + Total[2]]

print(Info[0])
for i in Total:
    print(i)

# North America

North_America = []

for i in range(4307, 4313):
    North_America.append(contents[i-1])


North_America.pop(1)
North_America.pop(2)
North_America.pop(3)

North_America = ['\nThese are the cases in North America\n', 'Total Cases Are: ' + North_America[0], 'Total Deaths Are: ' + North_America[1], 'Total Recoveries Are: ' + North_America[2]]

for i in North_America:
    print(i)

# Asia

Asia = []

for i in range(4349, 4355):
    Asia.append(contents[i-1])


Asia.pop(1)
Asia.pop(2)
Asia.pop(3)

Asia = ['\nThese are the cases in Asia\n', 'Total Cases Are: ' + Asia[0], 'Total Deaths Are: ' + Asia[1], 'Total Recoveries Are: ' + Asia[2]]

for i in Asia:
    print(i)

# South America

South_America = []

for i in range(4328, 4334):
    South_America.append(contents[i-1])


South_America.pop(1)
South_America.pop(2)
South_America.pop(3)

South_America = ['\nThese are the cases in South America\n', 'Total Cases Are: ' + South_America[0], 'Total Deaths Are: ' + South_America[1], 'Total Recoveries Are: ' + South_America[2]]

for i in South_America:
    print(i)

# Europe

Europe = []

for i in range(4370, 4376):
    Europe.append(contents[i-1])


Europe.pop(1)
Europe.pop(2)
Europe.pop(3)

Europe = ['\nThese are the cases in Europe\n', 'Total Cases Are: ' + Europe[0], 'Total Deaths Are: ' + Europe[1], 'Total Recoveries Are: ' + Europe[2]]

for i in Europe:
    print(i)

# Africa

Africa = []

for i in range(4391, 4397):
    Africa.append(contents[i-1])


Africa.pop(1)
Africa.pop(2)
Africa.pop(3)

Africa = ['\nThese are the cases in Africa\n', 'Total Cases Are: ' + Africa[0], 'Total Deaths Are: ' + Africa[1], 'Total Recoveries Are: ' + Africa[2]]

for i in Africa:
    print(i)

# Australia/Oceania

Australia_or_Oceania = []

for i in range(4412, 4418):
    Australia_or_Oceania.append(contents[i-1])


Australia_or_Oceania.pop(1)
Australia_or_Oceania.pop(2)
Australia_or_Oceania.pop(3)

Australia_or_Oceania = ['\nThese are the cases in Australia or Oceania\n', 'Total Cases Are: ' + Australia_or_Oceania[0], 'Total Deaths Are: ' + Australia_or_Oceania[1], 'Total Recoveries Are: ' + Australia_or_Oceania[2]]

for i in Australia_or_Oceania:
    print(i)

class MyApp(App):

    def build(self):
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')
        list = Info.extend(Total)
        list = Info.extend(North_America)
        list = Info.extend(South_America)
        list = Info.extend(Asia)
        list = Info.extend(Europe)
        list = Info.extend(Africa)
        list = Info.extend(Australia_or_Oceania)
        list = " ".join(Info)
        file = open('DataDisplayed.txt', 'w')
        file.write(list)
        file.close()
        return Label(text = list)




MyApp().run()
