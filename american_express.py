from credit_card import CreditCard
import logging

class AmericanExpress(CreditCard):
    def __init__(self, card_number, expiry_date, name_of_card_holder):
        super().__init__('AmericanExpress', card_number, expiry_date, name_of_card_holder)
        logging.info('American Express card is created')