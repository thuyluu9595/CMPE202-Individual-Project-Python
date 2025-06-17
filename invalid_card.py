from credit_card import CreditCard
import logging

class NonCard(CreditCard):
    def __init__(self, card_number, expiry_date, name_of_card_holder):
        super().__init__('Error', card_number, expiry_date, name_of_card_holder)
        logging.info('Card info error')