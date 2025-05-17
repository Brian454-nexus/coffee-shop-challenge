from coffee_shop_challenge import Customer, Coffee, Order

def main():
    # Create customers
    john = Customer("John")
    jane = Customer("Jane")
    
    # Create coffees
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    # Create orders
    john.create_order(latte, 5.0)
    john.create_order(cappuccino, 6.0)
    jane.create_order(latte, 5.5)
    jane.create_order(latte, 6.0)
    
    # Test customer methods
    print(f"John's orders: {len(john.orders())}")
    print(f"John's unique coffees: {len(john.coffees())}")
    
    # Test coffee methods
    print(f"Latte orders: {latte.num_orders()}")
    print(f"Latte average price: ${latte.average_price():.2f}")
    
    # Test most aficionado
    most_latte_lover = Customer.most_aficionado(latte)
    print(f"Most latte lover: {most_latte_lover.name}")

if __name__ == "__main__":
    main() 