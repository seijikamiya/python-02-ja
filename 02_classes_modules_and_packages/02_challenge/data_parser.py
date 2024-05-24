from vehicle import Vehicle
import os
import re

def parse_vehicle_data(file_name):
    # 実行ファイルのディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 読み込みたいtxtファイルのパスを指定
    path = os.path.join(script_dir, file_name)

    vehicles = []
    with open(path) as f:
        elements = [l.rstrip() for l in f.readlines()]
        for elem in elements:
            elem = elem.split(",")
            model = elem[0]
            make = elem[1]
            year = int(elem[2])
            price = int(elem[3])
            vehicle = Vehicle(model, make, year, price)
            vehicles.append(vehicle)
        return vehicles

if __name__ == "__main__":
    vehicles = parse_vehicle_data("vehicles.txt")
    print(vehicles)
