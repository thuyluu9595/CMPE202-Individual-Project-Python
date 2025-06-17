from credit_card_factory import CreditCardFactory
from invalid_card import NonCard

class CardValidator(CreditCardFactory):

    def __init__(self):
        self.__next_chain = None

    
    def create_credit_card(self, card_number, expiration_date, card_holder_name):
        if len(card_number) > 19:
            return NonCard(card_number, expiration_date, card_holder_name)
        
        return self.__next_chain.create_credit_card(card_number, expiration_date, card_holder_name)
    

    def set_next_chain(self, next_chain):
        self.__next_chain = next_chain