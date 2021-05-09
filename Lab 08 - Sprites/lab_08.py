import random
import arcade

SPRITE_SCALING_COIN = 0.5
SPRITE_SCALING_PLAYER = 0.5
COIN_COUNT = 50

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
PLAYER_MOVEMENT_SPEED = 15

class Coin(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                        SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("player_stand.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):

            coin = Coin("coinGold.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
    
    def update(self, delta_time):

        self.coin_list.update()
        self.player_sprite.update()

        if self.player_sprite.center_x < SPRITE_SCALING_PLAYER:
            self.player_sprite.center_x = SPRITE_SCALING_PLAYER

        if self.player_sprite.center_x > SCREEN_WIDTH - SPRITE_SCALING_PLAYER:
            self.player_sprite.center_x = SCREEN_WIDTH - SPRITE_SCALING_PLAYER

        if self.player_sprite.center_y < SPRITE_SCALING_PLAYER:
            self.player_sprite.center_y = SPRITE_SCALING_PLAYER

        if self.player_sprite.center_y > SCREEN_HEIGHT - SPRITE_SCALING_PLAYER:
            self.player_sprite.center_y = SCREEN_HEIGHT - SPRITE_SCALING_PLAYER

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.coin_list)

        for coin in coins_hit_list:
            coin.reset_pos()
            self.score += 1

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, symbol, modifiers):
        
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif symbol == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif symbol == arcade.key.UP:
            self.player_sprite.change_y = 0


def main():
    Window = MyGame()
    Window.setup()
    arcade.run()

if __name__ == "__main__":
    main()