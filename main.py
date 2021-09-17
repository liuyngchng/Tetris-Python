import requirements
import pygame
import screens, events, functions, interface
from settings import Settings
from squares import Squares
import player


def game_start():
    # initialisations
    pygame.init()

    status = functions.Status()         # 描述游戏状态的类
    st = Settings()                     # 实例化参数设置

    screen = pygame.display.set_mode(st.screen_size)    # 初始化屏幕区域
    pygame.display.set_caption(st.screen_name)          # 设置屏幕标题

    func = functions.Functions(st, screens.get_func_surface(screen, st))    # 实例化功能区
    sqs = Squares(st, status, screens.get_sqs_surface(screen, st))          # 实例化

    ai = player.AI()             # 实例化AI类
    # main loop
    while True:
        pygame.display.flip()
        events.check_events(sqs, status, ai)
        if status.is_game_active():
            if sqs.update():
                screens.update_screen(screen, sqs, func, status, st)
        elif status.is_game_over():
            interface.game_over(screen, st)
        elif status.is_game_new():
            interface.start(screen, st)
        elif status.is_game_renew():
            ai_mode = status.new_AI
            status.refresh()
            status.game_status = status.ACTIVE
            sqs = Squares(st, status, screens.get_sqs_surface(screen, st))
            st = Settings()
            if ai_mode:
                status.ai = True
                sqs.st.adjust_for_ai()
        else:
            raise RuntimeError  # this should never happen


if __name__ == "__main__":
    requirements.check()
    game_start()
