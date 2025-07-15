# Pac-Man in Pygame
## Functions outside of the main loop
### draw_board()
1. define tile numbers for height:num1 and width:num2 [(H-50) // 32, W // 30]
2. two for loops running through the board variable
```
for i in range(len(level)):
  for j ...
    if level[i][j] == NUMBER:
      pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5*num1)), 4)
    if... 2: same as 1 but radius is 10
    if... 3: pygame.draw.line(screen, color, (j * num2 + (0.5*num2), i * num1), (j * num2 + (0.5*num2), i * num1 + num1))
    if... 4: ...line(screen, color, (j * num2, i*num1 + 0.5 *num1)), (j * num2 + num2, i*num1 + (0.5 *num1)), 3)

```
### draw_player()
1. define *player_images*: each element has pygame.image.load(), scale for (45, 45) with pygame.transform.scale
2. define player_x and player_y: 450, 663, define direction(= 0), define counter variable
3. if direction == 0~3: pygame.transform.flip and .rotate for flipping and rotation


## Setting up Pygame
- Import and initialize Pygame
- define the W, H, screen, timer, frame per sec, font, color, player_images = [], counter, and **board**
- Make a game loop:
 - timer.tick(fps)
 - screen.fill
 - Define the **draw_board()** func
 - make a pygame.event.get() *for loop*
  - change direction var with the arrow keys
 - if counter < 19: counter += 1, else counter = 0
