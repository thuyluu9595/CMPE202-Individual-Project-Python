from visa import Visa
from visa_factory import VisaFactory
from master_factory import MasterFactory
from discover_factory import DiscoverFactory
from american_express_factory import AmericanExpressFactory
from card_validator import CardValidator
from csv_handler import CSVHandler
import sys

def get_credit_card_factory():

    visa = VisaFactory()
    master = MasterFactory()
    discover = DiscoverFactory()
    amex = AmericanExpressFactory()
    validator = CardValidator()

    amex.set_next_chain(discover)
    master.set_next_chain(amex)
    visa.set_next_chain(master)
    validator.set_next_chain(visa)

    return validator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = sys.argv[1]

    factory = get_credit_card_factory()

    file_handler = CSVHandler(factory)
    cards = file_handler.read_card(file_name)

    for card in cards:
        print(card)

    file_handler.write_file(cards)


