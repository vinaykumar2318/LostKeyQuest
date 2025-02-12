import imgui
import numpy as np
from utils.graphics import Object, Camera, Shader
from assets.shaders.shaders import object_shader
from assets.objects.objects import backgroundProps, CreateCircle, playerProps, homepageProps, newGameButtonProps, loadGameButtonProps


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = -1
        self.camera = Camera(height, width)
        self.shaders = [Shader(object_shader['vertex_shader'], object_shader['fragment_shader'])]
        self.objects = []
        self.maps = [self.createmap0, self.createmap1, self.createmap2, self.createmap3]
        self.currentmap = 0

    def createmap0(self):
        background = Object(self.shaders[0], homepageProps)
        new_game_button = Object(self.shaders[0], newGameButtonProps)
        load_game_button = Object(self.shaders[0], loadGameButtonProps)
        obj = [background, new_game_button, load_game_button]
        return obj


    def createmap1(self):
        background = Object(self.shaders[0], backgroundProps)
        start_x = -self.width/2 + 50
        start_y = 0
        player = Object(self.shaders[0], playerProps)
        player.properties['is_player'] = True
        player.properties['speed'] = 150.0
        player.properties['position'] = [start_x, start_y, 1.0]

        circles = []
        num_circles = 5  # Number of circles
        x_positions = [2, -1, 6, -5, -3]
        speed = [100, 150, 80, 180, 170]
        end_x = 2  # Rightmost position
        y_positions = [6, 3, 0, -3, -6]  # Vertical positions of circles
        radius = 1.4  # Radius of circles
        color = [1.0, 1.0, 1.0, 1.0]  # Red color

        for i in range(num_circles):
            center = [x_positions[i], y_positions[i], 0.5] 
            vertices, indices = CreateCircle(center, radius, color)

            vertices = np.array(vertices, dtype=np.float32)
            indices = np.array(indices, dtype=np.uint32)
            circle = Object(self.shaders[0], {"vertices": vertices, "indices": indices})
            circle.properties['position'] = [x_positions[i], y_positions[i], 0.5]   # Start at left edge
            circle.properties['speed'] = speed[i]  # Set movement speed
            circle.properties['direction'] = [1, 0]  # Move right
            circle.properties['rotation_z'] = 0.0
            circle.properties['scale'] = np.array([30, 30, 1], dtype = np.float32)
            circle.properties['identity'] = i
            circles.append(circle)
        
        obj = [background, player] + circles
        return obj

    def createmap2(self):
        # Implement the second map here
        pass

    def createmap3(self):
        # Implement the third map here
        pass

    def InitScreen(self):
        if self.screen == -1:
            self.objects = self.maps[self.currentmap]()
            # print("Initialized maps", self.objects)
        elif self.screen == 0:
            self.objects = self.maps[self.currentmap]()
            # print("Initialized maps", self.objects)  
        elif self.screen == 1:
            pass
        elif self.screen == 2:
            pass

    def ProcessFrame(self, inputs, time):
        if self.screen == -1:
            self.InitScreen()
            self.DrawText()
            self.screen = 0
        elif self.screen == 0:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
        elif self.screen == 1:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
        elif self.screen == 2:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
    
    def DrawText(self):
        if (self.screen == -1 or self.screen==0) and self.currentmap==0:
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(self.width, self.height)
            imgui.begin(
                "Text Overlay", 
                flags=imgui.WINDOW_NO_TITLE_BAR | 
                    imgui.WINDOW_NO_RESIZE | 
                    imgui.WINDOW_NO_MOVE | 
                    imgui.WINDOW_NO_BACKGROUND
            )

            imgui.set_window_font_scale(4) 

            game_title = "LOST KEYS QUEST"

            text_width = imgui.calc_text_size(game_title)[0]
            center_x = (self.width - text_width) / 2

            imgui.set_cursor_pos((center_x, 20))  
            imgui.text(game_title)
            imgui.separator()

            imgui.set_window_font_scale(2.0)
            background, new_game_button, load_game_button = self.objects
            
            new_game_button_pos = new_game_button.properties['position']
            new_game_button_size = new_game_button.properties['size']
            
            load_game_button_pos = load_game_button.properties['position']
            load_game_button_size = load_game_button.properties['size']
            
            # Pushing colors
            imgui.push_style_color(imgui.COLOR_BUTTON, 0.02, 0.84, 0.63, 1.0)
            imgui.push_style_color(imgui.COLOR_BUTTON_HOVERED, 0.02, 0.76, 0.56, 1.0)
            imgui.push_style_color(imgui.COLOR_BUTTON_ACTIVE, 0.01, 0.69, 0.50, 1.0)

            try:
                # New Game Button
                imgui.set_cursor_pos((
                    self.width // 2 + new_game_button_pos[0] - 100,
                    self.height // 2 - new_game_button_pos[1] - 25
                ))
                imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (20, 20))
                if imgui.button("New Game", width=200, height=50):
                    print("New Game button clicked")
                    self.currentmap = 1
                    self.screen = 0
                    self.InitScreen()
                imgui.pop_style_var()

                # Load Game Button
                imgui.set_cursor_pos((
                    self.width // 2 + load_game_button_pos[0] - 100,
                    self.height // 2 - load_game_button_pos[1] - 25
                ))
                imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (20, 20))
                if imgui.button("Load Game", width=200, height=50):
                    print("Load Game button clicked")
                imgui.pop_style_var()
                
            finally:
                # Ensure styles are always popped to avoid ImGui error
                imgui.pop_style_color(3)  

            imgui.end()
        elif self.screen == 0:
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(self.width, self.height)
            imgui.begin(
                "Text Overlay", 
                flags=imgui.WINDOW_NO_TITLE_BAR | 
                    imgui.WINDOW_NO_RESIZE | 
                    imgui.WINDOW_NO_MOVE | 
                    imgui.WINDOW_NO_BACKGROUND
            )

            imgui.set_window_font_scale(4) 

            game_title = "LEVEL 1"

            text_width = imgui.calc_text_size(game_title)[0]
            center_x = (self.width - text_width) / 2

            imgui.set_cursor_pos((center_x, 20))  
            imgui.text(game_title)
            imgui.separator()
            imgui.end()
        elif self.screen == 1:
            pass
        elif self.screen == 2:
            pass

    def UpdateScene(self, inputs, time):
        player = None
        for obj in self.objects:
            if obj.properties.get('is_player', False):
                player = obj
                break

        if player:
            speed = player.properties.get('speed', 5.0) 
            position = player.properties['position']

            if "W" in inputs: 
                player.properties['position'][1] += speed * time['deltaTime']
            if "S" in inputs: 
                player.properties['position'][1] -= speed * time['deltaTime']
            if "A" in inputs: 
                player.properties['position'][0] -= speed * time['deltaTime']
            if "D" in inputs: 
                player.properties['position'][0] += speed * time['deltaTime']

            half_width = self.width/2
            half_height = self.height/2
            player_size = 25
            position[0] = max(-half_width + player_size, min(half_width - player_size, position[0]))
            position[1] = max(-half_height + player_size, min(half_height - player_size, position[1]))

        for obj in self.objects:
            if 'speed' in obj.properties and not obj.properties.get('is_player', False):
                obj.properties['position'][0] += obj.properties['speed'] * time['deltaTime'] * obj.properties['direction'][0]

                if (obj.properties['position'][0] + 490 >= self.width / 2 or obj.properties['position'][0] - 80 <= -self.width / 2) and obj.properties['identity']==0:
                    obj.properties['direction'][0] *= -1  # Reverse direction
                elif (obj.properties['position'][0] + 300 >= self.width / 2 or obj.properties['position'][0] - 300 <= -self.width / 2) and obj.properties['identity']==1:
                    obj.properties['direction'][0] *= -1  # Reverse direction
                elif (obj.properties['position'][0] + 380 >= self.width / 2 or obj.properties['position'][0] - 300 <= -self.width / 2) and obj.properties['identity']==2:
                    obj.properties['direction'][0] *= -1  # Reverse direction
                elif (obj.properties['position'][0] + 288 >= self.width / 2 or obj.properties['position'][0] - 400 <= -self.width / 2) and obj.properties['identity']==3:
                    obj.properties['direction'][0] *= -1  # Reverse direction
                elif (obj.properties['position'][0] + 53 >= self.width / 2 or obj.properties['position'][0] - 400 <= -self.width / 2) and obj.properties['identity']==4:
                    obj.properties['direction'][0] *= -1  # Reverse direction


        if self.screen == 0:
            pass
        if self.screen == 1:
          pass

            
    def DrawScene(self):
        if self.screen==0 or self.screen == 1:
            for shader in self.shaders:
                self.camera.Update(shader)

            for obj in self.objects:
                obj.Draw()

