import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few Command Line Arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many Command Line Arguments")
        sys.exit(2)
    else:
        try:
            readfile = sys.argv[1]
            writefile = sys.argv[2]
            dot1 = readfile.find('.')
            dot2 = writefile.find('.')
            if readfile[dot1:] != '.csv' or writefile[dot2:] != '.csv':
                sys.exit(3)

            firstnames = []
            lastnames = []
            house = []

            with open(readfile,"r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last , first = row['name'].split(',')
                    lastnames.append(last.strip())
                    firstnames.append(first.strip())
                    house.append(row['house'])

        except FileNotFoundError:
            print("File does not exist!!")
            sys.exit()

        with open(writefile,'w') as file:
            fieldnames=['first','last','house']
            writer=csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(firstnames)):
                writer.writerow({'first': firstnames[i],'last': lastnames[i],'house': house[i],})


if __name__ == "__main__":
    main()
