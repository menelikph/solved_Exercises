from Library_Book_Tracker import *
from Student_Grade_Manager import *
from Restaurant_Menu_Editor import *
from Warehouse_Box_Counter import * 
from Movie_Rating_System import *
from Online_Course_Tracker import *
from To_Do_List_Organizer import *
from Digital_Wallet import *
from Pet_Adoption_Center import *
from Gym_Membership_System import *

# importa los demás archivos que quieras probar

# 1. Library Book Tracker
def test_library():
    library.clear()
    add_book("1984", "George Orwell", 328)
    assert "1984" in library
    assert find_book("Unknown") == "Book not found."

# 2. Student Grade Manager
def test_grades():
    grades.clear()
    add_student("Alice")
    add_grade("Alice", 90)
    add_grade("Alice", 80)
    assert get_average("Alice") == 85.0

# 3. Restaurant Menu Editor
def test_menu():
    menu.clear()
    add_dish("Pizza", 10.0, True)
    add_dish("Salad", 5.0, False)
    assert total_available_price() == 10.0

# 4. Warehouse Box Counter
def test_warehouse():
    warehouse.clear()
    add_box("BoxA", 5)
    update_quantity("BoxA", 8)
    assert has_enough("BoxA", 8) is True

# 5. Movie Rating System
def test_movies():
    movies.clear()
    add_movie("Inception")
    rate_movie("Inception", 5)
    rate_movie("Inception", 4)
    assert average_rating("Inception") == 4.5

# 6. Online Course Tracker
def test_courses():
    courses.clear()
    add_course("Python", 50, 20)
    assert "Python" in filter_by_hours(40)

# 7. To-Do List Organizer
def test_todos():
    todos.clear()
    add_task("Task1", "high")
    complete_task("Task1")
    filtered = filter_tasks(priority="high", status="completed")
    assert len(filtered) == 1

# 8. Digital Wallet
def test_wallet():
    wallet.clear()
    add_expense("food", 100)
    add_expense("transport", 50)
    percentages = expense_percentages()
    assert round(percentages["food"], 1) == 66.7

# 9. Pet Adoption Center
def test_pets():
    pets.clear()
    add_pet("Buddy", "dog", 5)
    older = older_than(3)
    assert any(p["name"] == "Buddy" for p in older)

# 10. Gym Membership System
def test_gym():
    members.clear()
    register_member("John", "monthly", "late")
    assert "John" in unpaid_members()
