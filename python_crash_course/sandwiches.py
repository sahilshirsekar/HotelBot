def sandwiches(*items):
    print(f"Items that you requested for :")
    for item in items :
        print(f"-> {item}")

sandwiches("fruit slices", "cheese", "tomatoes")