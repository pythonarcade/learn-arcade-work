import random
import arcade
import Constants

# Boilerplate code came from https://api.arcade.academy/en/latest/examples/slime_invaders.html
# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
rightEnemyBorder = Constants.screenWidth - Constants.enemyVerticalMargin
leftEnemyBorder = Constants.enemyVerticalMargin


# title screen
class TitleView(arcade.View):

    def on_show_view(self):
        # runs once we switch to this view
        arcade.set_background_color((27, 27, 27))
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        # clear out anything else like old views
        self.clear()

        # Draw the view
        arcade.draw_text("This is Definitely Not Space Invaders....", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to Continue", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    # go to next screen through mouse click
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # show instructions next
        self.window.show_view(InstructionView())


# instruction view that's called from title view
class InstructionView(arcade.View):

    # runs once we switch to this view
    def on_show_view(self):
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        # clear out anything else like old views
        self.clear()
        # Draw the view
        instructionPage = arcade.load_texture("InstructionPage.png")
        arcade.draw_lrwh_rectangle_textured(0, 0, Constants.screenWidth, Constants.screenHeight, instructionPage)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


# Game view
class GameView(arcade.View):

    def __init__(self):
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None

        # level variable
        self.level = 1

        # life variable
        self.lives = 5

        # Textures for the enemy
        self.enemy_textures = None

        # State of the game
        self.game_state = Constants.playGame

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Enemy movement
        self.enemy_change_x = - Constants.enemySpeed

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Load sounds. Sounds from arcade
        self.gun_sound = arcade.load_sound(":resources:sounds/laser1.ogg")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit3.wav")
        self.player_hit = arcade.load_sound(":resources:sounds/hurt1.wav")
        self.lost_game = arcade.load_sound(":resources:sounds/lose2.wav")
        self.level_up = arcade.load_sound(":resources:sounds/upgrade4.wav")

    def setup_levels(self):
        # Load the textures for the enemies, coming to you from Kenney.nl
        # enemy image from kenney.nl https://kenney.nl/assets/space-shooter-extension
        texture1 = arcade.load_texture("spaceShips_001.png")
        texture2 = arcade.load_texture("spaceShips_002.png")
        texture3 = arcade.load_texture("spaceShips_003.png")
        texture4 = arcade.load_texture("spaceShips_004.png")
        texture5 = arcade.load_texture("spaceShips_005.png")
        self.enemy_textures = [texture1, texture2, texture3, texture4, texture5]

        # Create rows and columns of enemies
        x_count = 6
        x_start = 380
        x_spacing = 60
        y_count = 4
        y_start = 420
        y_spacing = 40

        # randomize the enemy ships
        randomEnemy = random.randint(0, 4)

        for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing * y_count + y_start, y_spacing):
                # Create the enemy instance
                enemy = arcade.Sprite()
                enemy.scale = Constants.enemyScaling
                enemy.texture = self.enemy_textures[randomEnemy]

                # Position the enemy
                enemy.center_x = x
                enemy.center_y = y

                # Add the enemy to the lists
                self.enemy_list.append(enemy)

    def make_shield(self, x_start):
        # shield function
        # just a bunch of little sprites stuck together
        shield_block_width = 5
        shield_block_height = 10
        shield_width_count = 20
        shield_height_count = 5
        y_start = 150
        for x in range(x_start,
                       x_start + shield_width_count * shield_block_width,
                       shield_block_width):
            for y in range(y_start,
                           y_start + shield_height_count * shield_block_height,
                           shield_block_height):
                shield_sprite = arcade.SpriteSolidColor(shield_block_width,
                                                        shield_block_height,
                                                        arcade.color.RED)
                shield_sprite.center_x = x
                shield_sprite.center_y = y
                self.shield_list.append(shield_sprite)

    def setup(self):
        # Initial setup of the game and when we restart the game
        self.game_state = Constants.playGame

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)

        # Set up the player
        self.score = 0

        # Image from kenney.nl https://kenney.nl/assets/space-shooter-extension
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png",
                                           Constants.playerScaling)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Make each of the shields initially
        for x in range(75, 800, 190):
            self.make_shield(x)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # setup the initial level
        self.setup_levels()

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()

        # Render the score
        arcade.draw_text(f"Score: {self.score}", 5, 540, arcade.color.WHITE, 14)

        # Render the players lives
        arcade.draw_text(f"lives: {self.lives}", 5, 560, arcade.color.WHITE, 14)

        # Render the level
        arcade.draw_text(f"Level: {self.level}", 5, 580, arcade.color.WHITE, 14)

        # Draw game over
        if self.game_state == Constants.gameOver:
            self.clear()
            arcade.set_background_color(arcade.csscolor.BLACK)
            arcade.draw_text("GAME OVER", 175, 325, arcade.color.WHITE, 55)
            arcade.draw_text("Click to Restart", 300, 275, arcade.color.WHITE, 24)
            self.set_mouse_visible(True)

    def on_mouse_motion(self, x, y, dx, dy):
        # Don't move the player if the game is over
        if self.game_state == Constants.gameOver:
            return

        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        # Only allow the user so many bullets on screen at a time
        if len(self.player_bullet_list) < Constants.maxPlayerBullets + (self.level * 0.4):
            # Gun sound
            arcade.play_sound(self.gun_sound)

            # Create a bullet
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", Constants.laserScaling)

            # Rotate image
            bullet.angle = 90

            # Give the bullet a speed
            bullet.change_y = Constants.playerBulletSpeed + (self.level * 0.1)

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.player_bullet_list.append(bullet)

        # if game is over restart game with click
        if self.game_state == Constants.gameOver:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    def update_enemies(self):

        # Move the enemy vertically
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > rightEnemyBorder and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < leftEnemyBorder and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # if we hit the edge then we move down
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= Constants.enemyMoveDownAmount

    def allow_enemies_to_fire(self):
        # Track which x values have had a chance to fire a bullet.
        # Since enemy list is build from the bottom up, we can use
        # this to only allow the bottom row to fire.
        x_spawn = []
        for enemy in self.enemy_list:
            # Adjust the chance depending on the number of enemies. Fewer
            # enemies, more likely to fire.
            chance = 4 + len(self.enemy_list) * 4

            # Fire if we roll a zero, and no one else in this column has had
            # a chance to fire.
            if random.randrange(chance) == 0 and enemy.center_x not in x_spawn:
                # Create a bullet
                bullet = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", Constants.laserScaling)

                # Angle down.
                bullet.angle = 180

                # Give the bullet a speed
                bullet.change_y = -Constants.enemyBulletSpeed - (self.level * 0.3)

                # Position the bullet so its top id right below the enemy
                bullet.center_x = enemy.center_x
                bullet.top = enemy.bottom

                # Add the bullet to the appropriate list
                self.enemy_bullet_list.append(bullet)

            # Ok, this column has had a chance to fire. Add to list so we don't
            # try it again this frame.
            x_spawn.append(enemy.center_x)

    def process_enemy_bullets(self):

        # Move the bullets
        self.enemy_bullet_list.update()

        # Loop through each bullet
        for bullet in self.enemy_bullet_list:
            # Check this bullet to see if it hit a shield
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)

            # If it did, get rid of the bullet and shield blocks
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            # See if the player got hit with a bullet
            playerHitList = arcade.check_for_collision_with_list(bullet, self.player_list)

            # if so remove a life
            if len(playerHitList) > 0:
                bullet.remove_from_sprite_lists()
                arcade.play_sound(self.player_hit)
                self.lives -= 1

                # if lives reach zero end game
                if self.lives == 0:
                    arcade.play_sound(self.lost_game)
                    self.game_state = Constants.gameOver

            # If the bullet falls off the screen get rid of it
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def processEnemyHittingObjects(self):
        # Loop through each enemy
        for enemy in self.enemy_list:
            # Check this enemy to see if it hit a shield
            shieldHitList = arcade.check_for_collision_with_list(enemy, self.shield_list)

            # If it did, get rid of the shield blocks
            if len(shieldHitList) > 0:
                for shield in shieldHitList:
                    shield.remove_from_sprite_lists()
                continue

            # See if the player got hit with an enemy
            playerHitList = arcade.check_for_collision_with_list(enemy, self.player_list)

            # if they collide with player
            if len(playerHitList) > 0:
                enemy.remove_from_sprite_lists()
                arcade.play_sound(self.player_hit)
                self.lives -= 1

                if self.lives == 0:
                    arcade.play_sound(self.lost_game)
                    self.game_state = Constants.gameOver

    def process_player_bullets(self):

        # Move the bullets
        self.player_bullet_list.update()

        # Loop through each bullet
        for bullet in self.player_bullet_list:

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 10

                # Hit Sound
                arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > Constants.screenHeight:
                bullet.remove_from_sprite_lists()

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.game_state == Constants.gameOver:
            return

        self.update_enemies()
        self.allow_enemies_to_fire()
        self.process_enemy_bullets()
        self.process_player_bullets()
        self.processEnemyHittingObjects()

        if len(self.enemy_list) == 0:
            # increase level
            self.level += 1

            # play level up sound
            arcade.play_sound(self.level_up)

            # clear lasers
            self.player_bullet_list = arcade.SpriteList()
            self.enemy_bullet_list = arcade.SpriteList()

            # Remake shields
            for x in range(75, 800, 190):
                self.make_shield(x)

            self.setup_levels()

    def set_mouse_visible(self, param):
        pass


# what is initially called to start the game
def main():
    window = arcade.Window(Constants.screenWidth, Constants.screenHeight, Constants.title)
    window.show_view(TitleView())
    arcade.run()


# make sure main is called and not something else
if __name__ == "__main__":
    main()
