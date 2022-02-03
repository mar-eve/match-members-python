#Input files 'testmembers.csv' and 'testattendees.csv' to find matches. 
#Outputs files 'testoutput_members.csv' (for matches) and 'testoutput_non_members' (no match)

import csv
class Profile:
    def __init__(self, murmId, firstName, lastName, email, phone_1, phone_2, phone_3, zip_code):
        self.murmId = murmId
        self.firstName = firstName
        self.lastName = lastName
        self.phone_1 = phone_1
        self.phone_2 = phone_2
        self.phone_3 = phone_3
        self.email= email
        self.zip_code=zip_code


    
#remove parenthesis and dashes, and begin phone with 1
def remove_non_integers(phone):
    fixed_phone = ""
    for element in phone:
        if(element.isdigit()):
            fixed_phone = fixed_phone + element
    if(len(fixed_phone) < 11 and len(fixed_phone) != 0):
        fixed_phone = '1' + fixed_phone       
    return fixed_phone



def write_csv(list, filename):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Id','First', 'Last', 'Email', 'Phone1', 'Phone2','Phone3','Zip Code'])
        for obj in list:
            csvwriter.writerow([obj.murmId, obj.firstName, obj.lastName, obj.email, obj.phone_1, obj.phone_2, obj.phone_3, obj.zip_code])
     
    


def read_csv(list, filename):
     with open(filename) as members:
          csv_reader = csv.reader(members, delimiter=',')
          line_count = 0
          for row in csv_reader:
              if line_count == 0:
                  line_count +=1
              else:
                  row[3] = row[3].lower()
                  row[4] = remove_non_integers(row[4])
                  row[5] = remove_non_integers(row[5])
                  row[6] = remove_non_integers(row[6])
                  list.append(Profile(row[0],row[1],row[2],row[3],row[4], row[5],row[6],row[7]))
          return list          

def match(members, attendees):
    attendee_members = []
    attendee_non_members = []
    found = 0;
    for obj in attendees:
        print(obj.email)

    for obj_attendee in attendees:
        for obj_member in members:
            if( (found == 0 and obj_attendee.firstName.lower() == obj_member.firstName.lower() and obj_attendee.lastName.lower() == obj_member.lastName.lower()) and
                 (obj_attendee.email == obj_member.email
                 or obj_attendee.phone_1 == obj_member.phone_1
                 or obj_attendee.phone_1 == obj_member.phone_2
                 or obj_attendee.phone_1 == obj_member.phone_3) ):
                found = 1
                attendee_members.append(Profile(obj_member.murmId,obj_member.firstName, obj_member.lastName, obj_member.email, obj_member.phone_1, obj_member.phone_2,obj_member.phone_3, obj_member.zip_code))
              

        if (found == 0):
            attendee_non_members.append(Profile(obj_attendee.murmId,obj_attendee.firstName, obj_attendee.lastName, obj_attendee.email, obj_attendee.phone_1, obj_attendee.phone_2,obj_attendee.phone_3, obj_attendee.zip_code))                            
        found = 0;
        
    write_csv(attendee_members, 'testoutput_members.csv')
    write_csv(attendee_non_members, 'testoutput_non_members.csv')                                    



def main():

      members = []
      attendees = []

      filename= 'testmembers.csv'
      members = read_csv(members, filename)
      filename_attendees = 'testattendees.csv'
      attendees = read_csv(attendees, filename_attendees)

      match(members, attendees)

  
 
main()    

        
