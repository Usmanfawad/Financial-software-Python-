import sqlite3

class Liabilities:
    liabilities={}
    liabilities_id="L000"
    def __init__(self,id,title,debit,credit,debit_balance,credit_balance):
        Liabilities.liabilities_id= id
        self.id=id
        self.title=title
        self.debit = debit
        self.credit = credit
        self.debit_balance = debit_balance
        self.credit_balance = credit_balance
        Liabilities.liabilities[self.id]=self

    @classmethod
    def create_object(cls,type):
        def assign_id():
            x=list(Liabilities.liabilities_id)
            y=x[1]+x[2]+x[3]
            y=int(y)
            y+=1
            if len(str(y))==1:
                y='0'+'0'+str(y)
            elif len(str(y))==2:
                y='0'+str(y)
            f=x[0]+str(y)
            return f
        id= assign_id()
        # type=input("Enter Liability type: ")
        return cls(id,type.title(),"0","0","0","0")

    def update_debit(self,x):
        self.debit=x
        conn = sqlite3.connect("accounts_db.db")
        d = conn.cursor()
        d.execute(("Update Liability SET debit = ? WHERE id =?"), (x, self.id))
        conn.commit()
        self.update_debit_credit_balance()
        d.close()

    def update_credit(self,x):
        self.credit=x
        conn = sqlite3.connect("accounts_db.db")
        d = conn.cursor()
        d.execute(("Update Liability SET credit = ? WHERE id =?"), (x, self.id))
        conn.commit()
        self.update_debit_credit_balance()
        d.close()

    def update_debit_credit_balance(self):
        debit_value= int(Liabilities.liabilities[self.id].debit)
        credit_value=int(Liabilities.liabilities[self.id].credit)
        if debit_value>credit_value:
            insert_value=debit_value-credit_value
            Liabilities.liabilities[self.id].debit_balance = insert_value
            Liabilities.liabilities[self.id].credit_balance = 0
            conn = sqlite3.connect("accounts_db.db")
            d = conn.cursor()
            d.execute(("Update Liability SET debit_balance = ? WHERE id =?"), (insert_value, self.id))
            d.execute(("Update Liability SET credit_balance=0 WHERE id=?"),(self.id,))
            conn.commit()
            d.close()
        else:
            insert_value=credit_value-debit_value
            Liabilities.liabilities[self.id].debit_balance = 0
            Liabilities.liabilities[self.id].credit_balance = insert_value
            conn = sqlite3.connect("accounts_db.db")
            d = conn.cursor()
            d.execute(("Update Liability SET credit_balance = ? WHERE id =?"), (insert_value, self.id))
            d.execute(("Update Liability SET debit_balance=0 WHERE id=?"), (self.id,))
            conn.commit()
            d.close()
    @classmethod
    def delete_objects(cls):
        for k,v in Liabilities.liabilities.items():
            Liabilities.liabilities.pop(k,None)