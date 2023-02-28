class EmailMaker:
    def __init__(self):
        with open('./Input/Letters/starting_letter.txt') as letter:
            self.starting_letter = letter.read()
        with open('./Input/Names/invited_names.txt') as names:
            self.invited_list = [x.strip() for x in names.readlines()]

    def make_invitation(self):
        for name in self.invited_list:
            new_letter = self.starting_letter.replace('[name]', name)
            with open(f"./Output/ReadyToSend/invite_to_{name}.txt", mode="w") as invite:
                invite.write(new_letter)

