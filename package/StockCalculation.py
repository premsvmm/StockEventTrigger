from model.Database_model import User
from model.Database_model import Stock
from package.EmailSender import Email
from nsetools import Nse



class StockCalculation():


    def __init__(self):
        self.u = User()
        self.s = Stock()
        self.e = Email()

    def get_users(self):

        value = self.u.get_all_user()

        return value

    def get_stock_list(self,userId):

        value = self.s.get_stocklist_by_userid(userId)

        return value

    def stock_calculation(self):

        user_list = self.get_users()

        for user in user_list:

            stock_list = self.get_stock_list(user.id)

            for stock in stock_list:

                stock_values = self.get_stocks_values(stock.stockId)

                if float(stock_values['lastPrice']) > float(stock.buy):

                    if stock.emailtrigger:

                        print("Stocks is postive")

                        self.e.postiveprice_Email(user.username,stock.stockId,stock.buy,stock_values['lastPrice'])

                        self.update_emailtrigger_status(user.id,stock.id)


                if float(stock_values['lastPrice']) >= float(stock.sell):

                    if stock.emailtrigger:

                        print("it came to the sell price")

                        self.e.targetprice_email(user.username, stock.stockId, stock.buy, stock_values['lastPrice'])

                        self.update_emailtrigger_status(user.id, stock.id)

                if float(stock_values['lastPrice']) <= float(stock.loss):

                    if stock.emailtrigger:

                        print("stocks goes in loss")

                        self.e.loss_email(user.username, stock.stockId, stock.buy, stock_values['lastPrice'])

                        self.update_emailtrigger_status(user.id, stock.id)

                else:

                    print("ignore")

                    self.update_emailtrigger_status(user.id, stock.id)



    def get_stocks_values(self,stocksName):

        nse = Nse()

        return nse.get_quote(stocksName)


    def update_emailtrigger_status(self,userid,stockid):

        s = Stock()

        s.update_status_for_user_stock(userid,stockid)



if __name__ == '__main__':

    s =StockCalculation()

    s.stock_calculation()




