from sceneObjects import SceneObject

class SceneClass:
    def __init__(self,sceneObjects,sceneMap):
        self.sceneObjects = sceneObjects
        self.sceneMap = sceneMap

    def translateObject(self,key,x=0,y=0,z=0):
        self.sceneMap[key].translate(x,y,z)

    def rotateObject(self,key,rotation):
        self.sceneMap[key].rotation = rotation

    def addObject(self,key,object):
        self.sceneMap[key] = object

    def removeObject(self,key):
        self.sceneObjects.pop(key)


    def drawScene(self):
        for object in self.sceneMap.values():
            object.draw()
        return

    