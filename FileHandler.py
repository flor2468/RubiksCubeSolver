from cubies import *


def import_cube_from_csv(filepath):
    """
    imports a cube form a csv file

    the file consists of one header row (Line 1), 26 cubies with their values
    and an empty line (Line 28) and 14 columns whith data
    """
    filehandler = open(filepath)

    content = filehandler.read()

    cubies = []

    rows = content.split('\n')

    for i in range(1, len(rows)-2):
        temp = rows[i].split(',')

        temp_cubie = Cubie(temp[0],
                           int(temp[1]),
                           temp[2],
                           [int(temp[3]), int(temp[4])],
                           temp[5],
                           temp[6],
                           [int(temp[7]), int(temp[8])],
                           temp[9],
                           temp[10],
                           [int(temp[11]), int(temp[12])],
                           temp[13])
        cubies.append(temp_cubie)

    filehandler.close()
    return cubies


def export_cube_to_csv(cubies_list, filepath):
    """
    exports a cube with all its values to a csv file
    """
    filehandler = open(filepath, "w")
    header = "Cubies N,Colors number,Color 1,Pos Color 1 x,Pos Color 1 y," \
             "Identifier,Color 2,Pos Color 2 x,Pos Color 2 y,Identifier,Color 3" \
             ",Pos Color 3 x,Pos Color 3 y,Identifier"
    filehandler.write(header)

    for cubie in cubies_list:
        temp = cubie.name + ","
        temp += str(cubie.number) + ","
        temp += cubie.color1 + ","
        temp += str(cubie.pos1[0]) + ","
        temp += str(cubie.pos1[1]) + ","
        temp += cubie.id1 + ","
        temp += cubie.color2 + ","
        temp += str(cubie.pos2[0]) + ","
        temp += str(cubie.pos2[1]) + ","
        temp += cubie.id2 + ","
        temp += cubie.color3 + ","
        temp += str(cubie.pos3[0]) + ","
        temp += str(cubie.pos3[1]) + ","
        temp += cubie.id3 + "\n"
        filehandler.write(temp)

    endl = ",,,,,,,,,,,,,"
    filehandler.write(endl)
    filehandler.close()
