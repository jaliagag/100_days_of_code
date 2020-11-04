BlackShoes = {42:2, 41:3, 40:4, 39:1, 38:0} # inventory, no order
# size:stock
while(True): #(True == True)
    purchaseSize = int(input('which shoe size would you like to buy?\n'))
    if purchaseSize < 0:
        break
    if purchaseSize in BlackShoes == False:
        print('ta loco voooooo!!')
    if BlackShoes[purchaseSize] > 0:
        BlackShoes[purchaseSize] -= 1
    else:
        print('no shoe sizes', purchaseSize)
    print(BlackShoes)
