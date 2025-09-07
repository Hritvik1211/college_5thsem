def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Word count: {len(words)}")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    file_path = input("Enter the path to the text file: ")
    count_words_in_file(file_path)
