game.splash("Cao_Atrevido Life Simulator", "Chapter 1")
tiles.set_current_tilemap(tilemap("""
    level1-2
"""))
speedx = 50
speedy = 50
Cao_Atrevido = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
Cao_Atrevido.set_position(103, 66)
info.set_life(5)
game.show_long_text("Cao_Atrevido: Welcome to my city!", DialogLayout.BOTTOM)
game.show_long_text("Cao_Atrevido: Let´s explore!", DialogLayout.BOTTOM)
controller.move_sprite(Cao_Atrevido, speedx, speedy)
scene.camera_follow_sprite(Cao_Atrevido)
pause(7000)
game.show_long_text("Incoming Call. A to Accept.", DialogLayout.BOTTOM)
game.show_long_text("Person: Hello? Cao_Atrevido? We have a problem. Come here right now!",
    DialogLayout.BOTTOM)
game.show_long_text("Cao_Atrevido: Ok. I go.", DialogLayout.BOTTOM)
game.show_long_text("---CALL ENDED---", DialogLayout.BOTTOM)
game.show_long_text("Cao_Atrevido: Fast! We need to go fast to my home!",
    DialogLayout.BOTTOM)
speedx = 100
speedy = 100
Cao_Atrevido.set_velocity(speedx, speedy)