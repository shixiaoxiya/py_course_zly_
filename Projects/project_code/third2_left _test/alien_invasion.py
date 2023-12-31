import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from all_music import bg_music
from star import Star


def run_game(): 
    """ 初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 初始化声音播放模块
    pygame.mixer.init()

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    continue_button = Button(ai_settings, screen, "Continue")

    # 创建一个用于存储游戏统计信息的实例, 并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ships = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars=Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ships, aliens)
    # 加载背景音乐       
    bg_music()
    """ 开始游戏的主循环"""
    i=0
    while True:
        """ 监视键盘和鼠标事件"""
        gf.check_events(ai_settings, screen, stats, sb, play_button, ships, aliens, bullets)
        
        if stats.game_active:
            i=i+1
            gf.play_bg_music()
            ships.update()
            if i<=2:
                gf.create_star(ai_settings.screen_width, ai_settings.screen_height,stars)
            gf.update_bullets(ai_settings, screen, stats, sb, ships, bullets, aliens)
            gf.update_aliens(ai_settings, screen, stats, sb, ships, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ships, aliens, bullets, play_button, continue_button,stars)
    

run_game()
