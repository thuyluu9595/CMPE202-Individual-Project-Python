from file_handler import FileHandler

class CSVHandler(FileHandler):

    def __init__(self, factory_entry):
        super().__init__(factory_entry)


    def read_card(self, file_name):
        cards = []

        with open(file_name, 'r') as file:
            lines = file.readlines()

            for line in lines:
                data = line.split(',')
                card = self.factory_entry.create_credit_card(data[0].strip(), data[1].strip(), data[2].strip())
                cards.append(card)

        return cards
    

    def write_file(self, cards):
        output_file = 'result.csv'

        with open(output_file, 'a') as file:
            for card in cards:
                file.write(f'{card.get_card_number()}, {card.get_card_name()}\n')
        