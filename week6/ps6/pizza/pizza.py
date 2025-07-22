import sys
import tabulate
import csv

def main():
    if len(sys.argv) == 1:
        print("Too few Command Line Arguments")
        sys.exit(1)
    elif len(sys.argv)>2:
        print("Too many Command Line Arguments")
        sys.exit(2)
    else:
        try:
            print("File Found")
            filename = sys.argv[1]
            dot = filename.find('.')
            if filename[dot:] != '.csv':
                sys.exit(3)
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                table = []
                headers = list(next(reader))
                for row in reader:
                    table.append([row[0], row[1], row[2]])

            print(tabulate.tabulate(table, headers, tablefmt="grid"))

        except FileNotFoundError:
            print("File does not exist!!")
            sys.exit()


if __name__ == "__main__":
    main()
