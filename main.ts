game.splash("Cao_Atrevido Life Simulator", "Chapter 1")
tiles.setCurrentTilemap(tilemap`level1-2`)
let speedx = 50
let speedy = 50
let Cao_Atrevido = sprites.create(img`
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
    `, SpriteKind.Player)
Cao_Atrevido.setPosition(103, 66)
info.setLife(5)
game.showLongText("Cao_Atrevido: Welcome to my city!", DialogLayout.Bottom)
game.showLongText("Cao_Atrevido: Let´s explore!", DialogLayout.Bottom)
controller.moveSprite(Cao_Atrevido, speedx, speedy)
scene.cameraFollowSprite(Cao_Atrevido)
pause(7000)
game.showLongText("Incoming Call. A to Accept.", DialogLayout.Bottom)
game.showLongText("Person: Hello? Cao_Atrevido? We have a problem. Come here right now!", DialogLayout.Bottom)
game.showLongText("Cao_Atrevido: Ok. I go.", DialogLayout.Bottom)
game.showLongText("---CALL ENDED---", DialogLayout.Bottom)
game.showLongText("Cao_Atrevido: Fast! We need to go fast to my home!", DialogLayout.Bottom)
speedx = 100
speedy = 100
Cao_Atrevido.setVelocity(speedx, speedy)
