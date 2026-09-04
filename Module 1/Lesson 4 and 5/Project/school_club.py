member_name = input("Enter your real name, School Club Member: ")
club_name = input("Enter your school club name: ")

member_num = 2
points_earned = 11.8
event_count = 18
meeting_hrs = 4.5
active_status = True
 
print("Member Name:", member_name, "type of data here:", type(member_name))
print("Club Name:", club_name, "type of data here:", type(club_name))
print("Member Number:", member_num, "type of data here:", type(member_num))
print("Points Earned:", points_earned, "type of data here:", type(points_earned))
print("Event Count:", event_count, "type of data here:", type(event_count))
print("Meeting Hrs:", meeting_hrs, "type of data here:", type(meeting_hrs))
print("Active Status:", active_status, "type of data here:", type(active_status))
 
member_num_text = str(member_num)
event_count_text = str(event_count)
points_earned_text = str(points_earned)
active_status_text = str(active_status)
 
print("Member Num as text:", member_num_text, "type of data here:", type(member_num_text))
print("Event Count as text:", event_count_text, "type of data here:", type(event_count_text))
print("Points Earned as text:", points_earned_text, "type of data here:", type(points_earned_text))
print("Active Status as text:", active_status_text, "type of data here:", type(active_status_text))
 
first_four = name[0:4]
last_letter = name[-1:]
badge_code = first_four + last_letter
 
print("First 4 letters of name:", first_four)
print("Last letter of name:", last_letter)
print("Badge Code:", badge_code)
 
reverse_the_club_name = club[::-1]
print("Reverse the Club Name:", reverse_the_club_name)
 
badge_1 = " SCHOOL CLUB MEMBER " + badge_code.upper()
badge_2 = "MEMBER: " + member_num_text + " | EVENT: " + event_count_text
badge_3 = "POINTS: " + points_earned_text + " | ACTIVE: " + status_text
badge_4 = "SECRET CLUB CODE: " + reverse_the_club_name.upper()
 
print("")
print(" ===== SCHOOL CLUB MEMBER BADGE ===== ")
print(badge_1)
print(badge_2)
print(badge_3)
print(badge_4)
print("======================================")
