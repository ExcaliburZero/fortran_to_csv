from astropy.io import ascii
from os import path
import sys

def main():
    result = validate_arguments(sys.argv)

    if isinstance(result, str):
        print(result)
        sys.exit(1)

    readme = sys.argv[1]
    data_file = sys.argv[2]
    output_file = sys.argv[3]

    fortran_to_csv(readme, data_file, output_file)

def validate_arguments(argv):
    if len(argv) != 4:
        return "Incorrect number of arguments %d, should be %d" % (len(argv) - 1, 3)
    if not path.exists(argv[1]):
        return "The given readme file does not exist: %d" % argv[1]
    if not path.exists(argv[2]):
        return "The given data file does not exist: %d" % argv[2]

def fortran_to_csv(readme, data_file, output_file):
    reader = ascii.get_reader(ascii.Cds, readme=readme)

    data = reader.read(data_file)

    ascii.write(data, output_file, format="csv")

if __name__ == "__main__":
    main()
