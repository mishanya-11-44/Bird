from tkinter import*
from time import time
def paint_frame():
    canvas.itemconfig(sprite_id,image=get_current_frame())
    canvas.coords(sprite_id,x,y)
def next_frame():
    global frame_current_index
    frame_current_index+=1
    if frame_current_index>=len(frames):
        frame_current_index=0
def update():
    global last_time
    current_time=time()
    update_time=current_time-last_time
    update_motion_anim(update_time)
    update_frame_anim(update_time)
    paint_frame()
    last_time=current_time
    window.after(1,update)
def update_motion_anim(update_time):
    global x,y,speed
    coords=canvas.coords(sprite_id)
    x_left = coords[0]
    y_top = coords[1]
    if x_left + 115 > world_width:
        speed=0
    elif y_top + 100 > world_height - 10:
        speed=0
    elif x_left < 0:
        speed=0
    elif y_top < 0:
        speed=0
    else:
        delta_x = (vx * speed) * update_time
        delta_y = (vy * speed) * update_time
        x+=delta_x
        y+=delta_y
def update_frame_anim(update_time):
    global frame_time_elapsed
    frame_time_elapsed+=update_time
    if frame_time_elapsed>=frame_time:
        frame_time_elapsed=0
        next_frame()
def get_current_frame():
    return frames[frame_current_index]
def add_frame(frame_file_name):
    image=PhotoImage(file=frame_file_name)
    frames.append(image)
def load_frames():
    global frame_current_index
    first_number=1
    last_number=14
    for i in range(first_number,last_number+1):
        add_frame(f'./textures/player{i}.png')
    frame_current_index=0
def left():
    global vx,vy
    vx=-1
    vy=0
def right():
    global vx, vy
    vx = 1
    vy = 0
def up():
    global vx, vy
    vx = 0
    vy = -1
def down():
    global vx, vy
    vx = 0
    vy = 1
def key_press(event):
    key_w=87
    key_s = 83
    key_a = 65
    key_d = 68
    if event.keycode==key_w:
        up()
    if event.keycode==key_s:
        down()
    if event.keycode==key_a:
        left()
    if event.keycode==key_d:
        right()
x=0
y=0
vx=1
vy=0
speed=50
frames=[]
frame_current_index=-1
frame_time=0.1
frame_time_elapsed=0
last_time=time()
world_width=400
world_height=300
window=Tk()
load_frames()
window.title('Анимация')
canvas=Canvas(window,width=world_width,height=world_height)
sprite_id=canvas.create_image(x,y,image=get_current_frame(),anchor=NW)
update()
canvas.pack()
window.bind('<Key>',key_press)
window.mainloop()