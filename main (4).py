def linearsearchproduct(productlist, targetproduct):
    indices = []
    for index,product in enumerate(productlist):
        if products== targetproduct:
            indices.append(index)
    return indices


products = ["apple", "banana", "apple", "grape", "apple"]
target = "apple"
target2='shoes'
result = linearsearchproduct(products, target)
print(result) 