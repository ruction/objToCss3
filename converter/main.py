from converter import Converter
from exporter import Exporter
from objParser import ObjParser


def main():
    print("######### objToCss3 #########")

    objParser = ObjParser()
    converter = Converter()
    exporter = Exporter()

    objParser.loadFile()
    converter.convert(objParser.vertexes, objParser.normals, objParser.polygons)


if __name__=='__main__':
    main()
