from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()



# courtyards and such

r_campus_welcome_center = Room(title="Lambda Welcome Center",
description="""The Lambda School journey begins here""")

r_campus_courtyard_south = Room(title="Campus Courtyard South",
description="""The south end of Lambda's massive courtyard""")

r_campus_courtyard_north = Room(title="Campus Courtyard North",
description="""The north end of Lambda's massive courtyard""")

r_campus_courtyard_mid = Room(title="Campus Courtyard center",
description="""The middle grounds of Lambda's massive courtyard""")

r_campus_courtyard_east = Room(title="Campus Courtyard East",
description="""The East end of Lambda's massive courtyard""")

r_campus_courtyard_west = Room(title="Campus Courtyard West",
description="""The West end of Lambda's massive courtyard""")

r_path_housing = Room(title="Housing Path",
description="""The path leading towards campus housing, passing 
the Community Gardens and the Recreation Fields""")

r_garden = Room(title="Community Gardens",
description="""Community garden right off the path to campus housing making
easy access to fresh vegetables and herbs""")

r_rec_fields = Room(title="Recreation Fields",
description="""Massive grass field used for extracurricular activities like soccer and
football. """)

r_housing_sqaure = Room(title="Campus Housing Square",
description="""Square connecting all the Campus housing to the rest of campus""")


#data building

r_ds_building = Room(title="Data Science Department Main Building", 
description="""Here students come to learn about the wonders of Data.""")

r_ds_help = Room(title="Data Science Help Center", 
description="""Student's come here for an assist in data related work.""")

r_ds_u1 = Room(title="Data Science Unit 1 Classroom", 
description="""Here students study the first unit of Data Science.""")

r_ds_u2 = Room(title="Data Science Unit 2 Classroom", 
description="""Here students study the second unit of Data Science.""")

r_ds_u3 = Room(title="Data Science Unit 3 Classroom", 
description="""Here students study the third unit of Data Science.""")

r_ds_u4 = Room(title="Data Science Unit 4 Classroom", 
description="""Here students study the fourth unit of Data Science.""")

r_ds_hall = Room(title="Data Science Building Back Hallway", 
description="""Leads to the back of the Data Science Building where 
the higher level classes are held""")



#web building

r_web_building = Room(title="Web Development Department Main Building", 
description="""Here students come to learn about the wonders of full stack web development.""")

r_web_help = Room(title="Web Development Help Center", 
description="""Student's come here for an assist in web dev related work.""")

r_web_u1 = Room(title="Web Development Unit 1 Classroom", 
description="""Here students study the first unit of web development.""")

r_web_u2 = Room(title="Web Development Unit 2 Classroom", 
description="""Here students study the second unit of web development.""")

r_web_u3 = Room(title="Web Development Unit 3 Classroom", 
description="""Here students study the third unit of web development.""")

r_web_u4 = Room(title="Web Development Unit 4 Classroom", 
description="""Here students study the fourth unit of web development.""")

r_web_hall = Room(title="Web Development Building Back Hallway", 
description="""Leads to the back of the Web Development Building where 
the higher level classes are held""")



#android building

r_android_building = Room(title="Android Development Department Main Building Ruins", 
description="""Here students used to come to learn about the wonders of Android Developmet before 
it was destroyed in a fire.""")

r_and_help = Room(title="Android Development Help Center", 
description="""Student's came here for an assist in android dev related work.""")

r_and_u1 = Room(title="Android Development Unit 1 Classroom", 
description="""Students used to study the first unit of Android Development here
before the fire.""")

r_and_u2 = Room(title="Android Development Unit 2 Classroom", 
description="""Students used to study the second unit of Android Development here
before the fire.""")

r_and_u3 = Room(title="Android Development Unit 3 Classroom", 
description="""Students used to study the third unit of Android Development here
before the fire.""")

r_and_u4 = Room(title="Android Development Unit 4 Classroom", 
description="""Students used to study the fourth unit of Android Development here
before the fire.""")

r_and_hall = Room(title="Android Development Building Back Hallway Ruins", 
description="""Leads to the back of the Android Development Building where 
the higher level classes were held before the fire""")



#ios building

r_ios_building = Room(title="IOS Development Department Main Building", 
description="""Here students come to learn about the wonders of Data.""")

r_ios_help = Room(title="IOS Development Help Center", 
description="""Student's come here for an assist in ios dev related work.""")

r_ios_u1 = Room(title="IOS Development Unit 1 Classroom", 
description="""Here students study the first unit of IOS Development.""")

r_ios_u2 = Room(title="IOS Development Unit 2 Classroom", 
description="""Here students study the second unit of IOS Development.""")

r_ios_u3 = Room(title="Data Science Unit 3 Classroom", 
description="""Here students study the third unit of IOS Development.""")

r_ios_u4 = Room(title="Data Science Unit 4 Classroom", 
description="""Here students study the fourth unit of IOS Development.""")

r_ios_hall = Room(title="IOS Development Building Back Hallway", 
description="""Leads to the back of the IOS Development Building where 
the higher level classes are held""")



#ux building

r_ux_building = Room(title="UX Design Department Main Building", 
description="""Here students come to learn about the wonders of UX Design.""")

r_ux_help = Room(title="UX Design Help Center", 
description="""Student's come here for an assist in ios dev related work.""")

r_ux_u1 = Room(title="UX Design Unit 1 Classroom", 
description="""Here students study the first unit of UX Design.""")

r_ux_u2 = Room(title="UX Design Unit 1 Classroom", 
description="""Here students study the second unit of UX Design.""")

r_ux_u3 = Room(title="UX Design Unit 1 Classroom", 
description="""Here students study the third unit of UX Design.""")

r_ux_u4 = Room(title="UX Design Unit 4 Classroom", 
description="""Here students study the fourth unit of UX Design.""")

r_ux_hall = Room(title="UX Design Building Back Hallway", 
description="""Leads to the back of the UX Design Building where 
the higher level classes are held""")



#cs building

r_cs_building = Room(title="Computer Science Department Main Building", 
description="""Here students come to learn about the wonders of Computer Science.""")

r_cs_help = Room(title="Computer Science Help Center", 
description="""Student's come here for an assist in Computer Science related work.""")

r_cs_u1 = Room(title="Computer Science Unit 1 Classroom", 
description="""Here students study the first unit of Computer Science.""")

r_cs_u2 = Room(title="Computer Science Unit 2 Classroom", 
description="""Here students study the second unit of Computer Science.""")

r_cs_bw1_gal = Room(title="Unit 1 Gallery", 
description="""A wonderful gallery displaying the amazing projects built in the
first build week of Lambda's Computer Science Program.""")

r_cs_bw2_gal = Room(title="Unit 2 Gallery", 
description="""A wonderful gallery displaying the amazing projects built in the
second build week of Lambda's Computer Science Program.""")

r_cs_hall = Room(title="Computer Science Building Back Hallway", 
description="""Leads to the back of the Computer Science Building""")



#labs building

r_labs_building = Room(title="Lambda Labs Department Main Building", 
description="""Here students come to grind along other developers on
extensive projects getting true real world experience.""")

r_labs_help = Room(title="Lambda Labs Help Center", 
description="""Student's come here for an assist in Computer Science related work.""")

r_labs_team_room = Room(title="Lambda Labs Team Room", 
description="""Teams use this room to plan and execute their ideas.""")

r_labs_ds_display = Room(title="Lambda Labs Data Science Gallery", 
description="""A wonderful gallery displaying the amazing projects built in
Lambda Labs with a Data Science focus.""")

r_labs_web_display = Room(title="Lambda Labs Web Gallery", 
description="""A wonderful gallery displaying the amazing projects built in
Lambda Labs with a Web App focus.""")

r_labs_mobile_display = Room(title="Lambda Labs Mobile Gallery", 
description="""A wonderful gallery displaying the amazing projects built in
Lambda Labs with a Mobile App focus.""")

r_labs_hall = Room(title="Lambda Labs Building Back Hallway", 
description="""Leads to the back of the Lambda Labs Building
where it's galleries are held""")



#student center building 

r_student_center = Room(title="Lambda Student Center Building", 
description="""Here students come in the rare occurences they aren't behind their computer.""")

r_game_rooms = Room(title="Lambda Gaming Center", 
description="""Student's come here to win glory.""")

r_cafeteria = Room(title="Lambda Cafeteria", 
description="""Stay away from the chili...""")

r_pool = Room(title="Lambda Pool", 
description="""Students can swim here""")

r_gym = Room(title="Lambda Gym", 
description="""Students can pump iron here.""")

r_bb_court = Room(title="Lambda Basketball Court", 
description="""Students try to ball up here.(keyword=try)""")

r_student_hall = Room(title="Student Center Back Hallway", 
description="""Leads to the back of the Student Center Building""")



#admin building 

r_admin = Room(title="Lambda Administration Department Main Building", 
description="""Lambda Employees main place of operation.""")

r_tl_lounge = Room(title="Lambda Team Lead Lounge", 
description="""Team Leads little getaway.""")

r_teacher_lounge = Room(title="Lambda Teacher Lounge", 
description="""Teachers hide from students here.""")

r_office1 = Room(title="Ryan Allred's Office", 
description="""Here is where Ryan romes.""")

r_office2 = Room(title="Austen Allred's Office", 
description="""Here is where Austen get's it done.""")

r_office3 = Room(title="Ben Nelson's Office", 
description="""Here is where Ben is Ben.""")

r_admin_hall = Room(title="Administration Building Back Hallway", 
description="""Leads to the back of the Admin Building""")



#careers building 

r_career_building = Room(title="Lambda Careers Building", 
description="""Here students come for help on the job search.""")

r_career_help = Room(title="Careers Help Office", 
description="""Here students can pop in for general career questions""")

r_career_office_ux = Room(title="UX Career Office", 
description="""Student's come here for UX related career questions.""")

r_career_office_web = Room(title="Web Career Office", 
description="""Student's come here for Web related career questions.""")

r_career_office_ios = Room(title="IOS Career Office", 
description="""Student's come here for IOS related career questions.""")

r_career_office_ds = Room(title="Data Science Career Office", 
description="""Student's come here for Data Science related career questions.""")

r_career_hall = Room(title="Administration Building Back Hallway", 
description="""Leads to the back of the Admin Building""")



#student housing building 

r_housing_student = Room(title="Lambda Student Housing", 
description="""This is the main part of the student housing building.""")

r_housing_student_lounge = Room(title="Student Housing Lounge, 
description="""Students come here to chill.""")

r_housing_student_kitchen = Room(title="Student Housing Kitchen", 
description="""Students try to make their own food here.""")

r_housing_student_hall = Room(title="Student Housing Back Hall", 
description="""Hall provides access to the different housing wings""")

r_housing_student_alpha = Room(title="Student Housing Alpha Wing", 
description="""How those living in the Alpha Wing of the Student Building 
access their Quarters. You must be living here to go further.""")

r_housing_student_beta = Room(title="Student Housing Beta Wing", 
description="""How those living in the Beta Wing of the Student Building 
access their Quarters. You must be living here to go further.""")

r_housing_student_charlie = Room(title="Student Housing Charlie Wing", 
description="""How those living in the Charlie Wing of the Student Building 
access their Quarters. You must be living here to go further.""")



#staff housing building 

r_housing_staff = Room(title="Lambda Staff Housing", 
description="""This is the main part of the staff housing building.""")

r_housing_staff_lounge = Room(title="Staff Housing Lounge, 
description="""Staff come here to chill.""")

r_housing_staff_kitchen = Room(title="Staff Housing Kitchen", 
description="""Staff make their own food here.""")

r_housing_staff_hall = Room(title="Staff Housing Back Hall", 
description="""Hall provides access to the different staff housing wings""")

r_housing_staff_alpha = Room(title="Staff Housing Alpha Wing", 
description="""How those living in the Alpha Wing of the Staff Building 
access their Quarters. You must be living here to go further.""")

r_housing_staff_beta = Room(title="Staff Housing Beta Wing", 
description="""How those living in the Beta Wing of the Staff Building 
access their Quarters. You must be living here to go further.""")

r_housing_staff_charlie = Room(title="Staff Housing Charlie Wing", 
description="""How those living in the Charlie Wing of the Staff Building 
access their Quarters. You must be living here to go further.""")



#admin housing building 

r_housing_admin = Room(title="Lambda Administration Housing", 
description="""This is the main part of the administration housing building.""")

r_housing_admin_lounge = Room(title="Administration Housing Lounge, 
description="""Administration come here to chill.""")

r_housing_admin_kitchen = Room(title="Administration Housing Kitchen", 
description="""Administration make their own food here.""")

r_housing_admin_hall = Room(title="Administration Housing Back Hall", 
description="""Hall provides access to the different administration housing wings""")

r_housing_admin_alpha = Room(title="Administration Housing Alpha Wing", 
description="""How those living in the Alpha Wing of the Administration Building 
access their Quarters. You must be living here to go further.""")

r_housing_admin_beta = Room(title="Administration Housing Beta Wing", 
description="""How those living in the Beta Wing of the Administration Building 
access their Quarters. You must be living here to go further.""")

r_housing_admin_charlie = Room(title="Administration Housing Charlie Wing", 
description="""How those living in the Charlie Wing of the Administration Building 
access their Quarters. You must be living here to go further.""")



#all saves below

r_campus_welcome_center.save()
r_campus_courtyard_south.save()
r_campus_courtyard_north.save()
r_campus_courtyard_mid.save()
r_campus_courtyard_east.save()
r_campus_courtyard_west.save()


r_ds_building.save()
r_ds_help.save()
r_ds_u1.save()
r_ds_u2.save()
r_ds_u3.save()
r_ds_u4.save()
r_ds_hall.save()


r_web_building.save()
r_web_help.save()
r_web_u1.save()
r_web_u2.save()
r_web_u3.save()
r_web_u4.save()
r_web_hall.save()


r_android_building.save()
r_and_help.save()
r_and_u1.save()
r_and_u2.save()
r_and_u3.save()
r_and_u4.save()
r_and_hall.save()


r_ios_building.save()
r_ios_help.save()
r_ios_u1.save()
r_ios_u2.save()
r_ios_u3.save()
r_ios_u4.save()
r_ios_hall.save()


r_ux_building.save()
r_ux_help.save()
r_ux_u1.save()
r_ux_u2.save()
r_ux_u3.save()
r_ux_u4.save()
r_ux_hall.save()


r_cs_building.save()
r_cs_help.save()
r_cs_u1.save()
r_cs_u2.save()
r_cs_bw1_gal.save()
r_cs_bw2_gal.save()
r_cs_hall.save()


r_labs_building.save()
r_labs_help.save()
r_labs_team_room.save()
r_labs_hall.save()
r_labs_ds_display.save()
r_labs_web_display.save()
r_labs_mobile_display.save()


r_student_center.save()
r_game_rooms.save()
r_cafeteria.save()
r_student_hall.save()
r_bb_court.save()
r_pool.save()
r_gym.save()


r_admin.save()
r_tl_lounge.save()
r_teacher_lounge.save()
r_office1.save()
r_office2.save()
r_office3.save()
r_admin_hall.save()


r_career_building.save()
r_career_help.save()
r_career_office_ux.save()
r_career_office_ios.save()
r_career_office_web.save()
r_career_office_ds.save()
r_career_hall.save()


r_path_housing.save()
r_garden.save()
r_rec_fields.save()

r_housing_square.save()
r_housing_student.save()
r_housing_staff.save()
r_housing_admin.save()

r_housing_student_lounge.save()
r_housing_student_kitchen.save()
r_housing_student_hall.save()
r_housing_student_alpha.save()
r_housing_student_beta.save()
r_housing_student_charlie.save()

r_housing_staff_lounge.save()
r_housing_staff_kitchen.save()
r_housing_staff_hall.save()
r_housing_staff_alpha.save()
r_housing_staff_beta.save()
r_housing_staff_charlie.save()

r_housing_admin_lounge.save()
r_housing_admin_kitchen.save()
r_housing_admin_hall.save()
r_housing_admin_alpha.save()
r_housing_admin_beta.save()
r_housing_admin_charlie.save()







# Link welcome center

r_campus_welcome_center.connectRooms(r_campus_courtyard_south, "n")
r_campus_courtyard_south.connectRooms(r_campus_welcome_center, "s")

#connect courtyards

r_campus_courtyard_south.connectRooms(r_campus_courtyard_mid, "n")
r_campus_courtyard_mid.connectRooms(r_campus_courtyard_south, "s")

r_campus_courtyard_mid.connectRooms(r_campus_courtyard_north, "n")
r_campus_courtyard_north.connectRooms(r_campus_courtyard_mid, "s")

r_campus_courtyard_mid.connectRooms(r_campus_courtyard_east, "e")
r_campus_courtyard_east.connectRooms(r_campus_courtyard_mid, "w")

r_campus_courtyard_mid.connectRooms(r_campus_courtyard_west, "w")
r_campus_courtyard_west.connectRooms(r_campus_courtyard_mid, "e")



#connect buildings


#south 
r_campus_courtyard_south.connectRooms(r_student_center, "e")
r_student_center.connectRooms(r_campus_courtyard_south, "w")


#housing path
r_campus_courtyard_south.connectRooms(r_path_housing, "w")
r_path_housing.connectRooms(r_campus_courtyard_south, "e")

r_path_housing.connectRooms(r_garden, "n")
r_garden.connectRooms(r_path_housing, "s")

r_path_housing.connectRooms(r_rec_fields, "s")
r_rec_fields.connectRooms(r_path_housing, "n")

r_path_housing.connectRooms(r_housing_sqaure, "w")
r_housing_sqaure.connectRooms(r_path_housing, "e")

r_housing_sqaure.connectRooms(r_housing_staff, "n")
r_housing_staff.connectRooms(r_housing_sqaure, "s")

r_housing_sqaure.connectRooms(r_housing_student, "w")
r_housing_student.connectRooms(r_housing_sqaure, "e")

r_housing_sqaure.connectRooms(r_housing_admin, "s")
r_housing_admin.connectRooms(r_housing_sqaure, "n")


#east
r_campus_courtyard_east.connectRooms(r_ios_building, "e")
r_ios_building.connectRooms(r_campus_courtyard_east, "w")

r_campus_courtyard_east.connectRooms(r_web_building, "n")
r_web_building.connectRooms(r_campus_courtyard_east, "s")

r_campus_courtyard_east.connectRooms(r_android_building, "s")
r_android_building.connectRooms(r_campus_courtyard_east, "n")


#west
r_campus_courtyard_west.connectRooms(r_ds_building, "n")
r_ds_building.connectRooms(r_campus_courtyard_west, "s")

r_campus_courtyard_west.connectRooms(r_cs_building, "s")
r_cs_building.connectRooms(r_campus_courtyard_west, "n")

r_campus_courtyard_west.connectRooms(r_ux_building, "w")
r_ux_building.connectRooms(r_campus_courtyard_west, "e")


#north
r_campus_courtyard_north.connectRooms(r_admin, "n")
r_admin.connectRooms(r_campus_courtyard_north, "s")

r_campus_courtyard_north.connectRooms(r_labs_building, "e")
r_labs_building.connectRooms(r_campus_courtyard_north, "w")

r_campus_courtyard_north.connectRooms(r_career_building, "w")
r_career_building.connectRooms(r_campus_courtyard_north, "e")


#south
#student center -- courtyard is west
r_student_center.connectRooms(r_student_hall, "e")
r_student_hall.connectRooms(r_student_center, "w")

r_student_center.connectRooms(r_game_rooms, "n")
r_game_rooms.connectRooms(r_student_center, "s")

r_student_center.connectRooms(r_cafeteria, "s")
r_cafeteria.connectRooms(r_student_center, "n")

r_student_hall.connectRooms(r_bb_court, "e")
r_bb_court.connectRooms(r_student_hall, "w")

r_student_hall.connectRooms(r_gym, "n")
r_gym.connectRooms(r_student_hall, "s")

r_student_hall.connectRooms(r_pool, "s")
r_pool.connectRooms(r_student_hall, "n")

#east
#ios -- courtyard is w
r_ios_building.connectRooms(r_ios_hall, "e")
r_ios_hall.connectRooms(r_ios_building, "w")

r_ios_building.connectRooms(r_ios_help, "s")
r_ios_help.connectRooms(r_ios_building, "n")

r_ios_building.connectRooms(r_ios_u1, "n")
r_ios_u1.connectRooms(r_ios_building, "s")

r_ios_hall.connectRooms(r_ios_u2, "n")
r_ios_u2.connectRooms(r_ios_hall, "s")

r_ios_hall.connectRooms(r_ios_u3, "e")
r_ios_u3.connectRooms(r_ios_hall, "w")

r_ios_hall.connectRooms(r_ios_u4, "s")
r_ios_u4.connectRooms(r_ios_hall, "n")

#web -- courtyard is s

#android -- courtyard is n


#west
#ds -- courtyard is s

#cs -- courtyard is n

#ux -- courtyard is e


#north
#admin -- courtyard is s

#labs -- courtyard is w

#careers -- courtyard is e

#housing admin

#housing staff

#housing students

players=Player.objects.all()
for p in players:
  p.currentRoom=r_campus_welcome_center.id
  p.save()

