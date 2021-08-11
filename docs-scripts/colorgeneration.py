colorsFirstCol = {
    "Apricot": "FBCEB1",
    "Aquamarine": "7FFFD0",
    "Bittersweet": "FE6F5E",
    "Black": "000000",
    "Blue": "0000FF",
    "BlueGreen": "00DDDD",
    "BlueViolet": "8A2BE2",
    "BrickRed": "CB4154",
    "Brown": "964B00",
    "BurntOrange": "CC5500",
    "CadetBlue": "5F9EA0",
    "CarnationPink": "FFA6C9",
    "Cerulean": "007BA7",
    "CornflowerBlue": "6495ED",
    "Cyan": "00FFFF",
    "Dandelion": "F0E130",
    "DarkOrchid": "9932CC"
}

colorsSecondCol = {
    "Emerald": "50C878",
    "ForestGreen": "014421",
    "Fuchsia": "FF00FF",
    "Goldenrod": "DAA520",
    "Gray": "808080",
    "Green": "00A550",
    "GreenYellow": "ADFF2F",
    "JungleGreen": "29AB87",
    "Lavender": "CCCCFF",
    "LimeGreen": "32CD32",
    "Magenta": "FF00FF",
    "Mahogany": "C04000",
    "Maroon": "800000",
    "Melon": "FDBCB4",
    "MidnightBlue": "191970",
    "Mulberry": "C54B8C",
    "NavyBlue": "000080"
}

colorsThirdCol = {
    "OliveGreen": "808000",
    "Orange": "FB9902",
    "OrangeRed": "FF4500",
    "Orchid": "DA70D6",
    "Peach": "FFE5B4",
    "Periwinkle": "CCCCFF",
    "PineGreen": "01796F",
    "Plum": "8E4585",
    "ProcessBlue": "0085CA",
    "Purple": "800080",
    "RawSienna": "D68A59",
    "Red": "FF0000",
    "RedOrange": "FF4500",
    "RedViolet": "C71585",
    "Rhodamine": "E60094",
    "RoyalBlue": "4169E1",
    "RoyalPurple": "7851A9"
}

colorsFourthCol = {
    "RubineRed": "D10056",
    "Salmon": "FF8C69",
    "SeaGreen": "2E8B57",
    "Sepia": "704214",
    "YellowOrange": "FFAE42",
    "SkyBlue": "87CEEB",
    "SpringGreen": "00FF7F",
    "Tan": "D2B48C",
    "TealBlue": "367588",
    "Thistle": "D8BFD8",
    "Turquoise": "30D5C8",
    "Violet": "8F00FF",
    "VioletRed": "C71585",
    "White": "FFFFFF",
    "WildStrawberry": "FF43A4",
    "Yellow": "FFFF00",
    "YellowGreen": "9ACD32"
}

def generateLink(colorCode):
    return f"![](http://via.placeholder.com/80x40/{colorCode}/{colorCode})"


for x in range(0, 17):
    colOne = f"{generateLink(list(colorsFirstCol.values())[x])} <br> <b>{list(colorsFirstCol.keys())[x]}</b>"
    colTwo = f"{generateLink(list(colorsSecondCol.values())[x])} <br> <b>{list(colorsSecondCol.keys())[x]}</b>"
    colThr = f"{generateLink(list(colorsThirdCol.values())[x])} <br> <b>{list(colorsThirdCol.keys())[x]}</b>"
    colFor = f"{generateLink(list(colorsFourthCol.values())[x])} <br> <b>{list(colorsFourthCol.keys())[x]}</b>"
    print(f"| {colOne} | {colTwo} | {colThr} | {colFor} |")
