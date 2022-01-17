def profit(cp,sp):
    prof=sp-cp
    return prof
def loss(cp,sp):
    los=cp-sp
    return los

if __name__=="__main__":
    cp=int(input("enter the cost price:"))
    sp=int(input("enter the sell price:"))
    if cp==sp:
        print("no profit nor any loss")
    elif sp>cp:
        print("Rs",profit(cp,sp),",profit")
    else:
        print("Rs",loss(cp,sp),",loss")
