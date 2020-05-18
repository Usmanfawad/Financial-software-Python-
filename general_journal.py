
class Journal:
    journal={}
    journal_id="J000"
    def __init__(self,id,date,description):
        Journal.journal_id = id
        self.id = id
        self.date=date
        self.description=description
        Journal.journal[self.id]=self

    @classmethod
    def create_object(cls,date,description):
        def assign_id():
            x = list(Journal.journal_id)
            y = x[1] + x[2] + x[3]
            y = int(y)
            y += 1
            if len(str(y)) == 1:
                y = '0' + '0' + str(y)
            elif len(str(y)) == 2:
                y = '0' + str(y)
            f = x[0] + str(y)
            return f
        id = assign_id()
        return cls(id,date,description)


class Entries:
    entries={}
    entries_id="Z001"
    def __init__(self,amount_type,id,amount,journal_id,account_id):
        Entries.entries_id=id
        self.amount_type = amount_type
        self.id=id
        self.amount=amount
        self.journal_id=journal_id
        self.account_id=account_id
        Entries.entries[self.id]=self

    @classmethod
    def create_object(cls,amount_type,amount,account_id):
        def assign_id():
            x = list(Entries.entries_id)
            y = x[1] + x[2] + x[3]
            y = int(y)
            y += 1
            if len(str(y)) == 1:
                y = '0' + '0' + str(y)
            elif len(str(y)) == 2:
                y = '0' + str(y)
            f = x[0] + str(y)
            return f
        id=assign_id()
        # amount_type=input("Enter the type of entry? Dr/Cr: ")
        # amount=input("Enter the amount: ")
        journal_id=Journal.journal_id
        # account_id=input("Please enter the account id: ")

        return cls(amount_type,id,amount,journal_id,account_id)






