# Program organising sales data for pizza shop via list manipulation.

# creating list a pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# creating a list for prices of each kind of slice
prices = [2, 6, 1, 3, 2, 7, 2]

# counting how many times 2 occur in price list and storing to variable.
num_two_dollar_slices = prices.count(2)

# finding length of the toppings list and storing in variable.
num_pizzas = len(toppings)

# printing string with number of pizzas we sell
print("We sell ", num_pizzas, "different kinds of pizza!")

# creating a 2D list of prices and topping [price, topping_name]
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# sorting 2D list in ascending order of price
pizza_and_prices.sort()

# storing cheapest pizza (first index) in variable
cheapest_pizza = pizza_and_prices[0]

# storing most expensive pizza (last index) in variable
priciest_pizza = pizza_and_prices[-1]

# adding a new topping to our 2D pizzas list at index 4
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# slicing pizza list and storing lowest 3 pizzas in variable
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
