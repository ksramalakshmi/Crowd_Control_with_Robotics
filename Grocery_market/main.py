import eel
import cv2

eel.init('web')

item_dict = {'Vegetables':(408, 410), "Fruits":(648, 409), "Grains":(895, 689), "Canned Goods":(895, 1032), "Snacks":(398, 1360), "Beverages":(1142, 1365), "Meat":(895, 1360), "Dairy":(1143, 694), "Frozen":(1139, 415), "Household":(642, 1737)}
item_list = []
price = {"Vegetables":60, "Fruits":100, "Grains":140, "Canned Goods":20, "Snacks":50, "Beverages":40, "Meat":100, "Dairy":50, "Frozen":70, "Household":200}
price_total = 0

@eel.expose
def send_python(item_name):
    global item_list
    global price_total
    item_list.append(item_name)
    price_total += price[item_name]
    print(item_list)


@eel.expose
def clear_python():
    global price_total
    global item_list
    item = item_list.pop()
    price_total -= price[item]
    print(item_list)

@eel.expose
def check_pos():
    global item_list
    global item_dict

    img = cv2.imread("storemap.jpg", cv2.IMREAD_COLOR)  

    for item in item_list:
        item_coord = item_dict[item]
        img = cv2.circle(img, item_coord, 60, (255, 0, 0), 5)
        img = cv2.putText(img, str(item_list.index(item)+1), item_coord, cv2.FONT_HERSHEY_SIMPLEX, 
                   3, (0, 0, 255), 5, cv2.LINE_AA)

    cv2.imshow("Store Map", img)
    cv2.waitKey(0)
    return price_total

eel.start('index.html')
