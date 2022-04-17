import pygame
from Plane_sprites import *

class PlaneGame(object):
    """Plane game main game"""

    def __init__(self):
        print("Game initialized!")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵跟精灵组
        self.__create_sprites()
        # 4. 设置定时器事件-创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵跟精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵跟精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        print("Game starts!")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2、 事件监听
            self.__event_handler()
            # 3. 碰撞监测
            self.__check_collide()
            # 4. 更新/绘制精灵
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()
            pass
    def __event_handler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("Enemy is coming")
                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("Moving to the right")
        # 使用键盘提供的方法获取键盘按键-元组
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0




    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def __game_over():
        print("Game over")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # create a game
    game = PlaneGame()

    # game starts

    game.start_game()