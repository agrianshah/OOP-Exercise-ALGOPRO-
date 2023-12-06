class BelanjaTAP: 
    def __init__(self,name,amount):
        self.__name= name
        self.__amount= amount
        self.__standardprice= {
            "Dry Cured Iberian Ham": "$177.80",
            "Wagyu Steaks": "$450.00",
            "Matsutake Mushrooms": "$272.00",
            "Kopi Luwak Coffee": "$306.50",
            "Moose Cheese": "$487.20",
            "White Truffles": "$3600.00",
            "Blue Fin Tuna": "$3603.00",
            "Le Bonnotte Potatoes": "$270.81"
        }
        self.calculatedprice = 0.00

    def  PriceList(self):
        foodname = self.__foodname.lower()
        if foodname =="Dry Cured Iberian Ham":
            self.__standardprice== 177.80
        elif foodname =="Wagyu Steaks":
            self.__standardprice== 450.00
        elif foodname =="Matsutake Mushrooms":
            self.__standardprice== 272.00
        elif foodname =="Kopi Luwak Coffee":
            self.__standardprice== 306.50
        elif foodname =="Moose Cheese":
            self.__standardprice== 487.20
        elif foodname =="White Truffles":
            self.__standardprice== 3600.00
        elif foodname =="Blue Fin Tuna":
            self.__standardprice== 3603.00
        elif foodname =="Le Bonnotte Potatoes":
            self.__standardprice== 270.81
        else:
            self.__standardprice == 0.00

    def calculatePrice(self):
        self.calculatedprice = self.amount * self.standardprice
        return self.calculatedprice
    
    def __str__(self):
        return f"Here's a summary of the item's purchased: \
            "