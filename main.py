import sys
from token_counter import count_tokens_in_directory

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_tokens, total_tokens = count_tokens_in_directory(directory_path)
    
    print("Files ordered by number of tokens (descending):")
    for file_path, tokens in file_tokens:
        print(f"{file_path}: {tokens} tokens")
    
    print(f"\nTotal number of tokens in {directory_path}: {total_tokens}")

if __name__ == "__main__":
    main()
