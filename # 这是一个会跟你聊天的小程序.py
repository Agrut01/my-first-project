# 这是一个会跟你聊天的小程序
print("你好呀！我是你的Python助手 🤖")
print("你叫什么名字？")

# 等待你输入名字
name = input()

# 跟你打招呼
print("太高兴认识你，" + name + "！❤️")
print("我们一起来学编程吧！")import random

# 电脑随机选一个1-100的秘密数字
秘密数字 = random.randint(1, 100)
猜的次数 = 0

print("🎮 我们来玩个游戏吧！请猜一个1到100之间的数字。")

while True:
    # 让你输入猜测的数字
    用户输入 = input("请输入你猜的数字：")
    
    # 把文字转成整数
    guess = int(用户输入)
    猜的次数 = 猜的次数 + 1
    
    if guess < 秘密数字:
        print("📈 太小啦！再往大了猜。")
    elif guess > 秘密数字:
        print("📉 太大啦！再往小了猜。")
    else:
        print(f"🎉 恭喜你！你用了 {猜的次数} 次就猜对了！好厉害！")
        break  # 猜对就退出循环

print("游戏结束，感谢游玩！下次见！👋")import random

# 电脑随机选一个1-100的秘密数字
秘密数字 = random.randint(1, 100)
猜的次数 = 0

print("🎮 我们来玩个游戏吧！请猜一个1到100之间的数字。")

while True:
    # 让你输入猜测的数字
    用户输入 = input("请输入你猜的数字：")
    
    # 把文字转成整数
    guess = int(用户输入)
    猜的次数 = 猜的次数 + 1
    
    if guess < 秘密数字:
        print("📈 太小啦！再往大了猜。")
    elif guess > 秘密数字:
        print("📉 太大啦！再往小了猜。")
    else:
        print(f"🎉 恭喜你！你用了 {猜的次数} 次就猜对了！好厉害！")
        break  # 猜对就退出循环

print("游戏结束，感谢游玩！下次见！👋")import random

# 电脑随机选一个1-100的秘密数字
秘密数字 = random.randint(1, 100)
猜的次数 = 0

print("🎮 我们来玩个游戏吧！请猜一个1到100之间的数字。")

while True:
    # 让你输入猜测的数字
    用户输入 = input("请输入你猜的数字：")
    
    # 把文字转成整数
    guess = int(用户输入)
    猜的次数 = 猜的次数 + 1
    
    if guess < 秘密数字:
        print("📈 太小啦！再往大了猜。")
    elif guess > 秘密数字:
        print("📉 太大啦！再往小了猜。")
    else:
        print(f"🎉 恭喜你！你用了 {猜的次数} 次就猜对了！好厉害！")
        break  # 猜对就退出循环

print("游戏结束，感谢游玩！下次见！👋")