import os
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for i in bidder_details:   #in here we acces the values of dictionary using for loop 
        bidding_price=bidder_details[i]   #the values is assinged to a varible 
        if(bidding_price>highest_bid):   #comparing the result
            highest_bid=bidding_price  #swapping is happend
            winner=i
    print(f"Here is the list of all the bidder:{bidder_details}")
    print(f"the winner is {winner} with a bid price of {highest_bid}")

    
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name  : ")
    price=int(input("What is your bid : "))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders ? type yes/no : ").lower()
    if(more_bidders=="no"):
        end_of_bidding=True
        find_winner(bidder_data)
    elif(more_bidders=="yes"):
        os.system("cls")



