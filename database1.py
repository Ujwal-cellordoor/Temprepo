print("""           Welcome to Sunsari electronics!!
********************************************************
               Please select Menu""")
key = int(input("""
               Type 1 to store products
               Type 2 to display products
               Type 3 to search products
               Type 4 to delete products
                :: """))

product_dict = {}


if key == 1:
    f = open("hello.txt", "a")
    num_entries = 3

# Take input and store it in the dictionary
    for i in range(num_entries):
        key = input("Enter key: ")
        value = input("Enter value: ")
        product_dict[key] = value

# Print the resulting dictionary
    # print("Product details:", product_dict)
    f.write(str(product_dict) + '\n')


elif key == 2:
    f = open("hello.txt", "r")
    display_product = f.read()
    print(display_product)
elif key == 3:
    search_keyword = input("what do you want to search? >>.. ")
    print("searching " + search_keyword + "...")
    file_obj = open("hello.txt", "r")
    total_lines = file_obj.readlines()
    for line in total_lines:
        if search_keyword in line:
            print("search found! ")
            product_dict = line.split(",")
            product_name = product_dict[0]
            product_brand = product_dict[1]
            product_price = product_dict[2]
            print("Product name:" + str({product_name}) + "Product brand: " +
                  str({product_brand}) + "Prdouct price: " +
                  str({product_price}))
