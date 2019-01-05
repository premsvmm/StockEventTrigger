from model.Database_model import User
from model.Database_model import Stock
from nsetools import Nse



class StockCalculation():

    def get_users(self):

        u = User()

        value = u.get_all_user()

        return value

    def get_stock_list(self,userId):

        s =Stock()

        value = s.get_stocklist_by_userid(userId)

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

                if float(stock_values['lastPrice']) >= float(stock.sell):

                    if stock.emailtrigger:

                        print("it came to the sell price")

                if float(stock_values['lastPrice']) <= float(stock.loss) :

                    if stock.emailtrigger:

                        print("stocks goes in loss")

                else:

                    print("ignore")



    def get_stocks_values(self,stocksName):

        nse = Nse()

        return nse.get_quote(stocksName)


if __name__ == '__main__':

    s =StockCalculation()

    s.stock_calculation()




