import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    """Plane game sprite"""

    def __init__(self, image_name, speed=1):

        # inherit init from parent class
        super().__init__()

        # attributes
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # moving vertically
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移除屏幕，如果移出，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height

class Enemy(GameSprite):
    """Enemy sprites"""

    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，敌机图片
        super().__init__("./images/enemy1.png")

        # 2. 敌机的初始速度
        self.speed = random.randint(1, 3)
        # 3. 敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. 调用父类方法，保持垂直飞行
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("Enemy is out of the screen, needs to be deleted")

            # kill方法可以讲精灵从所有精灵中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):

        # print("Enemy died %s" % self.rect)
        pass

class Hero(GameSprite):
    """Hero gamesprite"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 创建英雄的初始位置
        self.rect.centerx  = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        print("Shooting")
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """bullet gamesprite"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹没了")


