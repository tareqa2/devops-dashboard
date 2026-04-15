def check_log():
    filename = input("Enter log file name: ")

    try:
        with open(filename, "r") as file:
            print("\n=== ERROR Lines ===")
            found = False
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
                    found = True

            if not found:
                print("No ERROR lines found.")

    except FileNotFoundError:
        print("Error: File not found.")
