from model.Database_model import  Stock


class StatusUpdate():

    def update_value(self):
        s = Stock()
        s.update_status_to_true()
