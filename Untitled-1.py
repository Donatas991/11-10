# # password=input("iveskite slaptazodi ")
# # sk=False
# # for raide in password:
# #     if raide.isdigit():
# #         sk=True

# # if len(password)>7 and sk:
# #     print(True)
# # else:
# #     print(False)
    

# # def ar_stiprus_slaptazodis(password)
# #         for raide in password:
# #                 if raide.isdigit():
# #                     sk=True
# #                 else:
# #                        sk=False
# #         if len(password)>7 and sk:
# #                return True
# #         else:
# #                return False
        
# # password=input("iveskite slaptazodi ")
# # print (ar_stiprus_slaptazodis )

# # password = "codding_is_fun!"
# # userinput= ""
# # def paswoordchecker():
# #     while userinput != password:
# #         userinput = input ("enter you password")
# #         if userinput == password:
# #            print("welcome to the main frame")
# #         else:
# #            print("wrong password")

# # zodis=input("iveskite zodis")
# # balses="aeiouąęėįųūAEIOUĄĘĖĮŲŪ"

# # b=0
# # p=0
# # for raides in zodis:
# #     if raides in balses:
# #       b=b+1
# #    else:
      
# #    p=p+1
# # print("balsiu sk: ", b)
# # Print("priebalsiu skaicius ", p)

# # def tiesinė_paieška(sąrašas, ieškomas_žodis):
# #     for i in range(len(sąrašas)):
# #         if sąrašas[i] == ieškomas_žodis:
# #             return i
# #     return -1  # ieškomas_žodis nerastas

# # daiktai = [1, 4, 7, 8]

# # print(tiesinė_paieška(daiktai, 4))

# # def tiesinė_paieška(daiktai, ieškomas_daiktas):
# #     for i in range(len(daiktai)):
# #       if daiktai[i] == ieškomas_daiktas:
# #         return True
# #     return False # ieškomas_daiktas nerastas

# # daiktai = [1, 25, 58, 7, 68]

# # print(tiesinė_paieška(daiktai, 7))


# # def tiesinė_paieška(daiktai, ieškomas_daiktas):
# #     for i in range(len(daiktai)):
# #       if daiktai[i] == ieškomas_daiktas:
       

# # daiktai = [1, 25, 58, 7, 68]

# # print(tiesinė_paieška(daiktai, 7))

# # import random
# # import time

# # ---------------------------
# # Room and Map Definitions
# # ---------------------------
# class Room:
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
#         self.connections = []

#     def connect(self, other_room):
#         self.connections.append(other_room)

# class GameMap:
#     def __init__(self):
#         self.rooms = {}
#         self.create_rooms()

#     def create_rooms(self):
#         # Define rooms
#         self.add_room('1A', 'Show Stage')
#         self.add_room('1B', 'Dining Area')
#         self.add_room('2A', 'West Hall')
#         self.add_room('2B', 'West Corner')
#         self.add_room('3A', 'East Hall')
#         self.add_room('3B', 'East Corner')
#         self.add_room('OFFICE', 'Office')

#         # Connect rooms
#         self.link('1A', '1B')
#         self.link('1B', '2A')
#         self.link('1B', '3A')
#         self.link('2A', '2B')
#         self.link('3A', '3B')
#         self.link('2B', 'OFFICE')
#         self.link('3B', 'OFFICE')

#     def add_room(self, code, name):
#         self.rooms[code] = Room(code, name)

#     def link(self, code1, code2):
#         self.rooms[code1].connect(code2)
#         self.rooms[code2].connect(code1)

#     def get_room(self, code):
#         return self.rooms.get(code)

#     def render_map(self, anim_positions):
#         # Visual ASCII Map
#         print("\nCurrent Facility Map:")
#         def marker(room):
#             tags = [a[0] for a in anim_positions if a[1] == room]
#             return f"{room} ({', '.join(tags)})" if tags else room

#         print(f"        [{marker('1A')}]")
#         print("           |")
#         print(f"        [{marker('1B')}]")
#         print("        /       \\")
#         print(f"   [{marker('2A')}]     [{marker('3A')}]")
#         print("     |               |")
#         print(f"[{marker('2B')}]     [{marker('3B')}]")
#         print("      \\             /")
#         print(f"         [{marker('OFFICE')}] (You)")

# # ---------------------------
# # Animatronic Definition
# # ---------------------------
# class Animatronic:
#     def __init__(self, name, path):
#         self.name = name
#         self.path = path
#         self.position = 0
#         self.active = False

#     def get_room(self):
#         return self.path[self.position]

#     def move(self, aggression):
#         if not self.active:
#             if random.randint(1, 100) < 10 + aggression:
#                 self.active = True
#                 print(f"{self.name} became active!")
#         elif self.position < len(self.path) - 1:
#             if random.randint(1, 100) < 30 + aggression:
#                 self.position += 1
#                 print(f"{self.name} moved to {self.get_room()}.")

#     def reset(self):
#         self.position = 0

# # ---------------------------
# # Game Class
# # ---------------------------
# class FNAFGame:
#     def __init__(self):
#         self.map = GameMap()
#         self.time = 0
#         self.power = 100
#         self.doors = {'left': False, 'right': False}
#         self.animatronics = [
#             Animatronic("Bonnie", ['1A', '1B', '2A', '2B', 'OFFICE']),
#             Animatronic("Chica",  ['1A', '1B', '3A', '3B', 'OFFICE']),
#             Animatronic("Freddy", ['1A', '1B', '3A', '3B', 'OFFICE'])
#         ]
#         self.alive = True

#     def render_status(self):
#         print(f"\n--- Hour {self.time + 1}/12 ---")
#         print(f"Power: {self.power}%")
#         print(f"Doors: Left - {'Closed' if self.doors['left'] else 'Open'} | Right - {'Closed' if self.doors['right'] else 'Open'}")

#     def get_anim_positions(self):
#         return [(a.name, a.get_room()) for a in self.animatronics]

#     def check_cameras(self):
#         print("\n--- Camera Feed ---")
#         for name, room in self.get_anim_positions():
#             print(f"{name} is in {room}")
#         self.power -= 2

#     def toggle_door(self, side):
#         self.doors[side] = not self.doors[side]
#         state = "closed" if self.doors[side] else "opened"
#         print(f"{side.capitalize()} door {state}.")
#         self.power -= 1

#     def render_map(self):
#         self.map.render_map(self.get_anim_positions())

#     def use_power(self):
#         usage = 1
#         usage += sum(self.doors.values())  # +1 per closed door
#         self.power -= usage
#         if self.power < 0:
#             self.power = 0

#     def animatronic_actions(self):
#         aggression = self.time * 5
#         for anim in self.animatronics:
#             anim.move(aggression)
#             if anim.get_room() == 'OFFICE':
#                 side = 'left' if anim.name == 'Bonnie' else 'right'
#                 if not self.doors[side]:
#                     print(f"\n💀 {anim.name} entered your office! You left the {side.upper()} door open!")
#                     self.game_over()
#                 else:
#                     print(f"{anim.name} tried to enter from {side.upper()} but the door was shut.")
#                     anim.reset()

#     def advance_time(self):
#         self.time += 1
#         if self.time >= 12:
#             self.win_game()

#     def game_over(self):
#         print("\n👻 JUMPSCARE! You lost.")
#         self.alive = False

#     def win_game(self):
#         print("\n🎉 12 PM - You survived the night!")
#         self.alive = False

#     def play(self):
#         print("🎮 Welcome to FNAF: Text Edition")
#         print("Survive from 12 AM to 12 PM. Use cams, doors, and power wisely.")

#         while self.alive and self.time < 12:
#             self.render_status()
#             print("\nActions:")
#             print("1. Check Cameras")
#             print("2. Toggle Left Door")
#             print("3. Toggle Right Door")
#             print("4. View Map")
#             print("5. Wait")

#             choice = input("Choose (1-5): ").strip()
#             if choice == '1':
#                 self.check_cameras()
#             elif choice == '2':
#                 self.toggle_door('left')
#             elif choice == '3':
#                 self.toggle_door('right')
#             elif choice == '4':
#                 self.render_map()
#             elif choice == '5':
#                 print("You wait silently...")
#             else:
#                 print("Invalid input. You fumble nervously...")

#             self.use_power()
#             if self.power <= 0:
#                 print("\n⚠️ Power Out! You sit in the dark...")
#                 if random.randint(1, 100) < 70:
#                     self.game_over()
#                     break
#                 else:
#                     print("Miraculously... you hang on.")

#             if self.alive:
#                 self.animatronic_actions()
#                 time.sleep(1)
#                 self.advance_time()

#         print("Game Over.")

# # ---------------------------
# # Run the Game
# # ---------------------------
# if __name__ == "__main__":
#     FNAFGame().play()

# n=(1; 2; 3; 4; 5; 6):
# n.pop(2) from [n]
# #naudojamas pašalinti  2 pozicijos skaičiu iš eilės


# n=(1; 2; 3; 4; 5; 6):
# n.remove(2) from [n]
# #naudojamas pašalinti skaičiu 2 iš eilės


# n=(1; 2; 3; 4; 5; 6):
# n.del(2) 
# #naudojamas ištrinti skaičiu 2


# x = range(6)
# for n in x:
#   print(n)


  n=(1; 2; 3; 4; 5; 6):
n.append(2)
#naudojamas perašyti sararaša be skaičiaus 2
