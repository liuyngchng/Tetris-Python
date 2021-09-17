import pygame


class Settings:
    def __init__(self):
        # times or  speed, in seconds, you can adjust this if youre not satisfied by the default
        self.time_drop = 0.8  # period to force drop
        self.time_drop_adjust = 0.99  # every score up, decrease drop time by this factor
        self.time_stop = 0.5  # time player can adjust pos at bottom
        self.time_move = 0.05  # minimum time interval to move
        self.time_rotate = 0.2  # minimum time interval to rotate
        self.time_to_quick = 0.15  # time interval to activate quick move mode
        self.time_before_drop = 0.3  # time to wait from one stop to drop
        self.time_quick_drop = 0.01  # minimum time interval to drop in quick mode
        self.time_move_quick = 0.015  # minimum time interval to move in quick mode
        self.time_to_straight_drop = 0.3  # time to do another down straight

        # colors, you can change it to be an artist
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (255, 0, 255),
            'cyan': (0, 255, 255),

            'none': (45, 45, 45),  # dark grey
            'tip': (100, 100, 100)  # grey
        }

        self.bg_color = (30, 30, 30)  # black
        self.square_color = (245, 245, 245)  # white
        self.space_color = (35, 35, 35)  # slightly lighter than bg

        # shapes, dont touch this if you are not clear what this dose
        self.shapes = (
            {'pos': ([-1, 0], [0, -1], [0, 1]), 'color': 'red', 'rotate': 4},  # _|_
            {'pos': ([-1, 0], [0, -1], [-1, 1]), 'color': 'green', 'rotate': 2},  # _|-
            {'pos': ([-1, 0], [-1, -1], [0, 1]), 'color': 'blue', 'rotate': 2},  # -|_
            {'pos': ([-1, 0], [-1, 1], [0, 1]), 'color': 'yellow', 'rotate': 1},  # ::
            {'pos': ([-1, 0], [-2, 0], [1, 0]), 'color': 'purple', 'rotate': 2},  # |
            {'pos': ([-1, -1], [0, -1], [0, 1]), 'color': 'cyan', 'rotate': 4},  # |__
            {'pos': ([-1, 1], [0, -1], [0, 1]), 'color': 'white', 'rotate': 4}  # --|
        )

        self.shape_num = len(self.shapes)               # 下落图形的数量

        # positions
        self.square_num_x = 12                          # 屏幕宽度的方格数
        self.square_num_y = 20                          # 屏幕高度的方格数
        self.square_length = 30                         # 游戏区每个小方格的边长
        self.square_space = 5                           # 游戏区小方格和小方格之间的空隙

        # 新出现的形状所在位置坐标
        self.new = [1, int(self.square_num_x / 2)]      # upper center

        # surfaces
        self.func_width = 300                           # 游戏右侧功能区的宽度（像素数）
        self.game_size = self.get_game_size(self)       # 游戏区的长宽尺寸
        self.func_size = self.get_func_size(self)       # 游戏右侧功能区的长宽尺寸

        self.screen_size = self.get_screen_size(self)   # 整个屏幕区的尺寸
        self.screen_name = "Tetris by Richard Liu"      # 屏幕上方的文字标题

        # texts
        self.text_margin = 10
        self.text_adjust_factor = 5
        self.score = "Score: "
        self.score_font = "Comic Sans MS"
        self.score_size = 120
        self.score_font_adjust = 5
        self.score_color = (255, 255, 255)  # white
        self.score_pos = (10, 10)

        self.start = "Press any key to start, press A to watch AI play"
        self.start_font = "Comic Sans MS"
        self.start_size = 200
        self.start_color = (0, 255, 0)  # green
        self.start_pos = "center"
        self.start_surface = self.adjust_start_size(self)

        self.game_over = "Press any key to play again, press A to watch AI play"
        self.game_over_font = self.start_font
        self.game_over_size = self.start_size
        self.game_over_color = (255, 0, 0)  # red
        self.game_over_pos = "center"
        self.game_over_surface = self.adjust_game_over_size(self)

    def adjust_for_ai(self):
        self.time_drop = 0  # period to force drop
        self.time_drop_adjust = 0  # every score up, decrease drop time by this factor
        self.time_stop = 0  # time player can adjust pos at bottom
        self.time_move = 0  # minimum time interval to move
        self.time_rotate = 0  # minimum time interval to rotate
        self.time_before_drop = 0  # time to wait from one stop to drop
        self.time_quick_drop = 0  # minimum time interval to drop in quick mode
        self.time_move_quick = 0  # minimum time interval to move in quick mode
        self.screen_name = 'Tetris by Richard Liu, AI playing...'

    '''
    获取游戏区的像素尺寸，包括长和宽
    '''

    @staticmethod
    def get_game_size(self):
        # 游戏区x轴的像素数
        x = ((self.square_length + self.square_space) \
             * self.square_num_x) + self.square_space
        # 游戏区y轴的像素数
        y = ((self.square_length + self.square_space) \
             * self.square_num_y) + self.square_space
        return x, y

    '''
    获取功能区的尺寸，包括长和宽
    '''

    @staticmethod
    def get_func_size(self):
        x = self.func_width
        y = self.game_size[1]
        return x, y

    @staticmethod
    def get_screen_size(self):

        x = self.game_size[0] + self.func_size[0]
        y = self.game_size[1]
        return x, y

    @staticmethod
    def adjust_start_size(self):
        adjust = True  # at least calculate surface once
        while adjust:
            font = pygame.font.SysFont(self.start_font, self.start_size)
            surface = font.render(self.start, True, self.start_color)
            # adjust font if it is too big
            adjust = ((surface.get_width() + 2 * self.text_margin) > self.screen_size[0])
            if adjust:
                self.start_size -= self.text_adjust_factor
            else:
                return surface

    @staticmethod
    def adjust_game_over_size(self):
        adjust = True  # at least calculate surface once
        while adjust:
            font = pygame.font.SysFont(self.game_over_font, self.game_over_size)
            surface = font.render(self.game_over, True, self.game_over_color)
            # adjust font if it is too big
            adjust = ((surface.get_width() + 2 * self.text_margin) > self.screen_size[0])
            if adjust:
                self.game_over_size -= self.text_adjust_factor
            else:
                return surface
