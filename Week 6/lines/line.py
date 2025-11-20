import sys

def get_lines(x):
    line = 0
    with open(f"{x}") as file:
        for _ in file:
                if _.strip() == "" or _.strip().startswith('#'):
                    continue
                else:
                     line += 1
        return line  

def main():

    if len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
         sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
    
    try:
         return f"O arquivo possui {get_lines(file_name)} linhas."
    except FileNotFoundError:
         sys.exit("File does not exist")

main()