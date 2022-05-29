import sys
input = sys.stdin.readline

M = int(input())
sanggeun_cards = list(map(int,input().split()))
card_num = {}
for card in sanggeun_cards :
    if card in card_num :
        card_num[card] += 1
    else :
        card_num[card] = 1

N = int(input())
compare_cards = list(map(int,input().split()))

result = ""
for compare in compare_cards :
    if compare in card_num :
        result += str(card_num[compare]) + " "
    else :
        result += "0 "

print(result)