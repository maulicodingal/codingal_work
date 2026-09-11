team_A = 134
team_B = 116
team_C = 122
team_D = 109
team_E = 127

total = team_A + team_B + team_C + team_D + team_E
average = total / 5
 
print("Total Points:", total)
print("Average per team:", average)
 
stars_per_point = 5
total_reward_stars = total * stars_per_point
print("Total reward stars :", total_reward_stars)
 
full_boxes = total_reward_stars // 25
left_over = total_reward_stars % 25
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover)

last_week = 650
 
print("Better than the last week? :", total > last_week)
print("Same as the last week? :", total == last_week)
print("At least as good as the last week? :", total >= last_week)
 
total += 30
print("After adding the bonus points :", total)
 
total -= 15
print("After missed a few tasks :", total)
 
total_reward_stars = total * stars_per_point
full_boxes = total_reward_stars // 25
 
print("The final boxes packed :", boxes)