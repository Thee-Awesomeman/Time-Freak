import time
import random
def blackjack():
              new_game = False
              round_over = False
              won = 0
              lost = 0
              round = 1
              opdone = False
              card_num = 0
              time.sleep(3)
              while new_game == False:
                     print(f"Round {round}")
                     time.sleep(3)
                     round += 1
                     round_over = False
                     opdone = False
                     num = random.randint(2,11)
                     name = num
                     num2 = random.randint(2,11)
                     name2 = num2
                     total = num + num2
                     if num == 11:
                            name = "an ace"
                     if num2 == 11:
                            name2 = "an ace"

                     opnum = random.randint(2,11)
                     opname = opnum
                     opnum2 = random.randint(2,11)
                     opname2 = opnum2
                     optotal = opnum + opnum2
                     if opnum == 11:
                            opname = "an ace"
                     if opnum2 == 11:
                            opname2 = "an ace"
                     optotal = opnum + opnum2
                     print("You each get dealt 2 cards.")
                     time.sleep(3)
                     print(f"Your card's values are {name} and {name2}.")
                     time.sleep(3)
                     if name == "an ace" and total > 21:
                            total -= 10
                            print(f"Your ace's value changes to 1 and your total is {total}.")
                            name = False
                            time.sleep(3)
                     elif name2 == "an ace" and total > 21:
                            total -= 10
                            print(f"Your ace's value changes to 1 and your total is {total}.")
                            name2 = False
                            time.sleep(3)
                     print(f"Your opponent has {opname} and {opname2}.")
                     time.sleep(3)
                     if opname == "an ace" and optotal > 21:
                            optotal -= 10
                            print(f"Their ace's value changes to 1 and their total is {optotal}.")
                            opname = False
                            time.sleep(3)
                     elif opname2 == "an ace" and optotal > 21:
                            optotal -= 10
                            print(f"Their ace's value changes to 1 and their total is {optotal}.")
                            opname2 = False
                            time.sleep(3)
                     while round_over == False:
                            hit_stand = input("Hit or stand? (hit/stand) ")
                            time.sleep(1)
                            if hit_stand == "hit":
                                   card_num += 1
                                   num = random.randint(2,11)
                                   total += num
                                   if num == 11:
                                          name = "an ace"
                                   else:
                                          name = False
                                   if name == "an ace":
                                          print(f"You drew {name}.")
                                   else:
                                          print(f"You drew {num}")
                                   time.sleep(3)
                                   if name == "an ace" and total > 21:
                                          total -= 10
                                          print(f"Your ace's value changes to 1 and your total is {total}.")
                                          time.sleep(3)
                                   elif name2 == "an ace" and total > 21:
                                          total -= 10
                                          print(f"Your ace's value changes to 1 and your total is {total}.")
                                          name2 = False
                                          time.sleep(3)
                                   if total <= 21:
                                          if card_num == 5:
                                                 print("You win the round by holding 5 cards.")

                                          else:
                                                 continue
                                   if total > 21:
                                          print("You busted!")
                                          time.sleep(3)
                                          lost += 1
                                          round_over = True            
                                          break
                            else:
                                   print(f"You stood with {total}.")
                                   time.sleep(3)
                                   opdone == False
                            while opdone == False:
                                   if 11 < optotal <= 21 and optotal >= total:
                                          print(f"Your opponent has stood with {optotal}")
                                          time.sleep(3)
                                          opdone = True
                                          break
                                   elif optotal <= 11 or optotal < total:
                                          opnum = random.randint(2,11)
                                          optotal += opnum
                                          if opnum == 11:
                                                 opname = "an ace"
                                          else:
                                                 opname = False
                                   if opname == "an ace":
                                          print(f"Your opponent draws {opname}")
                                          time.sleep(3)
                                   else:
                                          print(f"Your opponent draws {opnum}.")
                                          time.sleep(3)
                                   if opname == "an ace" and optotal > 21:
                                          optotal -= 10
                                          print(f"Their ace's value changes to 1 and their total is {optotal}.")
                                          time.sleep(3)
                                   elif opname2 == "an ace" and total > 21:
                                          total -= 10
                                          print(f"Your ace's value changes to 1 and your total is {total}.")
                                          opname2 = False
                                          time.sleep(3)
                                   if optotal > 21:
                                          print("Your opponent has busted!")
                                          time.sleep(3)
                                          won += 1
                                          round_over = True
                                          break
                            if total <= 21 and optotal <= 21:
                                   if optotal > total:
                                          print("Your opponent has a higher value than you, so your opponent wins the round.")
                                          time.sleep(3)
                                          bust += 1
                                          round_over = True
                                          break
                                   elif total > optotal:
                                          print("You have a higher value than your opponent, so you win the round.")
                                          time.sleep(3)
                                          bust += 1
                                          break
                                   else:
                                          print("Nobody wins the round due to a tie.")
                                          time.sleep(3)
                                          break
                     if won == 3:
                            print("You beat your opponent.")
                     if lost <= 3:
                            time.sleep(3)
                            continue
                     else:
                            print("You lost and were thrown out.")
                            time.sleep(3)
                            return "lost"

blackjack()