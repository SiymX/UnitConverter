import tkinter as tk
import requests
from tkinter import ttk, messagebox
from pint import UnitRegistry
from PIL import Image, ImageTk

currency_dict = {
    "United States Dollar - USD": "USD",
    "Euro - EUR": "EUR",
    "Australian Dollar - AUD": "AUD",
    "Canadian Dollar - CAD": "CAD",
    "Swiss Franc - CHF": "CHF",
    "Chinese Yuan - CNY": "CNY",
    "British Pound - GBP": "GBP",
    "Indian Rupee - INR": "INR",
    "Japanese Yen - JPY": "JPY",
    "Mexican Peso - MXN": "MXN",
    "UAE Dirham - AED": "AED",
    "Afghan Afghani - AFN": "AFN",
    "Albanian Lek - ALL": "ALL",
    "Armenian Dram - AMD": "AMD",
    "Netherlands Antillean Guilder - ANG": "ANG",
    "Angolan Kwanza - AOA": "AOA",
    "Argentine Peso - ARS": "ARS",
    "Aruban Florin - AWG": "AWG",
    "Azerbaijani Manat - AZN": "AZN",
    "Bosnia-Herzegovina Convertible Mark - BAM": "BAM",
    "Barbadian Dollar - BBD": "BBD",
    "Bangladeshi Taka - BDT": "BDT",
    "Bulgarian Lev - BGN": "BGN",
    "Bahraini Dinar - BHD": "BHD",
    "Burundian Franc - BIF": "BIF",
    "Bermudan Dollar - BMD": "BMD",
    "Brunei Dollar - BND": "BND",
    "Bolivian Boliviano - BOB": "BOB",
    "Brazilian Real - BRL": "BRL",
    "Bahamian Dollar - BSD": "BSD",
    "Bitcoin - BTC": "BTC",
    "Bhutanese Ngultrum - BTN": "BTN",
    "Botswanan Pula - BWP": "BWP",
    "Belarusian Ruble - BYN": "BYN",
    "Belize Dollar - BZD": "BZD",
    "Congolese Franc - CDF": "CDF",
    "Chilean Unit of Account (UF) - CLF": "CLF",
    "Chilean Peso - CLP": "CLP",
    "Chinese Yuan (Offshore) - CNH": "CNH",
    "Colombian Peso - COP": "COP",
    "Costa Rican Colón - CRC": "CRC",
    "Cuban Convertible Peso - CUC": "CUC",
    "Cuban Peso - CUP": "CUP",
    "Cape Verdean Escudo - CVE": "CVE",
    "Czech Koruna - CZK": "CZK",
    "Djiboutian Franc - DJF": "DJF",
    "Danish Krone - DKK": "DKK",
    "Dominican Peso - DOP": "DOP",
    "Algerian Dinar - DZD": "DZD",
    "Egyptian Pound - EGP": "EGP",
    "Eritrean Nakfa - ERN": "ERN",
    "Ethiopian Birr - ETB": "ETB",
    "Fijian Dollar - FJD": "FJD",
    "Falkland Islands Pound - FKP": "FKP",
    "Georgian Lari - GEL": "GEL",
    "Guernsey Pound - GGP": "GGP",
    "Ghanaian Cedi - GHS": "GHS",
    "Gibraltar Pound - GIP": "GIP",
    "Gambian Dalasi - GMD": "GMD",
    "Guinean Franc - GNF": "GNF",
    "Guatemalan Quetzal - GTQ": "GTQ",
    "Guyanaese Dollar - GYD": "GYD",
    "Hong Kong Dollar - HKD": "HKD",
    "Honduran Lempira - HNL": "HNL",
    "Croatian Kuna - HRK": "HRK",
    "Haitian Gourde - HTG": "HTG",
    "Hungarian Forint - HUF": "HUF",
    "Indonesian Rupiah - IDR": "IDR",
    "Israeli New Shekel - ILS": "ILS",
    "Manx pound - IMP": "IMP",
    "Iraqi Dinar - IQD": "IQD",
    "Iranian Rial - IRR": "IRR",
    "Icelandic Króna - ISK": "ISK",
    "Jersey Pound - JEP": "JEP",
    "Jamaican Dollar - JMD": "JMD",
    "Jordanian Dinar - JOD": "JOD",
    "Kenyan Shilling - KES": "KES",
    "Kyrgystani Som - KGS": "KGS",
    "Cambodian Riel - KHR": "KHR",
    "Comorian Franc - KMF": "KMF",
    "North Korean Won - KPW": "KPW",
    "South Korean Won - KRW": "KRW",
    "Kuwaiti Dinar - KWD": "KWD",
    "Cayman Islands Dollar - KYD": "KYD",
    "Kazakhstani Tenge - KZT": "KZT",
    "Laotian Kip - LAK": "LAK",
    "Lebanese Pound - LBP": "LBP",
    "Sri Lankan Rupee - LKR": "LKR",
    "Liberian Dollar - LRD": "LRD",
    "Lesotho Loti - LSL": "LSL",
    "Libyan Dinar - LYD": "LYD",
    "Moroccan Dirham - MAD": "MAD",
    "Moldovan Leu - MDL": "MDL",
    "Malagasy Ariary - MGA": "MGA",
    "Macedonian Denar - MKD": "MKD",
    "Burmese Kyat - MMK": "MMK",
    "Mongolian Tugrik - MNT": "MNT",
    "Macanese Pataca - MOP": "MOP",
    "Mauritanian Ouguiya - MRU": "MRU",
    "Mauritian Rupee - MUR": "MUR",
    "Maldivian Rufiyaa - MVR": "MVR",
    "Malawian Kwacha - MWK": "MWK",
    "Malaysian Ringgit - MYR": "MYR",
    "Mozambican Metical - MZN": "MZN",
    "Namibian Dollar - NAD": "NAD",
    "Nigerian Naira - NGN": "NGN",
    "Nicaraguan Córdoba - NIO": "NIO",
    "Norwegian Krone - NOK": "NOK",
    "Nepalese Rupee - NPR": "NPR",
    "New Zealand Dollar - NZD": "NZD",
    "Omani Rial - OMR": "OMR",
    "Panamanian Balboa - PAB": "PAB",
    "Peruvian Sol - PEN": "PEN",
    "Papua New Guinean Kina - PGK": "PGK",
    "Philippine Peso - PHP": "PHP",
    "Pakistani Rupee - PKR": "PKR",
    "Polish Złoty - PLN": "PLN",
    "Paraguayan Guarani - PYG": "PYG",
    "Qatari Riyal - QAR": "QAR",
    "Romanian Leu - RON": "RON",
    "Serbian Dinar - RSD": "RSD",
    "Russian Ruble - RUB": "RUB",
    "Rwandan Franc - RWF": "RWF",
    "Saudi Riyal - SAR": "SAR",
    "Solomon Islands Dollar - SBD": "SBD",
    "Seychellois Rupee - SCR": "SCR",
    "Sudanese Pound - SDG": "SDG",
    "Swedish Krona - SEK": "SEK",
    "Singapore Dollar - SGD": "SGD",
    "St. Helena Pound - SHP": "SHP",
    "Sierra Leonean Leone - SLL": "SLL",
    "Somali Shilling - SOS": "SOS",
    "Surinamese Dollar - SRD": "SRD",
    "South Sudanese Pound - SSP": "SSP",
    "São Tomé & Príncipe Dobra - STD": "STD",
    "São Tomé & Príncipe Dobra (new) - STN": "STN",
    "Salvadoran Colón - SVC": "SVC",
    "Syrian Pound - SYP": "SYP",
    "Swazi Lilangeni - SZL": "SZL",
    "Thai Baht - THB": "THB",
    "Tajikistani Somoni - TJS": "TJS",
    "Turkmenistani Manat - TMT": "TMT",
    "Tunisian Dinar - TND": "TND",
    "Tongan Paʻanga - TOP": "TOP",
    "Turkish Lira - TRY": "TRY",
    "Trinidad & Tobago Dollar - TTD": "TTD",
    "New Taiwan Dollar - TWD": "TWD",
    "Tanzanian Shilling - TZS": "TZS",
    "Ukrainian Hryvnia - UAH": "UAH",
    "Ugandan Shilling - UGX": "UGX",
    "Uruguayan Peso - UYU": "UYU",
    "Uzbekistani Som - UZS": "UZS"
}

media_storage_dict = {
    "floppy_disk_3.5_DD": 720 * 1024,
    "floppy_disk_3.5_HD": 1.44 * 1024 ** 2,
    "floppy_disk_3.5_ED": 2.88 * 1024 ** 2,
    "floppy_disk_5.25_DD": 360 * 1024,
    "floppy_disk_5.25_HD": 1.2 * 1024 ** 2,
    "Zip_100": 100 * 1024 ** 2,
    "Zip_250": 250 * 1024 ** 2,
    "Jaz_1GB": 1 * 1024 ** 3,
    "Jaz_2GB": 2 * 1024 ** 3,
    "CD_74_minute": 650 * 1024 ** 2,
    "CD_80_minute": 700 * 1024 ** 2,
    "DVD_1_layer_1_side": 4.7 * 1024 ** 3,
    "DVD_2_layer_1_side": 9 * 1024 ** 3,
    "DVD_1_layer_2_side": 9.4 * 1024 ** 3,
    "DVD_2_layer_2_side": 18 * 1024 ** 3,
}

digital_storage_conversion_dict = {
    "bit": 1,
    "kilobit": 1e3,
    "megabit": 1e6,
    "gigabit": 1e9,
    "terabit": 1e12,
    "petabit": 1e15,
    "exabit": 1e18,
    "byte": 8,
    "kilobyte": 8e3,
    "megabyte": 8e6,
    "gigabyte": 8e9,
    "terabyte": 8e12,
    "petabyte": 8e15,
    "exabyte": 8e18,
}

energy_conversion_dict = {
    "joule": 1,
    "kilojoule": 1e3,
    "kilowatt-hour": 3.6e6,
    "watt-hour": 3.6e3,
    "calorie": 4.184,
    "horsepower hour": 2.684519537696172792e6,
    "Btu (IT)": 1.05505585262e3,
    "Btu (th)": 1.0543502644888888889e3,
    "gigajoule": 1e9,
    "megajoule": 1e6,
    "millijoule": 1e-3,
    "microjoule": 1e-6,
    "nanojoule": 1e-9,
    "attojoule": 1e-18,
    "megaelectron-volt": 1.602176634e-13,
    "kiloelectron-volt": 1.602176634e-16,
    "erg": 1e-7,
    "gigawatt-hour": 3.6e12,
    "megawatt-hour": 3.6e9,
    "kilowatt-second": 1e3,
    "watt": 1,
    "second": 1,
    "newton meter": 1,
    "kilocalorie (IT)": 4.184e3,
    "kilocalorie (th)": 4.184e3,
    "calorie (IT)": 4.184,
    "calorie (th)": 4.184,
    "mega Btu (IT)": 1.05505585262e6,
    "ton hour (refrigeration)": 3.516853e9,
    "fuel oil equivalent @kiloliter": 4.1868e10,
    "fuel oil equivalent @barrel (US)": 5.63605e9,
    "gigaton [Gton]": 4.184e21,
    "megaton [Mton]": 4.184e18,
    "kiloton [kton]": 4.184e15,
    "ton (explosives)": 4.184e9,
    "dyne centimeter": 1e-7,
    "gram force centimeter": 9.80665e-4,
    "kilogram force centimeter": 9.80665e-2,
    "kilogram force meter": 9.80665,
    "kilopond meter": 9.80665,
    "pound force foot": 1.3558179483314004,
    "pound force inch": 0.11298482902845003,
    "ounce force inch": 0.007061551814277506,
    "foot-pound": 1.3558179483314004,
    "inch-pound": 0.11298482902845003,
    "inch-ounce": 0.007061551814277506,
    "poundal foot": 0.0421401100938048,
    "therm": 1.05506e8,
    "therm (EC)": 1.05506e8,
    "therm (US)": 1.054804e8,
    "Hatree Energy": 4.3597447222071e-18,
    "Rydber Constant": 2.17987236110355e-18,
}

number_conversion_dict = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hexadecimal": 16,
    "base-2": 2,
    "base-3": 3,
    "base-4": 4,
    "base-5": 5,
    "base-6": 6,
    "base-7": 7,
    "base-8": 8,
    "base-9": 9,
    "base-10": 10,
    "base-11": 11,
    "base-12": 12,
    "base-13": 13,
    "base-14": 14,
    "base-15": 15,
    "base-16": 16,
    "base-17": 17,
    "base-18": 18,
    "base-19": 19,
    "base-20": 20,
    "base-21": 21,
    "base-22": 22,
    "base-23": 23,
    "base-24": 24,
    "base-25": 25,
    "base-26": 26,
    "base-27": 27,
    "base-28": 28,
    "base-29": 29,
    "base-30": 30,
    "base-31": 31,
    "base-32": 32,
    "base-33": 33,
    "base-34": 34,
    "base-35": 35,
    "base-36": 36,
}

area_conversion_dict = {
    "square_meter": 1,
    "square_kilometer": 1e+6,
    "square_centimeter": 1e-4,
    "square_millimeter": 1e-6,
    "square_micrometer": 1e-12,
    "hectare": 1e+4,
    "square_mile": 2.59e+6,
    "square_yard": 0.836127,
    "square_foot": 0.092903,
    "square_inch": 0.00064516
}

volume_conversion_dict = {
    "cubic_meter": 1,
    "cubic_kilometer": 1e+9,
    "cubic_centimeter": 1e-6,
    "cubic_millimeter": 1e-9,
    "liter": 1e-3,
    "milliliter": 1e-6,
    "US_gallon": 0.00378541,
    "US_quart": 0.000946353,
    "US_pint": 0.000473176,
    "US_cup": 0.000236588,
    "US_fluid_ounce": 0.0000295735,
    "US_tablespoon": 0.0000147868,
    "US_teaspoon": 0.00000492892,
    "imperial_gallon": 0.00454609,
    "imperial_quart": 0.00113652,
    "imperial_pint": 0.000568261,
    "imperial_fluid_ounce": 0.0000284131,
    "imperial_tablespoon": 0.0000177582,
    "imperial_teaspoon": 0.00000591939,
    "cubic_mile": 4.16818e+9,
    "cubic_yard": 0.764555,
    "cubic_foot": 0.0283168,
    "cubic_inch": 0.0000163871
}

weight_mass_conversion_dict = {
    "kilogram": 1,
    "gram": 1e-3,
    "milligram": 1e-6,
    "ton": 1e3,
    "pound": 0.453592,
    "ounce": 0.0283495,
    "carat": 0.0002,
    "ton (US)": 0.907185,
    "ton (UK)": 1.01605,
    "atomic mass unit": 1.66053906660e-27,
    "exagram": 1e18,
    "petagram": 1e15,
    "teragram": 1e12,
    "gigagram": 1e9,
    "megagram": 1e6,
    "hectogram": 0.1,
    "dekagram": 0.01,
    "decigram": 0.0001,
    "centigram": 0.00001,
    "microgram": 1e-9,
    "nanogram": 1e-12,
    "picogram": 1e-15,
    "femtogram": 1e-18,
    "attogram": 1e-21,
    "dalton": 1.660539040e-27,
    "kilogram-force square second/meter": 9.80665,
    "kilopound": 453.592,
    "kip": 453.592,
    "slug": 14.5939,
    "pound-force square second/meter": 0.453592,
    "pound (troy or apothecary)": 0.373242,
    "poundal": 0.0152519,
    "ton (assay) (US)": 0.0291667,
    "ton (assay) (UK)": 0.0260417,
    "kiloton (metric)": 1e6,
    "quintal (metric)": 100,
    "hundredweight (US)": 45.3592,
    "hundredweight (UK)": 50.8023,
    "quarter (US)": 11.3398,
    "quarter (UK)": 12.7006,
    "stone (US)": 6.35029,
    "stone (UK)": 6.35029,
    "tonne": 1e3,
    "pennyweight": 0.00155517,
    "scruple": 0.00129598,
    "grain": 6.47989e-5,
    "gamma": 1e-9,
    "planck mass": 2.176434e-8,
    "proton mass": 1.67262192e-27,
    "neutron mass": 1.67492749804e-27,
    "deuteron mass": 3.3435837724e-27,
    "earth's mass": 5.972e24,
    "sun's mass": 1.989e30
}

power_conversion_dict = {
    'watt (W)': 1,
    'kilowatt (kW)': 1e3,
    'megawatt (MW)': 1e6,
    'gigawatt (GW)': 1e9,
    'terawatt (TW)': 1e12,
    'petawatt (PW)': 1e15,
    'exawatt (EW)': 1e18,
    'hectowatt (hW)': 1e2,
    'dekawatt (daW)': 1e1,
    'deciwatt (dW)': 1e-1,
    'centiwatt (cW)': 1e-2,
    'milliwatt (mW)': 1e-3,
    'microwatt (μW)': 1e-6,
    'nanowatt (nW)': 1e-9,
    'picowatt (pW)': 1e-12,
    'femtowatt (fW)': 1e-15,
    'attowatt (aW)': 1e-18,
    'horsepower (UK) [hp (UK)]': 745.7,
    'horsepower [hp (550 ft*lbf/s)]': 745.699872,
    'horsepower (metric) [hp (metric)]': 735.49875,
    'horsepower (boiler) [hp (boiler)]': 9809.5,
    'horsepower (electric) [hp (electric)]': 746,
    'horsepower (water) [hp (water)]': 746.043,
    'pferdestarke (ps)': 735.49875,
    'Btu (IT)/hour [Btu/h]': 0.29307107,
    'Btu (IT)/minute [Btu/min]': 17.584267,
    'Btu (IT)/second [Btu/s]': 1055.05585,
    'joule/second [J/s]': 1,
    'kilovolt ampere [kV*A]': 1e3,
    'volt ampere [V*A]': 1,
    'newton meter/second': 1,
    'kilocalorie (IT)/hour [kcal/h]': 1.163,
    'kilocalorie (IT)/minute': 69.78,
    'kilocalorie (IT)/second': 4184,
    'foot pound-force/hour': 0.0003766161,
    'foot pound-force/minute': 0.02259697,
    'foot pound-force/second': 1.35582,
    'erg/second [erg/s]': 1e-7,
    'ton (refrigeration)': 3516.85,
    'calorie (IT)/hour [cal/h]': 0.001163,
    'calorie (IT)/minute [cal/min]': 0.06978,
    'calorie (IT)/second [cal/s]': 4.184,
    'MBtu (IT)/hour [Mbtu/h]': 293071.07,
    'MBH': 293071.07,
    'joule/hour [J/h]': 0.000277777778,
    'joule/minute [J/min]': 0.0166666667,
    'kilojoule/hour [kJ/h]': 0.277777778,
    'kilojoule/minute [kJ/min]': 16.6666667
}


def convert_currency(amount, from_currency, to_currency):
    from_currency_code = from_currency
    to_currency_code = to_currency

    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency_code}')
    data = response.json()
    rate = data['rates'][to_currency_code]
    converted_amount = amount * rate
    return converted_amount


def create_gradient(width, height):
    base = Image.new('RGB', (width, height), '#2C3E50')
    top = Image.new('RGB', (width, height), '#4CA1AF')
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend(list(int(255 * (y / height)) for x in range(width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.ureg = UnitRegistry()

        self.root.title("Unit Converter | Created By: Siym")
        self.root.geometry("900x900")

        gradient = create_gradient(900, 900)
        self.background_image = ImageTk.PhotoImage(gradient)
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        welcome_label = ttk.Label(self.root, text="Welcome to the Unit Converter.", font=("Arial", 24, "bold"))
        welcome_label.grid(column=0, row=0, pady=10, padx=10)

        self.unit_categories = {
            "Length": ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard",
                       "foot", "inch", "light_year"],
            "Temperature": ["celsius", "kelvin", "fahrenheit"],
            "Area": ["square_meter", "square_kilometer", "square_centimeter", "square_millimeter", "square_micrometer",
                     "hectare", "square_mile", "square_yard", "square_foot", "square_inch"],
            "Volume": ["cubic_meter", "cubic_kilometer", "cubic_centimeter", "cubic_millimeter", "liter", "milliliter",
                       "US_gallon", "US_quart", "US_pint", "US_cup", "US_fluid_ounce", "US_tablespoon", "US_teaspoon",
                       "imperial_gallon", "imperial_quart", "imperial_pint", "imperial_fluid_ounce",
                       "imperial_tablespoon", "imperial_teaspoon", "cubic_mile", "cubic_yard", "cubic_foot",
                       "cubic_inch"],
            "Weight and Mass": list(weight_mass_conversion_dict.keys()),
            "Time": ["second", "millisecond", "microsecond", "picosecond", "minute", "hour", "day", "week", "month",
                     "year"],
            "Mathematics": ["degree", "radian", "grad", "minute", "second", "gon", "sign", "mil", "revolution",
                            "circle",
                            "turn", "quadrant", "right_angle", "sextant"],
            "Torque": ["newton*meter", "newton*centimeter", "newton*millimeter", "kilonewton*meter", "dyne*meter",
                       "dyne*centimeter", "dyne*millimeter", "kilogram_force*meter", "kilogram_force*centimeter",
                       "kilogram_force*millimeter", "gram_force*meter", "gram_force*centimeter",
                       "gram_force*millimeter",
                       "ounce_force*foot", "ounce_force*inch", "pound_force*foot", "pound_force*inch"],

            "Power": ["watt (W)", "exawatt (EW)", "petawatt (PW)", "terawatt (TW)", "gigawatt (GW)", "megawatt (MW)",
                      "kilowatt (kW)", "hectowatt (hW)", "dekawatt (daW)", "deciwatt (dW)", "centiwatt (cW)",
                      "milliwatt (mW)",
                      "microwatt (μW)", "nanowatt (nW)", "picowatt (pW)", "femtowatt (fW)", "attowatt (aW)",
                      "horsepower (UK) [hp (UK)]", "horsepower [hp (550 ft*lbf/s)]",
                      "horsepower (metric) [hp (metric)]",
                      "horsepower (boiler) [hp (boiler)]", "horsepower (electric) [hp (electric)]",
                      "horsepower (water) [hp (water)]", "pferdestarke (ps)", "Btu (IT)/hour [Btu/h]",
                      "Btu (IT)/minute [Btu/min]", "Btu (IT)/second [Btu/s]", "Btu (th)/hour [Btu (th)/h]",
                      "Btu (th)/second [Btu (th)/s]", "Btu (th)/minute", "MBtu (IT)/hour [MBtu/h]", "MBH",
                      "ton (refrigeration)", "kilocalorie (IT)/hour [kcal/h]", "kilocalorie (IT)/minute",
                      "kilocalorie (IT)/second", "kilocalorie (th)/hour", "kilocalorie (th)/minute",
                      "kilocalorie (th)/second", "calorie (IT)/hour [cal/h]", "calorie (IT)/minute [cal/min]",
                      "calorie (IT)/second [cal/s]", "calorie (th)/hour [cal (th)/h]", "calorie (th)/minute",
                      "calorie (th)/second", "foot pound-force/hour", "foot pound-force/minute",
                      "foot pound-force/second", "pound-foot/hour [lbf*ft/h]", "pound-foot/minute", "pound-foot/second",
                      "erg/second [erg/s]", "kilovolt ampere [kV*A]", "volt ampere [V*A]", "newton meter/second",
                      "joule/second [J/s]", "exajoule/second [EJ/s]", "petajoule/second [PJ/s]",
                      "terajoule/second [TJ/s]", "gigajoule/second [GJ/s]", "megajoule/second [MJ/s]",
                      "kilojoule/second [kJ/s]", "hectojoule/second [hJ/s]", "dekajoule/second [daJ/s]",
                      "decijoule/second [dJ/s]", "centijoule/second [cJ/s]", "millijoule/second [mJ/s]",
                      "microjoule/second [μJ/s]", "nanojoule/second [nJ/s]", "picojoule/second [pJ/s]",
                      "femtojoule/second [fJ/s]", "attojoule/second [aJ/s]", "joule/hour [J/h]", "joule/minute [J/min]",
                      "kilojoule/hour [kJ/h]", "kilojoule/minute [kJ/min]"],

            "Currency": [
                "USD - United States Dollar",
                "EUR - Euro",
                "AUD - Australian Dollar",
                "CAD - Canadian Dollar",
                "CHF - Swiss Franc",
                "CNY - Chinese Yuan",
                "GBP - British Pound",
                "INR - Indian Rupee",
                "JPY - Japanese Yen",
                "MXN - Mexican Peso",
                "AED - UAE Dirham",
                "AFN - Afghan Afghani",
                "ALL - Albanian Lek",
                "AMD - Armenian Dram",
                "ANG - Netherlands Antillean Guilder",
                "AOA - Angolan Kwanza",
                "ARS - Argentine Peso",
                "AWG - Aruban Florin",
                "AZN - Azerbaijani Manat",
                "BAM - Bosnia-Herzegovina Convertible Mark",
                "BBD - Barbadian Dollar",
                "BDT - Bangladeshi Taka",
                "BGN - Bulgarian Lev",
                "BHD - Bahraini Dinar",
                "BIF - Burundian Franc",
                "BMD - Bermudan Dollar",
                "BND - Brunei Dollar",
                "BOB - Bolivian Boliviano",
                "BRL - Brazilian Real",
                "BSD - Bahamian Dollar",
                "BTC - Bitcoin",
                "BTN - Bhutanese Ngultrum",
                "BWP - Botswanan Pula",
                "BYN - Belarusian Ruble",
                "BZD - Belize Dollar",
                "CDF - Congolese Franc",
                "CLF - Chilean Unit of Account (UF)",
                "CLP - Chilean Peso",
                "CNH - Chinese Yuan (Offshore)",
                "COP - Colombian Peso",
                "CRC - Costa Rican Colón",
                "CUC - Cuban Convertible Peso",
                "CUP - Cuban Peso",
                "CVE - Cape Verdean Escudo",
                "CZK - Czech Koruna",
                "DJF - Djiboutian Franc",
                "DKK - Danish Krone",
                "DOP - Dominican Peso",
                "DZD - Algerian Dinar",
                "EGP - Egyptian Pound",
                "ERN - Eritrean Nakfa",
                "ETB - Ethiopian Birr",
                "FJD - Fijian Dollar",
                "FKP - Falkland Islands Pound",
                "GEL - Georgian Lari",
                "GGP - Guernsey Pound",
                "GHS - Ghanaian Cedi",
                "GIP - Gibraltar Pound",
                "GMD - Gambian Dalasi",
                "GNF - Guinean Franc",
                "GTQ - Guatemalan Quetzal",
                "GYD - Guyanaese Dollar",
                "HKD - Hong Kong Dollar",
                "HNL - Honduran Lempira",
                "HRK - Croatian Kuna",
                "HTG - Haitian Gourde",
                "HUF - Hungarian Forint",
                "IDR - Indonesian Rupiah",
                "ILS - Israeli New Shekel",
                "IMP - Manx pound",
                "IQD - Iraqi Dinar",
                "IRR - Iranian Rial",
                "ISK - Icelandic Króna",
                "JEP - Jersey Pound",
                "JMD - Jamaican Dollar",
                "JOD - Jordanian Dinar",
                "KES - Kenyan Shilling",
                "KGS - Kyrgystani Som",
                "KHR - Cambodian Riel",
                "KMF - Comorian Franc",
                "KPW - North Korean Won",
                "KRW - South Korean Won",
                "KWD - Kuwaiti Dinar",
                "KYD - Cayman Islands Dollar",
                "KZT - Kazakhstani Tenge",
                "LAK - Laotian Kip",
                "LBP - Lebanese Pound",
                "LKR - Sri Lankan Rupee",
                "LRD - Liberian Dollar",
                "LSL - Lesotho Loti",
                "LYD - Libyan Dinar",
                "MAD - Moroccan Dirham",
                "MDL - Moldovan Leu",
                "MGA - Malagasy Ariary",
                "MKD - Macedonian Denar",
                "MMK - Burmese Kyat",
                "MNT - Mongolian Tugrik",
                "MOP - Macanese Pataca",
                "MRU - Mauritanian Ouguiya",
                "MUR - Mauritian Rupee",
                "MVR - Maldivian Rufiyaa",
                "MWK - Malawian Kwacha",
                "MYR - Malaysian Ringgit",
                "MZN - Mozambican Metical",
                "NAD - Namibian Dollar",
                "NGN - Nigerian Naira",
                "NIO - Nicaraguan Córdoba",
                "NOK - Norwegian Krone",
                "NPR - Nepalese Rupee",
                "NZD - New Zealand Dollar",
                "OMR - Omani Rial",
                "PAB - Panamanian Balboa",
                "PEN - Peruvian Sol",
                "PGK - Papua New Guinean Kina",
                "PHP - Philippine Peso",
                "PKR - Pakistani Rupee",
                "PLN - Polish Złoty",
                "PYG - Paraguayan Guarani",
                "QAR - Qatari Riyal",
                "RON - Romanian Leu",
                "RSD - Serbian Dinar",
                "RUB - Russian Ruble",
                "RWF - Rwandan Franc",
                "SAR - Saudi Riyal",
                "SBD - Solomon Islands Dollar",
                "SCR - Seychellois Rupee",
                "SDG - Sudanese Pound",
                "SEK - Swedish Krona",
                "SGD - Singapore Dollar",
                "SHP - St. Helena Pound",
                "SLL - Sierra Leonean Leone",
                "SOS - Somali Shilling",
                "SRD - Surinamese Dollar",
                "SSP - South Sudanese Pound",
                "STD - São Tomé & Príncipe Dobra",
                "STN - São Tomé & Príncipe Dobra (new)",
                "SVC - Salvadoran Colón",
                "SYP - Syrian Pound",
                "SZL - Swazi Lilangeni",
                "THB - Thai Baht",
                "TJS - Tajikistani Somoni",
                "TMT - Turkmenistani Manat",
                "TND - Tunisian Dinar",
                "TOP - Tongan Paʻanga",
                "TRY - Turkish Lira",
                "TTD - Trinidad & Tobago Dollar",
                "TWD - New Taiwan Dollar",
                "TZS - Tanzanian Shilling",
                "UAH - Ukrainian Hryvnia",
                "UGX - Ugandan Shilling",
                "UYU - Uruguayan Peso",
                "UZS - Uzbekistani Som"
            ],

            "Digital Storage": list(digital_storage_conversion_dict.keys()) + list(media_storage_dict.keys()),
            "Numbers": list(number_conversion_dict.keys()),
            "Energy": [
                "joule", "kilojoule", "kilowatt-hour", "watt-hour", "calorie", "horsepower hour", "Btu (IT)",
                "Btu (th)",
                "gigajoule", "megajoule", "millijoule", "microjoule", "nanojoule", "attojoule", "megaelectron-volt",
                "kiloelectron-volt", "erg", "gigawatt-hour", "megawatt-hour", "kilowatt-second", "watt", "second",
                "newton meter", "horsepower hour", "kilocalorie (IT)", "kilocalorie (th)", "calorie (IT)",
                "calorie (th)", "mega Btu (IT)", "ton hour (refrigeration)", "fuel oil equivalent @kiloliter",
                "fuel oil equivalent @barrel (US)", "gigaton [Gton]", "megaton [Mton]", "kiloton [kton]",
                "ton (explosives)", "dyne centimeter", "gram force centimeter", "kilogram force centimeter",
                "kilogram force meter", "kilopond meter", "pound force foot", "pound force inch", "ounce force inch",
                "foot-pound", "inch-pound", "inch-ounce", "poundal foot", "therm", "therm (EC)", "therm (US)",
                "Hatree Energy", "Rydber Constant"
            ],

        }

        self.category_var = tk.StringVar()
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()

        self.category_dropdown = ttk.Combobox(self.root, state="readonly", textvariable=self.category_var,
                                              font=("Helvetica", 15))
        self.category_dropdown['values'] = ["Select Unit"] + list(self.unit_categories.keys())
        self.category_dropdown.current(0)
        self.category_dropdown.grid(column=0, row=1, pady=10, padx=10)
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_unit_dropdowns)

        self.from_unit_dropdown = ttk.Combobox(self.root, state="readonly", textvariable=self.from_unit_var,
                                               font=("Helvetica", 15))
        self.from_unit_dropdown.grid(column=0, row=2, pady=10, padx=10)
        self.from_unit_dropdown.bind("<<ComboboxSelected>>", self.update_to_unit_dropdown)

        self.to_unit_dropdown = ttk.Combobox(self.root, state="readonly", textvariable=self.to_unit_var,
                                             font=("Helvetica", 15))
        self.to_unit_dropdown.grid(column=0, row=3, pady=10, padx=10)

        self.entry_value = tk.StringVar()
        self.entry = ttk.Entry(self.root, textvariable=self.entry_value, font=("", 10, "italic"))
        self.entry.grid(column=0, row=4, pady=10, padx=10)

        self.entry.insert(0, "Enter your input..")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.set_placeholder)

        convert_button = ttk.Button(self.root, text="Convert", command=self.convert_units)
        convert_button.grid(column=0, row=5, pady=10, padx=10)

        self.result_frame = ttk.Frame(self.root)
        self.result_frame.grid(column=1, row=0, rowspan=6, padx=20)

        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.pack(expand=True)

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter your input..":
            self.entry.delete(0, "end")
            self.entry.configure(font=("", 10))

    def set_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Enter your input..")
            self.entry.configure(font=("", 10, "italic"))

    def update_unit_dropdowns(self, event):
        category = self.category_var.get()
        if category != "Select Unit":
            self.from_unit_dropdown['values'] = ["Select Conversion"] + self.unit_categories[category]
            self.from_unit_dropdown.current(0)
            self.to_unit_dropdown['values'] = []

    def update_to_unit_dropdown(self, event):
        category = self.category_var.get()
        from_unit = self.from_unit_var.get()
        if from_unit != "Select Conversion":
            to_units = ["Select Conversion"] + [unit for unit in self.unit_categories[category] if unit != from_unit]
            self.to_unit_dropdown['values'] = to_units
            self.to_unit_dropdown.current(0)

    def baseconvert(self, number, base_from, base_to):
        if base_from < 2 or base_to < 2 or base_from > 36 or base_to > 36:
            raise ValueError("Invalid input")

        digits = "0123456789abcdefghijklmnopqrstuvwxyz"

        base10_num = 0
        for digit in str(number):
            base10_num = base10_num * base_from + digits.index(digit.lower())

        result = ""
        while base10_num > 0:
            base10_num, remainder = divmod(base10_num, base_to)
            result = digits[remainder] + result

        return result or "0"

    def convert_units(self):
        from_value = self.entry_value.get()
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        if not from_value or from_value == "Enter your input..":
            messagebox.showerror("Error", "Please enter a valid input")
        elif from_unit and to_unit and from_unit != "Select Conversion" and to_unit != "Select Conversion":
            try:
                if self.category_var.get() == "Currency":
                    converted_value = convert_currency(from_value, from_unit.split()[0], to_unit.split()[0])
                elif self.category_var.get() == "Temperature" and from_unit == "fahrenheit" and to_unit == "celsius":
                    converted_value = (float(from_value) - 32) * 5 / 9
                elif self.category_var.get() == "Temperature" and from_unit == "celsius" and to_unit == "fahrenheit":
                    converted_value = (float(from_value) * 9 / 5) + 32
                elif self.category_var.get() == "Digital Storage":
                    if from_unit in media_storage_dict:
                        from_value = float(from_value) * media_storage_dict[from_unit]
                        from_unit = 'bytes'
                    if to_unit in media_storage_dict:
                        converted_value = (from_value * self.ureg(from_unit)).to('bytes').magnitude
                        converted_value /= media_storage_dict[to_unit]
                    else:
                        converted_value = (from_value * self.ureg(from_unit)).to(to_unit).magnitude
                elif self.category_var.get() == "Numbers":
                    base_from = number_conversion_dict[from_unit]
                    base_to = number_conversion_dict[to_unit]
                    converted_value = self.baseconvert(from_value, base_from, base_to)
                elif from_unit in area_conversion_dict and to_unit in area_conversion_dict:
                    conversion_factor = area_conversion_dict[from_unit] / area_conversion_dict[to_unit]
                    converted_value = float(from_value) * conversion_factor
                elif from_unit in volume_conversion_dict and to_unit in volume_conversion_dict:
                    conversion_factor = volume_conversion_dict[from_unit] / volume_conversion_dict[to_unit]
                    converted_value = float(from_value) * conversion_factor
                elif self.category_var.get() == "Weight and Mass":
                    conversion_factor = weight_mass_conversion_dict[from_unit] / weight_mass_conversion_dict[to_unit]
                    converted_value = float(from_value) * conversion_factor
                elif from_unit in power_conversion_dict and to_unit in power_conversion_dict:
                    conversion_factor = power_conversion_dict[from_unit] / power_conversion_dict[to_unit]
                    converted_value = float(from_value) * conversion_factor
                elif from_unit in energy_conversion_dict and to_unit in energy_conversion_dict:
                    conversion_factor = energy_conversion_dict[from_unit] / energy_conversion_dict[to_unit]
                    converted_value = float(from_value) * conversion_factor
                else:
                    converted_value = (float(from_value) * self.ureg(from_unit)).to(to_unit).magnitude
                self.result_label.configure(text=str(converted_value))
            except Exception as e:
                self.result_label.configure(text="Error: " + str(e))


root = tk.Tk()
UnitConverter(root)
root.mainloop()
