from model.Database_model import  Stock


class StatusUpdate():

    def update_value(self):

        s = Stock()

        s.update_status_to_true()



if __name__ == '__main__':

    u = StatusUpdate()

    u.update_value()