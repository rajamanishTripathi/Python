
print("WELCOME TO THE BLIND ACTION !!!")
auction = {}

def highest_bidder(bidding):
    highest = 0
    highest_bidder= ""
    for bidder in bidding:
        bid_amount = int(bidding[bidder])
        if bid_amount > highest:
            highest = bid_amount
            highest_bidder = bidder

    print(f"The highest bidder is {highest_bidder} with bidding of ${highest} .")

auction_continue = True
while auction_continue:
    name = input("Please state your name: ")
    bid = int(input("Please bid $"))
    auction[name] = bid
    # auction.update({name, bid})
    auctionee = input("Is there any other auctioneer: Enter \"Yes\" to continue and \"No\" to end.").lower()
    if auctionee == "no":
        auction_continue = False
        highest_bidder(auction)
    elif auctionee == "yes":
        print("\n" * 20)
