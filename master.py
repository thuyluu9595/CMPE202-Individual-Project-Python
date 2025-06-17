from credit_card import CreditCard
import logging

class Master(CreditCard):
    def __init__(self, card_number, expiry_date, name_of_card_holder):
        super().__init__('Master', card_number, expiry_date, name_of_card_holder)
        logging.info('Master card is created')