from common.dos_cmd import DosCmd


def get_devices():
    """
    获取设备信息
    """

    devices_list = []
    result_list = DosCmd().excute_cmd_result('adb devices')
    if len(result_list) >= 2:
        for i in result_list:
            if 'List' in i:
                continue
            devices_info = i.split('\t')
            if devices_info[1] == 'device':
                devices_list.append(devices_info[0])
        return devices_list
    else:
        return None


if __name__ == '__main__':
    print(get_devices())
