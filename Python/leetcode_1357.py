from typing import List


class Cashier:
    customer_counter = 0
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount_on_nth_customer = n
        self.discount = discount
        self.products_prices = dict()

        index = 0
        for pId in products:
            self.products_prices[pId] = prices[index]
            index += 1

        print(self.products_prices)
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        subTotal = 0
        index = 0
        for pId in product:
            subTotal += self.products_prices[pId] * amount[index]

            index += 1

        print(subTotal)
        self.customer_counter += 1

        if self.customer_counter == self.discount_on_nth_customer:
            subTotal = subTotal - (subTotal * (self.discount / 100))
            self.customer_counter = 0
        
        print(f"subTotal after discount: {subTotal}")
        return round(subTotal, 1)
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

n = 3
discount = 50
products = [1,2,3,4,5,6,7]
prices = [100,200,300, 400, 300, 200, 100]

cashier = Cashier(n, discount, products, prices)

cashier.getBill([1, 2], [1, 2])
cashier.getBill([3, 7], [10, 10])
cashier.getBill([1,2,3,4,5,6,7], [1,1,1,1,1,1,1])
cashier.getBill([4], [10])
cashier.getBill([7, 3], [10, 10])
cashier.getBill([7, 5, 3, 1,6,4,2], [10, 10, 10, 9,9,9,7])
cashier.getBill([2,3,5], [5,3,2])