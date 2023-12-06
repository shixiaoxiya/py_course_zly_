import pygame  
import os  
import sys  
import pytest  
from all_music import get_resource_path,explosion_large,explosion_small,bg_music

@pytest.fixture  
def all_music():  
    # 在每个测试开始前初始化pygame并播放背景音乐  
    pygame.mixer.init()  
    bg_music()  
    yield  
    # 在每个测试结束后关闭pygame  
    pygame.quit()  
  

  
def test_explosion_large(all_music):  
    # 测试explosion_large函数，检查大爆炸声音是否正确播放  
    explosion_large()  
    # 等待一段时间确保音频已经播放完毕  
    pygame.time.wait(3000)  
  
def test_explosion_small(all_music):  
    # 测试explosion_small函数，检查小爆炸声音是否正确播放  
    explosion_small()  
    # 等待一段时间确保音频已经播放完毕  
    pygame.time.wait(1000)  
  
# def test_bullet_whiz(all_music):  
#     # 测试bullet_whiz函数，检查子弹biu声是否正确播放  
#     bullet_whiz()  
#     # 等待一段时间确保音频已经播放完毕  
#     pygame.time.wait(1000)