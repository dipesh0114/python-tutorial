# file = open ('youtube.txt', 'w')

# try:
#     file.write("chai aaur code")

# finally:
#     file.close()    


with open('youtube.txt', 'w') as file:
    try:
        file.write("chai aaur code")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("File written successfully.")
    finally:
        print("File operation completed.")

try:
    with open('you.txt', 'r') as file:
        file.read()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File was read successfully.")
finally:
    print("File operation completed.")

