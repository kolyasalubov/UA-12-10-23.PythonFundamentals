def factorial_(n):
    if n == 0 :
        return 1
    product_ = 1
    for i in range(1,n+1):
        product_*=i
    print(product_)
    return product_

factorial_(6)
