import sqlite3

connection = sqlite3.connect('POSTLAB_3.db')

cursor = connection.execute('select *from ADVENTURE_TRIP')

for row in cursor:
    TRIP_ID = row[0]
    TRIP_NAME = row[1]
    START_LOCATION = row[2]
    STATE = row[3]
    DISTANCE = row[4]
    MAX_GRP_SIZE= row[5]
    TYPE = row[6]
    SEASON = row[7]
    
    print('DATA:','\n',TRIP_ID,
          '\t',TRIP_NAME,'\t',START_LOCATION,
          '\t',STATE,'\t',DISTANCE,
          '\t',MAX_GRP_SIZE,
          '\t',TYPE,'\t',SEASON)
 
connection.execute('''insert into MUSIC_TRIP (Rock,Jazz,Blues) 
                   values('Bohemian_Rhapsody','My_Girl','Zombie')''')
connection.commit()
cursor = connection.execute('select *from MUSIC_TRIP')
for row in cursor:
    Rock = row[0]
    Jazz = row[1]
    Blues = row[2]
    
    
    print('SONGS:','\n',Rock,
          '\n',Jazz,'\n',Blues)