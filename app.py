import sqlite3
from enum import Enum


class Menu(Enum):
    add=1
    find_car=2
    print_all=3
    delete_1_car=4
    del_all=5
    exit=6

def display_menu():
    for action in Menu:
        print (f'{action.value}-{action.name}')
    return Menu(int(input("choose one option:")))
    
    


def add_car(con,cur):
       cur.execute(f"INSERT INTO cars(color,model,brand) VALUES ('{input("color:")}', '{int(input("model"))}', '{input("brand")}');")
       con.commit()
def print_all(cur):
       res=cur.execute('SELECT * FROM cars')
       print(res.fetchall())
def find_car(cur):
       target=cur.execute(f"SELECT * FROM cars WHERE brand='{input("what car?")}'")
       print(target.fetchall())

def delete_car(cur,con):
     target=cur.execute(f"DELETE FROM cars WHERE brand='{input("what car to delete?")}'")
     con.commit()
     print("car deleted")

def delete_all(con, cur):
    cur.execute("DELETE FROM cars;")
    con.commit()
    print("All cars deleted")

     
def main():
    while True:
        con = sqlite3.connect('garage.db')
        cur=con.cursor()
        try:
            cur.execute("CREATE TABLE cars (color,model int,brand)")
        except:
            pass
        user_choice=display_menu()
        try:
            if user_choice==Menu.add:add_car(con,cur)  
            if user_choice==Menu.delete_1_car:delete_car(cur,con)
            if user_choice==Menu.del_all:delete_all(con, cur)
            if user_choice==Menu.find_car:find_car(cur)
            if user_choice==Menu.print_all:print_all(cur)
            if user_choice==Menu.exit:exit()
        except Exception as e:
          print("error",e)




if __name__=='__main__':
    main()



