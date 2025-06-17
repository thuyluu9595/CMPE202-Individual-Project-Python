from abc import ABC, abstractmethod

class CreditCardFactory(ABC):

    @abstractmethod
    def create_credit_card(card_number, expiration_date, card_holder_name):
        pass

    @abstractmethod
    def set_next_chain(next_chain):
        pass
    