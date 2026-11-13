'''create a txt scoreboard file for the number guessing game'''

def main(initials, score):
    scores = [(initials, int(score))]
    
    with open("scoreboard.txt", "r") as f:
        for line in f:
            if line.strip():
                saved_initials, saved_score = line.strip().split(": ")
                scores.append((saved_initials, int(saved_score)))
                
    scores.sort(key=lambda item: item[1])
    
    with open("scoreboard.txt", "w") as f:
        for player, player_score in scores[:10]:
            f.write(f'{player}: {player_score}\n')
            
    print('\n<----- HIGH SCORES ----->\n')
    for player, player_score in scores[:10]:
        print(f'{player}: {player_score}')
        
if __name__ == "__main__":
    main()
    
#     with open("scoreboard.txt", "a+") as f:        
#         f.write(f'{initials}: {score}\n')
#         f.seek(0)
#         scores_list = f.read().splitlines()
#         print(scores_list)
        
#         scores = []
        
#         for line in scores_list:
#             initials, score = line.split(": ")
#             scores.append((initials, int(score)))
            
#         scores.sort(key=lambda item: item[1])
#         print(scores)
        
#         f.seek(0)
#         f.truncate(0)
        
#         for initials, score in scores:
#             f.write(f'{initials}: {score}\n')