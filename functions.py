import pygame


class Functions:
    """游戏区右侧的功能区"""

    def __init__(self, st, screen):
        self.st = st
        self.screen = screen

    def show_score(self, score):
        surface = None
        adjust = True                       # at least calculate surface once
        while adjust:
            text = self.st.score + str(score)
            font = pygame.font.SysFont(self.st.score_font, self.st.score_size)
            surface = font.render(text, True, self.st.score_color)
            # adjust score font when it is too big
            adjust = ((surface.get_width() + 2 * self.st.score_pos[0]) > self.st.func_size[0])
            if adjust:
                self.st.score_size -= self.st.score_font_adjust
        self.screen.blit(surface, self.st.score_pos)


class Status:
    """获取当前游戏状态的类"""

    def __init__(self):
        # some numbers
        self.GAMEOVER = 0x0
        self.NEWSTART = 0x1
        self.ACTIVE = 0x2
        self.RENEW = 0x3

        # game status
        self.game_status = self.NEWSTART
        self.refresh()

    def is_game_active(self):
        return self.game_status == self.ACTIVE

    def is_game_over(self):
        return self.game_status == self.GAMEOVER

    def is_game_new(self):
        return self.game_status == self.NEWSTART

    def is_game_renew(self):
        return self.game_status == self.RENEW

    def is_ai(self):
        return self.ai

    def refresh(self):
        self.left = False
        self.right = False
        self.down = False
        self.rotate = False
        self.straight_drop = False
        self.ai = False             # 是否人工智能

        # score status
        self.score = 0
