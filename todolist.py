# 20212105 KangEunHyeon
# Date : 2024.12.16
# ToDoList

# 할 일 추가하기 함수입니다.
def add_task(task_list):
    task = input("What Add to list?:")
    # 데드라인 확인 가능을 추가했습니다.
    deadline = input("Enter the deadline : ex) 2001.03.15 ")
    # 중요도 기능 추가했습니다.
    importnat = input("Enter the importance : ex) 중요, 보통, 낮음 ")
    # 데드라인, 중요도 출력 될 수 있게 추가 하였습니다.
    task_list.append((task, deadline, importnat))
    # 줄 바꿈 용 코드입니다.
    print()  
     # 같이 출력 할 수 있게 수정했습니다.
    print(f"{task}, deadline {deadline}, importance {importnat} is added. ") 

# 할 일 제거하기 함수입니다.
def remove_task(task_list):
    print("To do list")
    for i, (task, deadline, importnat) in enumerate(task_list):
        # 성능 2개 추가했습니다.
        print(f"{i+1}. {task} (deadline: {deadline}, importance: {importnat})")
    index = int(input("Enter the number you want to remove: ")) -1
    if 0 <= index < len(task_list):
        removed_task, removed_deadline, removed_importnat = task_list.pop(index)
        print()
        print(f"{removed_task} (deadline : {removed_deadline}), importance: {removed_importnat}) is removed from the list.")
    else:
        print("Invaild number. Please try again.")
    print()

# 할 일 확인하기 함수입니다.
def print_list(task_list):
    print("To do list")
    for i, (task, deadline, importnat) in enumerate(task_list):
        # 두 기능을 다 출력할 수 있게 추가하였습니다.
        print(f"{i+1}. {task} (deadline: {deadline}, importance: {importnat})")
    print()

# 실행 코드 함수입니다.
def main():
    to_do_list = []
    while True:
        print("1. Add to list")
        print("2. Remove task")
        print("3. Print <To do list>")
        print("4. End the program")

        choice = input("Enter the number you want to do: ")
        print()

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            remove_task(to_do_list)
        elif choice == "3":
            print_list(to_do_list)
        elif choice == "4":
            print("End the program. Thak you. ")
            break
        else:
            print("Invalid choice. Please try again. ")

if __name__ == "__main__":
    main()