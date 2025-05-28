import csv
from datetime import datetime

filename = "at2.csv"

#reset the file
def reset_attendance_file():
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])
    print("Attendance file reset with headers.")

#get the file with the headers
def initialize_file():
    try:
        with open(filename, "x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name","Date","Time"])
    except FileExistsError:
        pass
#to mark the attendance
def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    with open(filename, "a", newline ='') as file:
        writer = csv.writer(file)
        writer.writerow([name,date,time])
    print(f"attendance marked for{name} at {time}")
    
#to view the whole attendance
    
def view_attendance():
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"\n attendance for today:\n--------------------")
        found =  False
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Date"]==today:
                    print(f"{row['Name']} at {row['Time']}")
                    found = True
        if not found:
            print("No attendance marked today")
#calling it at end
def main():
    initialize_file()
    while True:
        print("\n---Attendance Tracker ---")
        print("1.Mark Attendance")
        print("2.View attendance")
        print("3.reset the attendance")
        print("4.exit")
        choice = input("choose an option:")
        if choice == '1':
            name = input("enter your name:").strip()
            if name:
                mark_attendance(name)
            else:
                print("Name cant be empty")
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            confirm = input("⚠️ Are you sure you want to reset the file? (yes/no): ").lower()
            if confirm == "yes":
                reset_attendance_file()
        elif choice == '4':
            print("exiting")
        else:
            print("invalid option")
if __name__ == "__main__":
    main()
                
            
    
              
    

