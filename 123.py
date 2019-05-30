# 电话本
phone_map = {}
# 是否退出系统
is_over = False
while not is_over:
    # 姓名初始制空，完成只有姓名输入正确才录入电话
    name = ''
    while True:
        # 姓名必须录入正确
        if not name:
            name = input("name：")
            if name == 'q':
                # 退出系统
                is_over = True
                break
            elif not name.isalpha():  # 全为英文
                # 录入错误，置空名字
                print('name error')
                name = ''
                continue
        # 录入电话，保证是11位的数字字符串
        phone = input("phone：")
        if not (phone.isdigit() and len(phone) == 11):
            continue

        # 取组名
        group = name[0:1].upper()
        # 对于组名的操作：无组名，添加分组 | 有组名，不操作
        phone_map.setdefault(group, {})
        phone_map[group][name] = phone
        # 一条信息添加完毕，重置信息
        name = ''
        phone = ''
        print('录入成功')
print(phone_map)