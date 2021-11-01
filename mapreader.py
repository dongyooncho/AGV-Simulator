from xml.etree import ElementTree
from res import vehicle, node

tree = ElementTree.parse('example.xml')
root = tree.getroot()

image = root.find("img")
mapdata = root.find("map")
ports = root.find("ports")
waits = root.find("waits")
vehicles = root.find("vehicles")
nodes = root.find("nodes")
paths = root.find("path")

# read image data
img_path = image.find("img_path").text
img_name = image.find("name").text

# read map size, scale and capa
map_width = int(mapdata.find("width").text)
map_scale = int(mapdata.find("scale").text)
map_capa = int(mapdata.find("capa").text)

# read nodes
node_list = []
xml_node_list = nodes.findall("node")
for x in xml_node_list:
    a = node.Node(int(x.find("num").text), int(x.find("x").text), int(x.find("y").text))
    if x.find("isCross").text == "Y":
        a.isCross = True
    node_list.append(a)

# read vehicles
vehicle_list = []
xml_vehicle_list = vehicles.findall("vehicle")
for x in xml_vehicle_list:
    a = vehicle.Vehicle(x.find("name").text)
    a.TYPE = x.find("type").text
    a.WIDTH = int(x.find("width").text)
    a.HEIGHT = int(x.find("height").text)
    a.DIAGONAL = int(x.find("diagonal").text)
    a.ROTATE_SPEED = int(x.find("rotate_speed").text)
    a.ACCEL = float(x.find("accel").text)
    a.MAX_SPEED = int(x.find("max_speed").text)
    a.LU_TYPE = x.find("lu_type").text
    a.CHARGE_SPEED = float(x.find("charge_speed").text)
    a.DISCHARGE_WAIT = float(x.find("discharge_wait").text)
    a.DISCHARGE_WORK = float(x.find("discharge_work").text)
    a.node = int(x.find("start_node").text)
    # a.x
    # a.y
    a.velocity = 0
    a.angle = int(x.find("start_angle").text)
    a.battery = 100

    vehicle_list.append(a)

