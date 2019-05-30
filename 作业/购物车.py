import os

product_list = [['Iphone7', 5800],
                ['Coffee', 30],
                ['疙瘩汤', 10],
                ['Python Book', 99],
                ['Bike', 199],
                ['ViVo X9', 2499],
                ]

shopping_cart = {}  # 购物车
current_userinfo = []  # 用户信息
login = False  # 登录标志
db_file = r'users.txt'

while True:
    print('1.登陆 2.注册 3.购物')
    choice = input('>>: ').strip()
    # 1.登录
    if choice == '1':
        if login == False:
            tag = True  # 标志位
            count = 0  # 错误次数
            while tag:
                if count == 3:
                    print('\033[45m尝试次数过多，退出。。。\033[0m')
                    break
                uname = input('用户名：').strip()
                pwd = input('密码：').strip()
                with open(db_file, 'r', encoding='utf-8') as f:  # 读取文件验证用户
                    for line in f:
                        line = line.strip('\n')
                        user_info = line.split('|')  # 切割字符串
                        uname_of_db = user_info[0]  # 用户名
                        pwd_of_db = user_info[1]  # 密码
                        balance_of_db = int(user_info[2])  # 余额
                        if uname == uname_of_db and pwd == pwd_of_db:
                            login = True    # 更改登录标志
                            print('\033[48m登陆成功\033[0m')
                            current_userinfo = [uname_of_db, balance_of_db]  # 登陆成功则将用户名和余额添加到列表
                            print('用户信息为：', current_userinfo)
                            tag = False  # 标志位更改
                            break
                    else:
                        print('\033[47m用户名或密码错误\033[0m')
                        count += 1
        else:
            print('您已经登录！')

    elif choice == '2':
        uname = input('请输入用户名：').strip()
        while True:
            pwd1 = input('请输入密码：').strip()
            pwd2 = input('再次确认密码：').strip()
            if pwd2 == pwd1:
                break
            else:
                print('\033[39m两次输入密码不一致，请重新输入！！!\033[0m')
        balance = input('请输入充值金额：').strip()
        with open(db_file, 'a', encoding='utf-8') as f:  # 写文件到txt中
            f.write('%s,%s,%s\n' % (uname, pwd1, balance))

    elif choice == '3':
        if len(current_userinfo) == 0:  # 判断当前是否有用户登录
            print('\033[49m请先登陆...\033[0m')
            break
        else:
            # 登陆成功后，开始购物
            uname_of_db = current_userinfo[0]
            balance_of_db = current_userinfo[1]
            print('尊敬的用户[%s] 您的余额为[%s],祝您购物愉快' % (
                uname_of_db,
                balance_of_db
            ))
            tag = True  # 购物循环
            while tag:
                for index, product in enumerate(product_list):  # 使用枚举，循环打印商品列表，product为键值
                    print(index, product)
                choice = input('输入商品编号购物，输入q退出>>: ').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < 0 or choice >= len(product_list):  # 错误选项跳过后续，继续选择输入
                        continue
                    pname = product_list[choice][0]  # p[index][]
                    pprice = product_list[choice][1]
                    if balance_of_db > pprice:   # 判断余额
                        if pname in shopping_cart:  # 原来已经购买过，数量加一
                            shopping_cart[pname]['count'] += 1  # shopping_cart:{ '商品名称':{'pprice':价格, 'count':商品数量},  }
                        else:
                            shopping_cart[pname] = {'pprice': pprice, 'count': 1}  # 添加

                        balance_of_db -= pprice  # 扣钱
                        current_userinfo[1] = balance_of_db  # 用户信息更新用户余额
                        print("添加 " + pname + " 到购物车,\033[42;1my账户\033[0m 余额为" + str(balance_of_db))
                    else:
                        print("买不起，穷逼! 产品价格是{price},你还差{lack_price}".format(
                            price=pprice,
                            lack_price=(pprice - balance_of_db)
                        ))
                    print(shopping_cart)
                elif choice == 'q':
                    print("""
                    ---------------------------------已购买商品列表---------------------------------
                    id          商品                   数量             单价               总价
                    """)
                    total_cost = 0  # 总花费
                    for i, key in enumerate(shopping_cart):
                        print('%22s%18s%18s%18s%18s' % (
                            i,
                            key,
                            shopping_cart[key]['count'],
                            shopping_cart[key]['pprice'],
                            shopping_cart[key]['pprice'] * shopping_cart[key]['count']
                        ))
                        total_cost += shopping_cart[key]['pprice'] * shopping_cart[key]['count']

                    print("""
                    您的总花费为: %s
                    您的余额为: %s
                    ---------------------------------end---------------------------------
                    """ % (total_cost, balance_of_db))

                    while tag:
                        inp = input('确认购买(yes/no?)>>: ').strip()
                        if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                            continue
                        if inp in ['Y', 'y', 'yes']:
                            # 将余额写入文件
                            src_file = db_file
                            dst_file = r'%s.swap' % db_file
                            with open(src_file, 'r', encoding='utf-8') as read_f, \
                                    open(dst_file, 'w', encoding='utf-8') as write_f:
                                for line in read_f:
                                    if line.startswith(uname_of_db):
                                        l = line.strip('\n').split(',')
                                        l[-1] = str(balance_of_db)
                                        line = ','.join(l) + '\n'

                                    write_f.write(line)
                            os.remove(src_file)
                            os.rename(dst_file, src_file)
                            print('购买成功，请耐心等待发货')
                        shopping_cart = {}  # 完成付款 清空购物车和用户
                        current_userinfo = []
                        tag = False
                else:
                    print('输入非法')
    else:
        print('\033[33m非法操作\033[0m')
