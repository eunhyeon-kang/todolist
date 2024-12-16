# 20212105 KangEunHyeon
# Date : 2024.12.16
# ToDoList

# 할 일 추가하기 
def add_task(task_list):
    task = input("What Add to list?:")
    deadline = input("Enter the deadline : ex) 2001.03.15 ") # 데드라인 확인 가능을 추가
    task_list.append((task,deadline)) # 데드라인이 같이 보여지게끔 추가
    print()  # 줄 바꿈 용 코드
    print(f"{task}, deadline {deadline} is added. ") # 같이 출력 할 수 있게 함.
    print()

# 할 일 제거하기 
def remove_task(task_list):
    print("To do list")
    for i, (task, deadline) in enumerate(task_list):
        print(f"{i+1}.{task} (deadline : {deadline})")
    index = int(input("Enter the number you want to remove: ")) -1
    if 0 <= index < len(task_list):
        removed_task, removed_deadline = task_list.pop(index)
        print()
        print(f"{removed_task} (deadline : {removed_deadline}) is removed to list")
    else:
        print("Invaild number. Please try again.")
    print()

# 할 일 확인하기
def print_list(task_list):
    print("To do list")
    for i, (task, deadline) in enumerate(task_list):
        print(f"{i+1}. {task} (deadline : {deadline})")
    print()

# 실행 코드
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