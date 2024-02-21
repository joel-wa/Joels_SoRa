from sceneObjects import SceneObject as so
import json
from scene import SceneClass
from util import UtilClass


scene = SceneClass([],{})


util = UtilClass()
a,b = util.read_shape_data(r"C:\Users\RanVic\OneDrive\Documents\GitHub\Joels_SoRa\sphere.txt")

cube  = so("cube",0,a,b)


# ball = so("ball", 0)
# floor = so("floor", -1)


# scene.addObject("sphere",sphere)
scene.addObject("cube",cube)


def getObject(key):
    desired_object = next(obj for obj in scene.sceneMap.values() if obj.name == key)
    return desired_object

def getSceneObjects():
    keys = []
    for obj in scene.sceneMap.values():
        key = obj.name
        keys.append(key)
    return keys

def readTimeFrameFromFile(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]


timeFrame = readTimeFrameFromFile("timeframeScript.txt")


print(timeFrame)
timeIndex = 0
for frame in timeFrame:

    print(f"At {timeIndex}")

    for obj_key, obj_value in frame.items():
            
            if obj_key in getSceneObjects():
                
                getObject(obj_key).position = float(obj_value)
                print(f"{obj_key}:", getObject(obj_key).position)

    timeIndex += 1
