from settings import *
from pytmx.util_pygame import load_pygame #carrega os mapas
from os.path import join
from sprites import Sprite, AnimatedSprite, CollisionSprite, CollidableSprite, TransitionSprite, DialogSprite, InteractiveSprite
from entities import Player, Character
from inventory import Inventory
from computer import Computer
from battle import Battle
from item import Item
from link import Link
from groups import AllSprites
from support import *
from game_data import *
from dialog import Dialog
from time import sleep

class Game:
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Amaes Game')
        self.clock = pygame.time.Clock()
        
        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites   = pygame.sprite.Group()
        self.character_sprites   = pygame.sprite.Group()
        self.transition_sprites  = pygame.sprite.Group()
        self.dialogs_sprites     = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()

        # transition
        self.transition_area = None
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_mode = 'untint'
        self.tint_progress = 0
        self.tint_direction = 1
        self.tint_speed = 600
        
        self.import_assets()
        self.setup(self.tmx_maps['sala_vitor'], 'ct7')
        
        # Computer
        self.computer_links = []

        def add_link(self, item):
            self.computer_links.append(item)

        def create_computer(self):
            for i in COMPUTER_DATA:
                add_link(self,Link(i))

        create_computer(self)

        self.player_items = []
        self.create_inventory()
        # overlays
        self.dialog_tree = None
        self.inventory = Inventory(self.player_items , self.fonts, self.interface_frames, self.player)
        self.inventory_open = False
        self.computer = Computer(self.computer_links,self.fonts, self.interface_frames)
        self.computer_open = False
        self.battle_open = False
        self.add_item(Item('0'))
        self.add_item(Item('1'))
        self.add_item(Item('2'))
        self.add_item(Item('4'))

        # Inventory
    def create_inventory(self):
        inventory_size = 30
        for _ in range(inventory_size):
            self.player_items.append({})

    def add_item(self, item):
        for index, item_ in enumerate(self.player_items):
            if (item_ == {}):
                self.player_items[index] = item
                break
            else:
                pass

    # carrega todos os assets do jogo
    def import_assets(self):
        self.tmx_maps = import_all_maps('.', 'data', 'maps')

        self.overworld_frames = {
            'characters': all_characters_import('.', 'graphics', 'characters'),
            'water': import_folder('.', 'graphics', 'tilesets', 'water'),
            'lake': lake_importer(3, 12, '.', 'graphics', 'tilesets', 'lake'),
        }
        self.fonts = {
            'dialog': pygame.font.Font(join('.', 'graphics', 'fonts', 'PixeloidSans.ttf'), 30),
            'bold': pygame.font.Font(join('.', 'graphics', 'fonts', 'dogicapixelbold.otf'), 20),
            'regular': pygame.font.Font(join('.', 'graphics', 'fonts', 'PixeloidSans.ttf'), 18),
        }
        self.interface_frames = {
            'interface': import_folder_dict('.', 'graphics', 'interface'),
            'items': import_folder_dict('.', 'graphics', 'items'),
        }

    # carrega o mapa a ordem é importante pois vai sobrepor os objetos
    def setup(self,tmx_map, player_start_pos = 'house'):
        # clean sprites
        for group in (self.all_sprites, self.collision_sprites, self.character_sprites, self.transition_sprites):
            group.empty()
        # terrain 
        try:
            for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, GAME_LAYERS['bg'])
        except ValueError as ve:
            print(ve)
            # manter os items do jogador aqui

		# water 
        try:
            for obj in tmx_map.get_layer_by_name('Lake'):
                for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                    for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                        AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites, GAME_LAYERS['water'])
        except ValueError as ve:
            print(ve)

        # lake edges
        try:
            if tmx_map.get_layer_by_name('Lake Edges'):
                for obj in tmx_map.get_layer_by_name('Lake Edges'):
                    side = obj.properties['side']
                    AnimatedSprite((obj.x, obj.y), self.overworld_frames['lake'][side], self.all_sprites, GAME_LAYERS['bg'])
        except ValueError as ve:
            print(ve)

        # objects
        try:
            for obj in tmx_map.get_layer_by_name('Objects'):
                if obj.name == 'passarela_ufes_top':
                    Sprite((obj.x, obj.y), obj.image, self.all_sprites, GAME_LAYERS['top'])
                else:
                    # print(obj)
                    CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
        except ValueError as ve:
            print(ve)
        # objects
        try:
            for obj in tmx_map.get_layer_by_name('Interactive Objects'):
                print(obj.properties['item_id'])
                InteractiveSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.interaction_sprites), obj.properties['item_id'], GAME_LAYERS['top'])
        except ValueError as ve:
            print(ve)

        # collision
        try:
            for obj in tmx_map.get_layer_by_name('Collisions'):
                # print(obj)
                CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), (self.collision_sprites))
                # print (type((obj.width, obj.height)))
        except ValueError as ve:
            print(ve)

        # dialogs
        
        if (not tmx_map in VISITED_MAPS):
            VISITED_MAPS.append(tmx_map)
            try:
                for obj in tmx_map.get_layer_by_name('Dialogs'):
                    DialogSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), (self.dialogs_sprites), obj.properties['message'])
                    # print (type((obj.width, obj.height)))
            except ValueError as ve:
                print(ve)

        # transitions
        try:
            for obj in tmx_map.get_layer_by_name('Transitions'):
                # print(obj.x, obj.y, obj.properties['dest'], obj.properties['src'])
                TransitionSprite((obj.x, obj.y), obj.properties['dest'], obj.properties['src'], self.transition_sprites, (obj.width, obj.height))
        except ValueError as ve:
            print(ve)

        # entities
        try:
            for obj in tmx_map.get_layer_by_name('Entities'):
                if obj.name == 'Player':
                    # print(obj.x, obj.y) # pos do player
                    if obj.properties['pos'] == player_start_pos:
                        self.player = Player(
                            pos = (obj.x, obj.y),
                            groups = self.all_sprites,
                            frames = self.overworld_frames['characters']['player1'],
                            facing_direction = obj.properties['direction'],
                            collision_sprites = self.collision_sprites,
                            character_data = CHARACTERS_DATA[obj.properties['character_id']],
                        )
                else:
                    Character(
                        pos = (obj.x, obj.y), 
                        groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                        frames = self.overworld_frames['characters'][obj.properties['graphic']], 
                        facing_direction = obj.properties['direction'],
                        collision_sprites = self.collision_sprites,
                        character_data = CHARACTERS_DATA[obj.properties['character_id']],
                    )
        except ValueError as ve:
            print(ve)

    # verifica o input do jogador
    def input(self):
        if not self.dialog_tree: # and not self.battle:
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_SPACE] and not self.dialog_tree:
                for character in self.character_sprites:
                    if check_connections(100, self.player, character):
                        # for i in character.character_data['questions']:
                        #     print (i)
                        #     for value in character.character_data['questions'][i].values():
                        #         print (value)


                            # print(question)
                            # for a, b in question.items():1
                        #     print(a, b)
                            # print(question['title'], question['description'], question['options'])

                        character.change_facing_direction(self.player.rect.center)
                        self.create_dialog(character)
                for sprite in self.interaction_sprites:
                    if check_interaction(150, self.player, sprite):
                        if sprite.item_id == 'computer':
                            self.computer_open = not self.computer_open
                            self.player.blocked = not self.player.blocked
                            # emitir som
                        if sprite.item_id == 'coffe':
                            self.add_item(Item('4'))
                            sprite.kill()
                            # emitir som
            if keys[pygame.K_i]:
                self.inventory_open = not self.inventory_open
                self.player.blocked = not self.player.blocked
                # emitir som
            if keys[pygame.K_ESCAPE]:
                self.inventory_open = False
                self.computer_open = False
                self.player.blocked = False
                self.battle_open = False

    def create_dialog(self, character, message = None):
        if not self.dialog_tree:
            self.player.block()
            self.dialog_tree = Dialog(character, self.player, self.all_sprites, self.fonts['dialog'], self.end_dialog, message)

    def end_dialog(self,character):
        if (check_questions(character)):
            self.battle = Battle(self.player, character, self.interface_frames, self.fonts)
            self.battle_open = True
        # self.dialog_tree = Dialog(self.player, self.player, self.all_sprites, self.fonts['dialog'], self.end_dialog)
        # pause game
        # index com a escolha da resposta
        if True:
            self.dialog_tree = None
            self.player.unblock()
            character.character_data['visited'] = True

    def check_transitions(self):
        transition_rect = [sprite for sprite in self.transition_sprites if sprite.rect.colliderect(self.player.hitbox)]
        if transition_rect:
            self.player.block()
            self.transition_area = transition_rect
            self.tint_mode = 'tint'

    def check_dialog(self):
        for sprite in self.dialogs_sprites:
            if sprite.hitbox.colliderect(self.player.hitbox):
                self.create_dialog(self.player, sprite.message)
                sprite.kill()

    def tint(self, dt):
        if self.tint_mode == 'untint':
            self.tint_progress -= self.tint_speed * dt
        if self.tint_mode == 'tint':
            self.tint_progress += self.tint_speed * dt    
            if self.tint_progress >= 255: 
                self.setup(self.tmx_maps[self.transition_area[0].dest], self.transition_area[0].src)
                self.tint_mode = 'untint'
                self.transition_area = None

        self.tint_progress = max(0, min(self.tint_progress, 255))
        self.tint_surf.set_alpha(self.tint_progress)
        self.screen.blit(self.tint_surf, (0,0))

    def run(self):
        # event loop
        while True:
            self.screen.fill(COLORS['black'])
            dt = self.clock.tick() / 1000 # correção de movimento para todos os pcs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.input()
            self.check_transitions()
            self.check_dialog()
            self.all_sprites.update(dt)

            # drawing
            self.all_sprites.draw(self.player)

            # overlays
            if self.dialog_tree: self.dialog_tree.update()
            if self.inventory_open: self.inventory.update(dt)
            if self.computer_open: self.computer.update(dt)
            if self.battle_open: self.battle.update(dt)
            self.tint(dt)
            pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()