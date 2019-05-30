with open('users.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        print(line)
        user_info = line.split('|')  # 切割字符串
        print(user_info)
        uname_of_db = user_info[0]  # 用户名
        pwd_of_db = user_info[1]  # 密码
        balance_of_db = int(user_info[2])
        print(uname_of_db,pwd_of_db,balance_of_db)