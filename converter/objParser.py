class ObjParser(object):
    vertexes = []
    normals = []
    polygons = []

    def __init__(self):
        print("Init ObjParser")

    def loadFile(self):
        f = open("../input/cube.obj", "r")
        for line in f:
            if line.startswith('vn'):
                self.normals.append(line)
                print(self.normals)
            elif line.startswith('v'):
                self.vertexes.append(line)
                print(self.vertexes)
            elif line.startswith('f'):
                self.polygons.append(line)
                print(self.polygons)
