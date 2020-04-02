def weight_on_planets():
    weight = float(input("What do you weigh on earth? "))
    mars = weight * 0.38
    jupiter = weight * 2.34
    print("\n" + "On Mars you would weigh", mars, "pounds." + "\n" + "On Jupiter you would weigh", jupiter, "pounds.")


if __name__ == '__main__':
    weight_on_planets()
