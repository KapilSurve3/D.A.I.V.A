import numpy as np
Rashilords = ("Jupiter","Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn","Saturn")
Rashislist = ("Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces")
FirstH=("Personality","Body","Physique","Self","Nature")
SecondH=("Wealth","Food","Speech","Family","Mouth")
ThirdH=("Siblings","Speech","Conversation","Bravery/Courage","Neck/Collar")
FourthH=("Mother","Home","Estate","Pleasure/Comfort","Chest/Lungs")
FifthH=("Children","Education","Romance","Creativity","Stomach")
SixthH=("Enemies","Competetion","Debt","Disease","Intestine")
SeventhH=("Partner","Buisness","Spouse","Diplomacy","Pelvic/Kidney")
EightH=("Longetivity","Death","OccultScience","Sudden Events","Genitals")
NineH=("Dharma/Duty","Fortune","Ancestor","HigherEducation","Thighs")
TenthH=("Carrier/Profession","Workplace","Father","Authority","Knees")
Eleventh=("Income/Gains","SocialService","Friends","Fulfillment","Shins/Ankle")
TwelthH=("Spirituality","Foreign Lands","Distant/Secluded","Dream/intutions","Feet")
Vimshot=("Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury")
nakshatras = (
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashira",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati"
)
nakshatra_symbols = (
    "Horse's Head",
    "(Yoni) Female Reproductive Organ",
    "(Knife) or Spear",
    "(Cart) or Chariot",
    "(Deer's Head)",
    "(Teardrop) or Diamond",
    "(Bow and Quiver) of Arrows",
    "(Flower, Circle,) or Cow's Udder",
    "(Coiled Serpent)",
    "(Throne) or Palanquin",
    "(Front of a Couch)",
    "(Back Legs of a Couch)",
    "(Hand) or Fist",
    "(Pearl) or Bright Jewel",
    "(Young Plant Shoot,) Coral",
    "(Arch, Potter's Wheel)",
    "(Lotus Flower) or Triumphal Arch",
    "(Earring, Circular) Talisman",
    "(Roots, Umbrella)",
    "(Fan) or Winnowing Basket",
    "(Elephant's Tusk) or Planks of a Bed",
    "(Ear) or Three Footprints in an Ascending Path",
    "(Drum) or Flute",
    "(Empty Circle) or 1000 Flowers",
    "(Two-Faced Man) or Sword",
    "(Back Legs of a Funeral Cot) or Snake in the Water",
    "(Fish) or Drum"
)
#Dasha time in years
vimshottara=(7,20,6,10,7,18,16,19,17)
#Planet time percentage
Suntime = 6/120*100
Moontime = 10/120*100
Marstime = 7/120*100
Mercurytime = 17/120*100
Venustime = 20/120*100
Jupitertime = 16/120*100
Saturntime = 19/120*100
Rahutime = 18/120*100
ketutime = 7/120*100

#This is Rolling function
def roll(num):
  house = num % 12
  if (house==0):
    num =  num - 12
  else:
    num = house
  return num

def roll2(num):
  planet = num % 9
  if(planet == 0):
    num = num - 9
  else:
    num = planet
  return num

#This Function helps to get the nakshatranumber as input
def Nakshatracalculator(nakshatranum):
  nakshatraname = nakshatras[nakshatranum - 1]
  print(nakshatraname)
  if nakshatraname == "Ashwini" or nakshatraname == "Magha" or nakshatraname == "Moola":
    Nlord = "Ketu"
  elif nakshatraname == "Bharani" or nakshatraname == "Purva Phalguni" or nakshatraname == "Purva Ashadha":
    Nlord = "Venus"
  elif nakshatraname == "Krittika" or nakshatraname == "Uttara Phalguni" or nakshatraname == "Uttara Ashadha":
    Nlord = "Sun"
  elif nakshatraname == "Rohini" or nakshatraname == "Hasta" or nakshatraname == "Shravana":
    Nlord = "Moon"
  elif nakshatraname == "Mrigashīrsha" or nakshatraname == "Chitra" or nakshatraname == "Dhanishta":
    Nlord = "Mars"
  elif nakshatraname == "Ardra" or nakshatraname == "Swati" or nakshatraname == "Shatabhisha":
    Nlord = "Rahu"
  elif nakshatraname == "Punarvasu" or nakshatraname == "Vishakha" or nakshatraname == "Purva Bhadrapada":
    Nlord = "Jupiter"
  elif nakshatraname == "Pushya" or nakshatraname == "Anuradha" or nakshatraname == "Uttara Bhadrapada":
    Nlord = "Saturn"
  elif nakshatraname == "Ashlesha" or nakshatraname == "Jyeshtha" or nakshatraname == "Revati":
    Nlord = "Mercury"
  print("The Nakshatra lord is",Nlord)
  return Nlord,nakshatraname

Current_Day = 27
Current_Month = 12
Current_Year = 2023
Current_Dasha = "Jupiter"
Wanted_Dasha = "Venus"
Time_Left = ""
bday = 4
bmon = 12
byear = 2004

def Vimshotcalculator(Wanted_Dasha):
  Counter = 0
  for i in Vimshot:
    Counter = Counter + 1
    print(i)
    Planet = i
    if Planet == Wanted_Dasha:
      print("Match found at",Counter)
      break
    else:
      print("Not found")
  return Counter

def Vimshottaracalculator(Counter):
  Years = 0
  Counter1 = 0
  Total = 0
  for i in vimshottara:
    Counter1 = Counter1 + 1
    if Counter1 == Counter :
      Years = int(i)
    else:
      print(".")
  return Years

def Jyotantar():

  from os import wait

  Rashcounter = 0
  for Rashiname in Rashislist:
    Rashcounter = Rashcounter + 1
    if Rashiname == "Taurus":
      break
  Degrees = 9
  Minute = 56
  Rashinumber = Rashcounter - 1
  cras = Rashinumber * 30
  cdega = cras + Degrees
  cdeg = cdega * 60
  cmin = cdeg + Minute
  print(cmin)
  rashi = float(cmin / 800)
  nakshatranum = int(cmin / 800 + 1)
  print("The Nakshatra number is", nakshatranum)
  rashika = str(rashi)
  rashi, deg = map(int, rashika.split("."))
  diff = cmin - (800 * rashi)
  print(diff)
  if diff <= 200:
      pada = 1
  elif 200 < diff <= 400:
      pada = 2
  elif 400 < diff <= 600:
      pada = 3
  elif 600 < diff <= 800:
      pada = 4
  print("The Nakshatra pada is", pada)
  bhogya = 800 - diff
  print("The Bhogya remaining is", bhogya)
  Nlord, nakshatraname = Nakshatracalculator(nakshatranum)
  Counter = Vimshotcalculator(Nlord)
  Kalah = Vimshottaracalculator(Counter)
  print(Kalah)
  Bhogyakalah = Kalah / 800 * bhogya
  print(Bhogyakalah)
  Salmah = str(Bhogyakalah)
  Sal, mah = map(int, Salmah.split("."))
  if Sal == 0:
    Mah = 0
  else:
    Mah = int(Bhogyakalah % Sal * 12)
  print(
      "The Person born in",
      nakshatraname,
      "Nakshatra of planet",
      Nlord,
      "Remaining bhogyakalh is",
      Sal,
      "years and",
      Mah,
      "months that sum up the person will have ",
      Nlord,
      "Mahadasha First From",
  )


  # Arrays to store values
  dashalist = []
  kallist = []

  Counter2 = Counter - 1
  Counter3 = Counter - 1

  for i in Vimshot:
      Counter4 = roll2(Counter3 + 1)
      if Counter4 == 0:
          Counter4 = 9
      nextkal = Vimshottaracalculator(Counter4)
      nextdasha = Vimshot[roll2(Counter2)]

      # Store values in arrays
      dashalist.append(nextdasha)
      kallist.append(nextkal)

      print(nextdasha)
      print(nextkal)

      Counter2 = Counter2 + 1
      Counter3 = Counter3 + 1

  print(dashalist)
  print(kallist)

  return Sal,Mah,nakshatraname,Nlord,dashalist,kallist
Jyotantar()


import ephem
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
#City longitude and lattitude

def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent="city_locator")

    try:
        location = geolocator.geocode(city_name)
        if location:
            latitude, longitude = location.latitude, location.longitude
            return latitude, longitude
        else:
            print(f"Could not find coordinates for {city_name}.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

city_name = input("Enter Major City Name")
coordinates = get_lat_lon(city_name)

if coordinates:
    print(f"Coordinates for {city_name}: Latitude {coordinates[0]}, Longitude {coordinates[1]}")

#moon locater

def get_moon_position(date,latitude,longitude):
    observer = ephem.Observer()
    observer.date = date
    observer.lat = latitude
    observer.lon = longitude

    moon = ephem.Moon()
    moon.compute(observer)

    sign = ephem.constellation(moon)[1]
    degrees = int(moon.dec / ephem.degree)
    minutes = abs(int((moon.dec / ephem.degree - degrees) * 60))

    return sign, degrees, minutes

# Example: Enter the date in the format 'YYYY-MM-DD HH:MM:SS'
date_input = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
latitude = coordinates[0]
longitude = coordinates[1]
date = ephem.Date(date_input)
bday,nn = map(str,date_input.split(" "))
byear,bmon,bday= map(str,bday.split("-"))
moon_sign, moon_degrees, moon_minutes = get_moon_position(date,latitude,longitude)

print(f"The Moon is in {moon_sign} at {moon_degrees}° {moon_minutes}'")
Sal,Mah,nakshatraname,Nlord,dashalist,kallist = Jyotantar()
print(Sal,Mah)
months = Sal*12 + Mah
print(months)

def subtract_months_from_years(years, months_to_subtract):
    # Convert years to months
    total_months = years * 12

    # Subtract months
    result_months = total_months - months_to_subtract

    # Calculate years and remaining months
    result_years = result_months // 12
    remaining_months = result_months % 12

    result = f"{result_years} years, {remaining_months} months"

    return result,result_years,remaining_months

# Example usage
given_years = kallist[0]
months_to_subtract = months

result,result_years,remaining_months = subtract_months_from_years(given_years, months_to_subtract)
print(f"Original Years: {given_years}")
print(f"Result after subtracting {months_to_subtract} months: {result}")

Newtotalmonths = result_years * 12 + remaining_months

def subtract_months_from_date(original_date_str, months_to_subtract):
    # Convert input string to a datetime object
    original_date = datetime.strptime(original_date_str, '%d-%m-%Y')

    # Subtract months
    new_date = original_date - timedelta(days=months_to_subtract * 30)

    # Format the result as dd-mm-YYYY
    result_date = new_date.strftime('%d-%m-%Y')

    return result_date

# Example usage
given_DATE = bday+"-"+ bmon+"-"
given_date = given_DATE + byear
print(given_date)
months_to_subtract = Newtotalmonths

# Subtract the specified months from the given date
new_date = subtract_months_from_date(given_date, months_to_subtract)

print(f"Original Date: {given_date}")
print(f"Result after subtracting {months_to_subtract} months: {new_date}")

from datetime import datetime, timedelta

# Lists of planets and corresponding numbers
planets = dashalist
numbers = kallist

# Starting date and initial dasha
start_date_str = new_date
start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
current_dasha_index = 0
current_dasha_number = numbers[current_dasha_index]

# Function to calculate the end date for a given dasha
def calculate_end_date(start_date, dasha_number):
    end_date = start_date + timedelta(days=dasha_number * 365)
    return end_date

# List to store dasha information
dasha_info = []

# Loop through the dashas and store information
for i in range(len(planets)):
    end_date = calculate_end_date(start_date, current_dasha_number)
    dasha_info.append({
        'planet': planets[current_dasha_index],
        'start_date': start_date.strftime('%d-%m-%Y'),
        'end_date': end_date.strftime('%d-%m-%Y')
    })

    # Update for the next dasha
    start_date = end_date
    current_dasha_index = (current_dasha_index + 1) % len(planets)
    current_dasha_number = numbers[current_dasha_index]

# Print the list of dasha information
for info in dasha_info:
    print(f"{info['planet']} Dasha: {info['start_date']} to {info['end_date']}")


def split_list(input_list):
    if len(input_list) != 19:
        raise ValueError("Input list must have exactly 19 elements")

    first_array = input_list[:9]
    second_array = input_list[9:18]
    third_array = input_list[18:]

    return first_array, second_array, third_array

def array_difference(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same length")

    difference = [x - y for x, y in zip(array1, array2)]
    return difference

def l3_norm(array):
    squared_sum = np.sum(np.square(array))
    l3_norm = np.sqrt(squared_sum)
    return l3_norm

#the list of Degree of Planets , Positon of Planet and Rashi
list1=[1 for x in range(19)]
list2=[2 for x in range(19)]
arr=split_list(list1)
list2=split_list(list2)
arr2=[]
for x in range(3):
  arr2.append(array_difference(list2[x],arr[x]))
normArr=[]
for x in arr2:
  normArr.append(l3_norm(x))
normArr2=l3_norm(normArr)
normArr2

nearList=[]