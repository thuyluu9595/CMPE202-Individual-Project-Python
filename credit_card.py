from abc import ABC, abstractmethod

class CreditCard(ABC):
    def __init__(self, card_name, card_number, expiry_date, name_of_card_holder):
        self.__card_name = card_name
        self.__card_number = card_number
        self.__expiry_date = expiry_date
        self.__card_holder = name_of_card_holder

    def get_card_number(self):
        return self.__card_number
    
    def set_card_number(self, card_number):
        self.__card_number = card_number

    def get_expiry_date(self):
        return self.__expiry_date
    
    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    def get_card_holder(self):
        return self.__card_holder
    
    def set_card_holder(self, card_holder):
        self.__card_holder = card_holder

    def get_card_name(self):
        return self.__card_name
    
    def __str__(self):
        return f'Card number: {self.__card_number}, expiry date: {self.__expiry_date}, card holder: {self.__card_holder}'