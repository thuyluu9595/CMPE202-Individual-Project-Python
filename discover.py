from credit_card import CreditCard
import logging

class Discover(CreditCard):
    def __init__(self, card_number, expiry_date, name_of_card_holder):
        super().__init__('Discover', card_number, expiry_date, name_of_card_holder)
        logging.info('Discover card is created')