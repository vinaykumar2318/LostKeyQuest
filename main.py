from OpenGL.GL import *
from utils.window_manager import Window
from game import Game
import imgui
from imgui.integrations.glfw import GlfwRenderer
import json
import os
import pygame
import OpenGL.GL as gl

def load_texture(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.flip(image, False, True)
    image_data = pygame.image.tostring(image, "RGBA", True)

    width, height = image.get_size()
    texture_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, image_data)

    return texture_id, width, height

class App:
    def __init__(self, width, height):
        self.window = Window(height, width)
        self.game = Game(height, width)
        self.show_main_menu = True
        imgui.create_context()
        self.impl = GlfwRenderer(self.window.window)
        self.save_filename = "save_game.json"
        self.logo_texture, self.logo_width, self.logo_height = load_texture("logo.webp")

    def RenderLoop(self):

        while self.window.IsOpen():
            inputs, time = self.window.StartFrame(0.0, 0.0, 0.0, 1.0)

            self.impl.process_inputs() 
            imgui.new_frame()

            if not self.show_main_menu:
                if self.game.is_game_over:
                    self.show_game_over_screen()
                elif self.game.is_game_won:
                    self.show_you_won_screen()
                else:
                    self.game.ProcessFrame(inputs, time)
            else:
                self.show_main_menu_screen(inputs)

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            self.window.EndFrame()

        if not (self.game.is_game_over or self.game.is_game_won):
            self.save_current_game()
        
        self.window.Close()


    def save_current_game(self):
        data = {
            "map": self.game.current_map,
            "lives": self.game.lives,
            "health": self.game.health,
            "total_time": self.game.total_time,
        }
        with open(self.save_filename, "w") as f:
            json.dump(data, f)

    def show_you_won_screen(self):
        window_width, window_height = 850, 600
        center_x = (self.window.windowWidth - window_width) / 2
        center_y = (self.window.windowHeight - window_height) / 2
        imgui.set_next_window_position(center_x, center_y)
        imgui.set_next_window_size(window_width, window_height)

        imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, 0.75, 0.95, 0.85, 1.0)
        imgui.push_style_color(imgui.COLOR_BORDER, 0.3, 0.7, 0.6, 1.0)
        imgui.push_style_color(imgui.COLOR_TEXT, 0.1, 0.2, 0.2, 1.0)

        imgui.push_style_color(imgui.COLOR_BUTTON, 0.02, 0.84, 0.63, 1.0)
        imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, 0.02, 0.76, 0.56, 1.0)
        imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, 0.01, 0.69, 0.50, 1.0)

        imgui.push_style_var(imgui.STYLE_FRAME_ROUNDING, 15.0)

        imgui.begin("Victory!", True, imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE)

        imgui.set_window_font_scale(6.0)
        title = "🎉 YOU WON! 🎉"
        title_width = imgui.calc_text_size(title)[0]
        imgui.set_cursor_pos_x((window_width - title_width) / 2)
        imgui.text(title)

        imgui.set_window_font_scale(3.0)
        imgui.spacing()
        imgui.spacing()

        time_text = f"Time taken: {int(self.game.total_time)}s"
        time_width = imgui.calc_text_size(time_text)[0]
        imgui.set_cursor_pos_x((window_width - time_width) / 2)
        imgui.text(time_text)

        imgui.spacing()
        imgui.separator()
        imgui.spacing()

        button_width, button_height = 450, 70
        imgui.set_cursor_pos_x((window_width - button_width) / 2)
        imgui.set_cursor_pos_y(280)

        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (20, 20))
        if imgui.button("Return to Main Page", button_width, button_height):
            self.show_main_menu = True  
        imgui.pop_style_var()

        imgui.pop_style_var()  
        imgui.pop_style_color(6)
        imgui.end()

    def show_game_over_screen(self):
        window_width, window_height = 850, 600
        center_x = (self.window.windowWidth - window_width) / 2
        center_y = (self.window.windowHeight - window_height) / 2
        imgui.set_next_window_position(center_x, center_y)
        imgui.set_next_window_size(window_width, window_height)

        imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, 0.75, 0.95, 0.85, 1.0)
        imgui.push_style_color(imgui.COLOR_BORDER, 0.3, 0.7, 0.6, 1.0)
        imgui.push_style_color(imgui.COLOR_TEXT, 0.1, 0.2, 0.2, 1.0)

        imgui.push_style_color(imgui.COLOR_BUTTON, 0.84, 0.02, 0.02, 1.0)
        imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, 0.76, 0.02, 0.02, 1.0)
        imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, 0.69, 0.01, 0.01, 1.0)

        imgui.push_style_var(imgui.STYLE_FRAME_ROUNDING, 15.0)

        imgui.begin("Game Over", True, imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE)

        imgui.set_window_font_scale(6.0)
        title = "💀 GAME OVER 💀"
        title_width = imgui.calc_text_size(title)[0]
        imgui.set_cursor_pos_x((window_width - title_width) / 2)
        imgui.text(title)

        imgui.set_window_font_scale(3.0)
        imgui.spacing()
        imgui.spacing()

        subtitle = "You lost all your lives!"
        subtitle_width = imgui.calc_text_size(subtitle)[0]
        imgui.set_cursor_pos_x((window_width - subtitle_width) / 2)
        imgui.text(subtitle)

        imgui.spacing()
        imgui.separator()
        imgui.spacing()

        button_width, button_height = 460, 70
        imgui.set_cursor_pos_x((window_width - button_width) / 2)
        imgui.set_cursor_pos_y(450)

        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (20, 20))
        if imgui.button("Return to Main Menu", button_width, button_height):
            self.show_main_menu = True  
        imgui.pop_style_var()

        imgui.pop_style_var()  
        imgui.pop_style_color(6)
        imgui.end()


    def show_main_menu_screen(self, inputs):
        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(self.window.windowWidth, self.window.windowHeight)

        imgui.push_style_color(imgui.COLOR_WINDOW_BACKGROUND, 0.55, 0.92, 0.85, 1.0)  
        imgui.push_style_color(imgui.COLOR_BORDER, 0.35, 0.75, 0.65, 1.0)  
        imgui.push_style_color(imgui.COLOR_TEXT, 0.1, 0.2, 0.2, 1.0)  

        imgui.begin("Main Menu", True, imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE)
        
        logo_width, logo_height = 150, 150 
        logo_x = (self.window.windowWidth - logo_width) / 2
        logo_y = self.window.windowHeight * 0.1 

        imgui.set_cursor_pos((logo_x, logo_y))
        imgui.image(self.logo_texture, logo_width, logo_height)

        imgui.spacing()
        imgui.separator()

        imgui.set_window_font_scale(5) 
        game_title = "LOST KEYS QUEST"
        text_width, text_height = imgui.calc_text_size(game_title)

        title_x = (self.window.windowWidth - text_width) / 2
        title_y = self.window.windowHeight * 0.25
        imgui.set_cursor_pos((title_x, title_y))
        imgui.text(game_title)
        imgui.separator()

        imgui.set_window_font_scale(3.0)

        imgui.push_style_color(imgui.COLOR_BUTTON, 0.02, 0.84, 0.63, 1.0)  
        imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, 0.02, 0.76, 0.56, 1.0)
        imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, 0.01, 0.69, 0.50, 1.0)

        imgui.push_style_var(imgui.STYLE_FRAME_ROUNDING, 15.0) 

        button_width, button_height = 300, 80

        button_x = (self.window.windowWidth - button_width) / 2
        button_y_start = (self.window.windowHeight / 2) - (button_height * 1.5)

        imgui.set_cursor_pos((button_x, button_y_start))
        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (30, 20))  
        if imgui.button("New Game", button_width, button_height):
            print("New Game button clicked")
            self.start_new_game()
        imgui.pop_style_var()

        imgui.set_cursor_pos((button_x, button_y_start + button_height + 30)) 
        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (30, 20))
        if imgui.button("Load Game", button_width, button_height):
            print("Load Game button clicked")
            self.load_game()
        imgui.pop_style_var()

        imgui.pop_style_var() 
        imgui.pop_style_color(6)

        imgui.end()

    def start_new_game(self):
        self.show_main_menu = False
        self.game = Game(self.window.windowHeight, self.window.windowWidth)
        self.game.screen = 0
        self.game.InitScreen()

    def load_game(self):
        self.show_main_menu = False
        if os.path.exists(self.save_filename):
            with open(self.save_filename, "r") as f:
                data = json.load(f)
                self.game.screen = data["map"]
                self.game.lives = data["lives"]
                self.game.health = data["health"]
                self.game.total_time = data["total_time"]
            self.game.InitScreen()
        else:
            self.start_new_game()

if __name__ == "__main__":
    app = App(1000, 1000)
    app.RenderLoop()


