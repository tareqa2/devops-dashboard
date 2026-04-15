import sysinfo
import logcheck
import tasklist

def main():
    while True:
        print("\n=== DevOps Dashboard ===")
        print("[1] System Info")
        print("[2] Log Checker")
        print("[3] Task List")
        print("[0] Exit")

        choice = input("Select an option: ")

        if choice == "1":
            sysinfo.show_sysinfo()
        elif choice == "2":
            logcheck.check_log()
        elif choice == "3":
            print("Coming soon...")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
