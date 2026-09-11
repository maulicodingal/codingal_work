print("Welcome to Special Agent Badge")


name = input("Whats your name agent?")
gadget =input("Whats your fav gadget?")

id = 7
status = "active"
total_mis = 20
kill_per = 99.9

print("Name: ", name, "type of data here: ", type(name))
print("Gadget used: ", gadget, "type of data here: ", type(gadget))
print("Id: ", id, "type of data here: ", type(id))
print("Status: ", status, "type of data here: ", type(status))
print("Total missions: ", total_mis, "type of data here: ", type(total_mis))
print("Kill percentage: ", kill_per, "type of data here: ", type(kill_per))

id_str = str(id)
total_str = str(total_mis)
kill_per = str(kill_per)
status_str = str(status)

print("id as text:", id_text, "type of data here:", type(id_text))
print("total missions as text:", total_mission_text, "type of data here:", type(total_missions_text))
print("kill percentage as text:", kill_percentage text, "type of data here:", type(kill_percentage_text))
print("Status as text:", status_text, "type of data here:", type(status_text))

first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First 3 letters of the name:", first_three)
print("Last letter of the name:", last_letter)
print("The Secret Code Name:", code_name)

reversed_gadget = gadget[::-1]
print("Reversed the Gadget Name:", reversed_gadget)

badge_num_1 = "AGENT " + code_name.upper()
badge_num_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text
badge_num_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
badge_num_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()

print("")
print("===== SECRET AGENT BADGE =====")
print(badge_num_1)
print(badge_num_2)
print(badge_num_3)
print(badge_num_4)
print("===============================")