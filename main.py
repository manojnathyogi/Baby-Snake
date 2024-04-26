from graphics import Canvas
import time
import random

    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

#make this larger, the game will go slower
DELAY = 0.15

def main():
    
    # TODO: setup the world
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    score = 0  # Initialize score
    score_text = canvas.create_text(10, 10, text=f'Score: {score}', font='Arial', font_size=20, color='black')
    DELAY = 0.15
    # TODO:
    player = canvas.create_rectangle(0,0,SIZE,SIZE)
    canvas.set_color(player, "blue")
    
    #goal
    width_str = random.randint(0, (CANVAS_WIDTH-20)//20) * 20
    height_str = random.randint(0, (CANVAS_HEIGHT-20)//20) * 20
    goal = canvas.create_rectangle(width_str, height_str, width_str+SIZE,height_str+SIZE)
    canvas.set_color(goal, "salmon")
    w = 20 
    h = 0
    
    while True:
        left_x_player = canvas.get_left_x(player)
        top_y_player = canvas.get_top_y(player)
        
        if left_x_player == 400 or top_y_player == 400 or left_x_player ==-20 or top_y_player==-20:
            #canvas.moveto(player, 0, 0)
            print("Game Over")
            break
        else:
            canvas.move(player, w, h)
            key = canvas.get_last_key_press()
            if key == 'ArrowLeft':
                #print('left arrow pressed!')
                w = -20
                h = 0
            if key == 'ArrowRight':
                #print('right arrow pressed!')
                w = 20
                h = 0
            if key == 'ArrowUp':
                #print('up arrow pressed!')
                h = -20
                w = 0
            if key == 'ArrowDown':
                #print('down arrow pressed!')
                h = 20
                w = 0
        
        overlay = canvas.find_overlapping(width_str, height_str, width_str+SIZE,height_str+SIZE)
        if overlay[0]==player:
            canvas.delete(goal)
            score += 10
            canvas.change_text(score_text, f'Score: {score}')
            width_str = random.randint(0, (CANVAS_WIDTH-20)//20) * 20
            height_str = random.randint(0, (CANVAS_HEIGHT-20)//20) * 20
            goal = canvas.create_rectangle(width_str, height_str, width_str+SIZE,height_str+SIZE)
            canvas.set_color(goal, "salmon")
            if DELAY == 0.02:
                DELAY = 0.02
            else:
                DELAY -= 0.01
            #print(DELAY)
        time.sleep(DELAY)
        
    
if __name__ == '__main__':
    main()