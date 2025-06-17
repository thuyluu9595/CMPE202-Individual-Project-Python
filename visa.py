from credit_card import CreditCard
import logging

class Visa(CreditCard):
    def __init__(self, card_number, expiry_date, name_of_card_holder):
        super().__init__('Visa', card_number, expiry_date, name_of_card_holder)
        logging.info('Visa card is created')