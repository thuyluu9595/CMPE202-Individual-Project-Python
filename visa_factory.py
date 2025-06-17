from credit_card_factory import CreditCardFactory
from visa import Visa
from invalid_card import NonCard

class VisaFactory(CreditCardFactory):

    def __init__(self):
        self.__next_chain = None


    def create_credit_card(self, card_number, expiration_date, card_holder_name):
        if (card_number[0] == '4' and len(card_number) == 16) or len(card_number) == 13:
            return Visa(card_number, expiration_date, card_holder_name)
        
        if self.__next_chain is not None:
            return self.__next_chain.create_credit_card(card_number, expiration_date, card_holder_name)
        else:
            return NonCard(card_number, expiration_date, card_holder_name)
    

    def set_next_chain(self, next_chain):
        self.__next_chain = next_chain
