# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import sys
import os
import yaml
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
file_path = (rootPath+'/config/device.yaml')


class ReadYaml(object):

    def read_data(self):
        """
        加载yaml数据
        :return:
        """
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_value(self, key, port):
        """
        获取value
        :param key:
        :param value:
        :return:
        """
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        """
        写入数据
        :param i:
        :param device:
        :param bp:
        :param port:
        :return:
        """
        self.clear_data()
        data = self.join_data(i, device, bp, port)
        with open(file_path, "a", encoding="utf-8") as fr:
            yaml.dump(data, fr)
        fr.close()

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(file_path, "w", encoding="utf-8") as f:
            f.truncate()
        f.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    readYaml = ReadYaml()
    device = readYaml.get_value("user_info_0", "port")
    print(device)
