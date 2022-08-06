import pandas as pd
import os

home_dir = "/home/ybenp"
countries_file = os.path.join(
    home_dir, "CMIP6_data", "population", "national_pop", "countryvalue_blank.csv"
)
countries_df = pd.read_csv(countries_file, usecols=["COUNTRY"])
country_names = [*countries_df["COUNTRY"].values, "World"]

# Classifications from https://www.healthdata.org/sites/default/files/files/Projects/GBD/GBDRegions_countries.pdf

# Super Region: Central Europe, Eastern Europe, and Central Asia
Central_Asia = [
    "Armenia",
    "Azerbaijan",
    "Georgia",
    "Kazakhstan",
    "Kyrgyzstan",
    "Mongolia",
    "Tajikistan",
    "Turkmenistan",
    "Uzbekistan",
]
Central_Europe = [
    "Albania",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Czech Republic",
    "Hungary",
    "Serbia+Montenegro",
    "Macedonia",
    "Poland",
    "Romania",
    "Slovakia",
    "Slovenia",
]
Eastern_Europe = [
    "Belarus",
    "Estonia",
    "Latvia",
    "Lithuania",
    "Moldova",
    "Russia",
    "Ukraine",
]

# Super Region: High-income
Australasia = ["Australia", "New Zealand"]
High_income_Asia_Pacific = ["Brunei", "Japan", "Singapore", "South Korea"]
High_income_North_America = ["Canada", "United States"]
Southern_Latin_America = ["Argentina", "Chile", "Uruguay"]
Western_Europe = [
    "Andorra",
    "Austria",
    "Belgium",
    "Cyprus",
    "Denmark",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Iceland",
    "Ireland",
    "Israel",
    "Italy",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Norway",
    "Portugal",
    "Spain",
    "Sweden",
    "Switzerland",
    "United Kingdom",
]

# Super Region: Latin America and Caribbean
Andean_Latin_America = ["Bolivia", "Ecuador", "Peru"]
Caribbean = [
    "Antigua and Barbuda",
    "The Bahamas",
    "Barbados",
    "Belize",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "Grenada",
    "Guyana",
    "Haiti",
    "Jamaica",
    "Puerto Rico",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Suriname",
    "Trinidad and Tobago",
]
Central_Latin_America = [
    "Colombia",
    "Costa Rica",
    "El Salvador",
    "Guatemala",
    "Honduras",
    "Mexico",
    "Nicaragua",
    "Panama",
    "Venezuela",
]
Tropical_Latin_America = ["Brazil", "Paraguay"]

# Super Region: North Africa and Middle East
North_Africa_and_Middle_East = [
    "Afghanistan",
    "Algeria",
    "Bahrain",
    "Egypt",
    "Iran",
    "Iraq",
    "Jordan",
    "Kuwait",
    "Lebanon",
    "Libya",
    "Morocco",
    "Oman",
    "Qatar",
    "Saudi Arabia",
    "Syria",
    "Tunisia",
    "Turkey",
    "United Arab Emirates",
    "Yemen",
]

# Super Region: South Asia
South_Asia = ["Bangladesh", "Bhutan", "India", "Nepal", "Pakistan"]

# Super Region: Sub-Saharan Africa
Central_Sub_Saharan_Africa = [
    "Angola",
    "Central African Republic",
    "Congo",
    "Democratic Republic of the Congo",
    "Equatorial Guinea",
    "Gabon",
]
Eastern_Sub_Saharan_Africa = [
    "Burundi",
    "Comoros",
    "Djibouti",
    "Eritrea",
    "Ethiopia",
    "Kenya",
    "Madagascar",
    "Malawi",
    "Mozambique",
    "Rwanda",
    "Somalia",
    "Tanzania",
    "Uganda",
    "Zambia",
]
Southern_Sub_Saharan_Africa = [
    "Botswana",
    "Lesotho",
    "Namibia",
    "South Africa",
    "Swaziland",
    "Zimbabwe",
]
Western_Sub_Saharan_Africa = [
    "Benin",
    "Burkina Faso",
    "Cape Verde",
    "Cameroon",
    "Chad",
    "Cote d'Ivoire",
    "The Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
    "Liberia",
    "Mali",
    "Mauritania",
    "Niger",
    "Nigeria",
    "Sao Tome and Principe",
    "Senegal",
    "Sierra Leone",
    "Togo",
]

# Super Region: Southeast Asia, East Asia, and Oceania
East_Asia = ["China", "North Korea"]
Southeast_Asia = [
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Maldives",
    "Mauritius",
    "Myanmar",
    "Philippines",
    "Seychelles",
    "Sri Lanka",
    "Thailand",
    "Timor-Leste",
    "Vietnam",
]

###############################################################

High_SDI = [
    "Switzerland",
    "Norway",
    "Monaco",
    "Germany",
    "Andorra",
    "Luxembourg",
    "Denmark",
    "San Marino",
    "Netherlands",
    "United Arab Emirates",
    "Canada",
    "South Korea",
    "Japan",
    "Iceland",
    "Singapore",
    # "Taiwan (province of China)",
    "Ireland",
    "United States",
    "Belgium",
    "Austria",
    "United Kingdom",
    "Kuwait",
    "Cyprus",
    "Slovenia",
    "Australia",
    "New Zealand",
    "Lithuania",
    "France",
    "Estonia",
    "Czech Republic",
    "Brunei",
    "Qatar",
    "Latvia",
    # "Bermuda",
]

High_middle_SDI = [
    "Slovakia",
    "Puerto Rico",
    # "Guam",
    "Israel",
    "Russia",
    "Italy",
    "Poland",
    "Greece",
    "The Bahamas",
    "Malta",
    "Croatia",
    "Hungary",
    "Saudi Arabia",
    # "Montenegro",
    "Oman",
    "Spain",
    "Serbia+Montenegro",
    # "Northern Mariana Islands",
    "Bulgaria",
    "Trinidad and Tobago",
    # "Greenland",
    "Romania",
    "Cook Islands",
    "Chile",
    "Bahrain",
    "Barbados",
    "Macedonia",
    "Belarus",
    "Ukraine",
    "Portugal",
    "St.Kitts+Nevis",
    "Antigua and Barbuda",
    "Palau",
    "Turkey",
    "Malaysia",
    "Dominica",
    "Jordan",
    "Kazakhstan",
    "Libya",
    "Bosnia and Herzegovina",
    "Seychelles",
    # "American Samoa",
    "Niue",
]

Middle_SDI = [
    "Argentina",
    "Mauritius",
    "Lebanon",
    "Georgia",
    "Uruguay",
    "Moldova",
    "Armenia",
    "Jamaica",
    "Azerbaijan",
    "Sri Lanka",
    "Thailand",
    "Albania",
    "South Africa",
    "Costa Rica",
    "Panama",
    "China",
    "Saint Lucia",
    "Equatorial Guinea",
    "Tunisia",
    "Grenada",
    "Iran",
    "Turkmenistan",
    "Cuba",
    "Fiji",
    "Indonesia",
    "Iraq",
    "Mexico",
    "Peru",
    "Algeria",
    "Egypt",
    "Samoa",
    "Gabon",
    "Brazil",
    "Ecuador",
    "Suriname",
    "Tonga",
    "Paraguay",
    "Botswana",
    "Uzbekistan",
    "Colombia",
    "Syria",
    "Venezuela",
]

Low_middle_SDI = [
    "Guyana",
    "Philippines",
    "Namibia",
    "Vietnam",
    "Mongolia",
    "Belize",
    "Nauru",
    "Kyrgyzstan",
    "Dominican Republic",
    "Tuvalu",
    "Federated States of Micronesia",
    "Swaziland",
    # "Palestine",
    "El Salvador",
    "Bolivia",
    "North Korea",
    "Maldives",
    "Congo",
    "India",
    "Marshall Islands",
    "Ghana",
    "Tajikistan",
    "Morocco",
    "Guatemala",
    "Timor-Leste",
    "Cape Verde",
    "Nicaragua",
    "Myanmar",
    "Nigeria",
    "Lesotho",
    "Honduras",
    "Kenya",
    "Sudan",
    "Zambia",
    "Vanuatu",
    "Mauritania",
    "Laos",
    "Cameroon",
]

Low_SDI = [
    "Zimbabwe",
    "Bangladesh",
    "Cambodia",
    "Angola",
    "Comoros",
    "Bhutan",
    "Djibouti",
    "Pakistan",
    "Haiti",
    "Yemen",
    "Rwanda",
    "Nepal",
    "Tanzania",
    "Solomon Islands",
    "Togo",
    "Papua New Guinea",
    "Cote d'Ivoire",
    "Uganda",
    "The Gambia",
    "Madagascar",
    "Eritrea",
    "Senegal",
    "Malawi",
    "Liberia",
    # "South Sudan",
    "Democratic Republic of the Congo",
    "Guinea-Bissau",
    "Benin",
    "Sierra Leone",
    "Afghanistan",
    "Ethiopia",
    "Guinea",
    "Mozambique",
    "Burundi",
    "Central African Republic",
    "Mali",
    "Burkina Faso",
    "Chad",
    "Niger",
    "Somalia",
]

GBD_regions = [
    # Central Europe, Eastern Europe, and Central Asia
    Central_Asia,
    Central_Europe,
    Eastern_Europe,
    # High-income
    Australasia,
    High_income_Asia_Pacific,
    High_income_North_America,
    Southern_Latin_America,
    Western_Europe,
    # Latin America and Caribbean
    Andean_Latin_America,
    Caribbean,
    Central_Latin_America,
    Tropical_Latin_America,
    # North Africa and Middle East
    North_Africa_and_Middle_East,
    # South Asia
    South_Asia,
    # Sub-Saharan Africa
    Central_Sub_Saharan_Africa,
    Eastern_Sub_Saharan_Africa,
    Southern_Sub_Saharan_Africa,
    Western_Sub_Saharan_Africa,
    # Southeast Asia, East Asia, and Oceania
    East_Asia,
    Southeast_Asia,
]

SDI_regions = [High_SDI, High_middle_SDI, Middle_SDI, Low_middle_SDI, Low_SDI]

regions = SDI_regions

if all(all(country in country_names for country in countries) for countries in regions):
    print("Check complete: all countries are in the official country list")
else:
    for countries in regions:
        for country in countries:
            if country not in country_names:
                print(f"Country {country} not in list!")
