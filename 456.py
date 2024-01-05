
import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 定義顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 設置視窗大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game")

# 定義玩家物件
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# 定義敵人物件
enemy_size = 50
enemy_speed = 5
enemy_list = []

# 設定計分
score = 0
font = pygame.font.SysFont(None, 35)

# 函數：新增敵人
def spawn_enemy():
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    enemy_list.append([enemy_x, enemy_y])

# 遊戲主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移動玩家
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # 移動敵人
    for enemy in enemy_list:
        enemy[1] += enemy_speed

        # 碰撞偵測
        if (
            player_x < enemy[0] < player_x + player_size
            and player_y < enemy[1] < player_y + player_size
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # 移除超出螢幕的敵人
        if enemy[1] > height:
            enemy_list.remove(enemy)
            spawn_enemy()
            score += 1

    # 新增敵人
    if random.random() < 0.02:
        spawn_enemy()

    # 清除畫面
    screen.fill(WHITE)

    # 畫出玩家
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # 畫出敵人
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # 顯示分數
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲速度
    pygame.time.Clock().tick(30)
