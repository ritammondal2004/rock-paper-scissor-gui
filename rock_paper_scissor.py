# Rock Paper Scissor Game using Tkinter and Pygame for sound effects             
                        
from tkinter import Tk, Canvas, Label, Button, Frame, Toplevel
from PIL import ImageTk, Image 
import random, pygame, time
from functools import partial  
import threading 

# main window object
root = Tk() 

# Title of window
root.title('Rock Paper Scissor')

# Size of window
root.geometry('1000x680')  
root.configure(bg="white")   
                                 
#Create Two Frames
start_frame = Frame(root, width=1000, height=680)
start_frame.grid(row=0, column=0, sticky="news")

bg_img = Image.open("images/start_img.png").resize((1000, 680))
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = Label(start_frame, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


game_frame = Frame(root, width=1000, height=680, bg='white')

canvas = Canvas(game_frame, width=1000, height=680, bg='white')
canvas.grid(row=0, column=0)
canvas.configure(bg="white") 

# ------------ Initialize pygame mixer for sound effects-------------- 
pygame.mixer.init()  
def play_sound(path, vol = 1):
    def inner():
        pygame.mixer.music.load(path) 
        pygame.mixer.music.set_volume(vol)  # Volume 0.0 to 1.0
        pygame.mixer.music.play()  #(loops: int = 0, start: float = 0, fade_ms: int = 0) -> None
    threading.Thread(target=inner, daemon=True).start()


def loop_sound(path, loop_count=-1,vol=0.5):
    def inner():
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play(loop_count)
    threading.Thread(target=inner, daemon=True).start() 


def play_clip(path, start_sec, end_sec, vol=0.9):
    def inner():
        pygame.mixer.music.load(path) 
        pygame.mixer.music.play(start=start_sec) 
        pygame.mixer.music.set_volume(vol)  
        time.sleep(end_sec - start_sec)
        pygame.mixer.music.stop()
    threading.Thread(target=inner, daemon=True).start()
                                                              
# start the frames in the grid 
for frame in (start_frame, game_frame):
    frame.grid(row=0, column=0, sticky='news')  

welcome_label = Label(start_frame, text='🎮 Welcome to Rock Paper Scissors 🎮', font=("Arial", 24, "bold"), bg='white')
welcome_label.place(x=180, y=30)

round_label = Label(start_frame, text='Select Rounds:', font=("Arial", 18), bg='white')
round_label.place(x=400, y=100)  

# Function to raise a frame to the top
def show_frame(f):
    f.tkraise()

def select_rounds(n):
    play_sound("sounds/round_click.wav")

    global total_rounds, current_round, game_active, score_p, score_b
    total_rounds = n
    current_round = 0 
    score_p = 0
    score_b = 0
    game_active = True 
    show_frame(game_frame)  #  switch to gameplay screen

for i in range(1, 11): 
    Button(start_frame, text=f"{i} Round{'s' if i > 1 else ''}", font=("Arial", 14),
           width=12, bg="#30e30c" if i%2==0 else '#df2443' , fg="black", command=partial(select_rounds, i))\
           .place(x=160 + (i-1) *150 if i<=5 else 160 + (i-6)*150, y=150 if i<=5 else 197 ) 

 
# Creating labels
l1 = Label(game_frame, text='Player(You)', font=('Arial', 20), bg='#612685', fg='white')  
l1.place(x=80, y=30) 

bot_icon = Image.open("images/bot_icon.jpg").resize((100, 80))
bot_icon = ImageTk.PhotoImage(bot_icon)
# Place bot image
l2 = Label(game_frame, image=bot_icon, bg='white')
l2.image = bot_icon  # Keep a reference to the image to prevent garbage collection 
l2.place(x=710, y=20)

l3 = Label(game_frame, text='Vs', font=('Arial', 25), bg='#2eaf14', fg='white') 
l3.place(x=470, y=230)  

# load default image and flip it or transpose
img_p = Image.open('images/default.jpg') 
img_p = img_p.resize((300, 300))  

img_b = img_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_b = ImageTk.PhotoImage(img_b)  

## ----------------rocks-----------------------
Rock_p = Image.open('images/rock.jpg').resize((300, 300))  # Load rock image
Rock_b = Rock_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flip for bot image 
# put on canvas
Rock_p = ImageTk.PhotoImage(Rock_p)
Rock_b = ImageTk.PhotoImage(Rock_b)

# load rock angry image
RockAngry_p = Image.open('images/RockAngry.webp') 
RockAngry_p = RockAngry_p.resize((300, 300)) 
RockAngry_b = RockAngry_p.transpose(Image.FLIP_LEFT_RIGHT) # for bot
#put on canvas
RockAngry_p = ImageTk.PhotoImage(RockAngry_p)
RockAngry_b = ImageTk.PhotoImage(RockAngry_b) 

# Load rock fear image
RockFear_p = Image.open('images/RockFear.png').resize((300, 300)) 
RockFear_b = RockFear_p.transpose(Image.FLIP_LEFT_RIGHT)  # for bot rock hand
# put on canvas
RockFear_p = ImageTk.PhotoImage(RockFear_p)
RockFear_b = ImageTk.PhotoImage(RockFear_b) 

## -----------------papers---------------------

Paper_p = Image.open('images/Paper.jpg').resize((300, 300))  # Load paper image 
Paper_b = Paper_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flip for bot image
# put on canvas
Paper_p = ImageTk.PhotoImage(Paper_p)
Paper_b = ImageTk.PhotoImage(Paper_b) 

# load paper angry image
PaperAngry_p = Image.open('images/PaperAngry.jpg').resize((300, 300))  
PaperAngry_b = PaperAngry_p.transpose(Image.FLIP_LEFT_RIGHT)  # for bot rock hand
# put on canvas
PaperAngry_p = ImageTk.PhotoImage(PaperAngry_p)
PaperAngry_b = ImageTk.PhotoImage(PaperAngry_b)    

# load paper fear image 
PaperFear_p = Image.open('images/PaperFear.jpg').resize((300, 300))  
PaperFear_b = PaperFear_p.transpose(Image.FLIP_LEFT_RIGHT)  # for bot paper hand 
# put on canvas
PaperFear_p = ImageTk.PhotoImage(PaperFear_p)
PaperFear_b = ImageTk.PhotoImage(PaperFear_b)

# -----------------scissors---------------------
Scissor_p = Image.open('images/Scissor.webp').resize((300, 300))  # Load scissor image
Scissor_b = Scissor_p.transpose(Image.FLIP_LEFT_RIGHT)  # Flip for bot image 
# put on canvas 
Scissor_p = ImageTk.PhotoImage(Scissor_p)
Scissor_b = ImageTk.PhotoImage(Scissor_b) 

# load scissor Angry image
ScissorAngry_p = Image.open('images/ScissorAngry.webp').resize((300, 300)) 
ScissorAngry_b = ScissorAngry_p.transpose(Image.FLIP_LEFT_RIGHT)  # for bot scissor hand 
# put on canvas 
ScissorAngry_p = ImageTk.PhotoImage(ScissorAngry_p)
ScissorAngry_b = ImageTk.PhotoImage(ScissorAngry_b) 

# load scissor fear image
ScissorFear_p = Image.open('images/ScissorFear.png').resize((300, 300)) 
ScissorFear_b = ScissorFear_p.transpose(Image.FLIP_LEFT_RIGHT)  # for bot scissor hand
# put on canvas
ScissorFear_p = ImageTk.PhotoImage(ScissorFear_p)
ScissorFear_b = ImageTk.PhotoImage(ScissorFear_b)

# selection img 
img_s = Image.open('images/selection.jpg').resize((300,110)) 
img_s = ImageTk.PhotoImage(img_s) 

# Put image on canvas on specific coordinate
canvas.create_image(0,470, anchor='nw', image=img_s) 
canvas.create_image(620,470, anchor='nw', image=img_s)  

# Result images
win_img = Image.open('images/YouWin.jpg').resize((200, 200))
win_img = ImageTk.PhotoImage(win_img)

lose_img = Image.open('images/YouLose.jpg').resize((200, 200))
lose_img = ImageTk.PhotoImage(lose_img)

draw_img = Image.open('images/YouTie.jpg').resize((200, 200))
draw_img = ImageTk.PhotoImage(draw_img)


player_img_id = canvas.create_image(0, 100, anchor='nw', image=img_p) # default images
bot_img_id    = canvas.create_image(620, 100, anchor='nw', image=img_b) 

# Initialize empty images for moves (to show after player clicks)
player_move_id = canvas.create_image(0, 100, anchor='nw', image=None)
bot_move_id = canvas.create_image(620, 100, anchor='nw', image=None)

# Initially hide move hands
canvas.itemconfig(player_move_id, state='hidden')
canvas.itemconfig(bot_move_id, state='hidden')

score_p = 0  # Player score
score_b = 0  # Bot score
canvas.create_text(490,100, text=f"Score - You: {score_p} | Bot: {score_b}", font=('Arial', 17), fill='black', tags='result') 

# Function to show result image based on the game outcome 
def show_result_image(img):
    # Remove any previous result image or text
    canvas.delete('result_img')
    
    # Display new image at center-bottom
    canvas.create_image(480, 500, image=img, anchor='center', tags='result_img')

# clear function or reset
def clear():
    play_sound("sounds/reset_and_menu.wav", 1.4) 

    canvas.delete('result') 
    canvas.delete('result_img')
    
    global score_p, score_b, current_round  # Access global scores 
    score_p = 0  # Reset player score
    score_b = 0  # Reset bot score
    current_round = 0  # Reset current round
    canvas.create_text(490,100, text=f"Score - You: {score_p} | Bot: {score_b}", font=('Arial', 17), fill='black', tags='result') 
    
    # Show default hands
    canvas.itemconfig(player_img_id, state='normal')
    canvas.itemconfig(bot_img_id, state='normal')

    # Hide move hands
    canvas.itemconfig(player_move_id, state='hidden')
    canvas.itemconfig(bot_move_id, state='hidden')


def end_game_popup():
    popup = Toplevel(root)
    popup.title("🎮 Game Over!🎮")
    popup.geometry("400x250") 
    popup.configure(bg="#ffe4e1")  # Light pink background
    popup.resizable(False, False)

    # CENTER THE POPUP
    popup.update_idletasks()
    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    x = int((screen_width / 2) - (popup_width / 2))
    y = int((screen_height / 2) - (popup_height / 2))
    popup.geometry(f"400x250+{x}+{y}")

    # Message with emojis
    msg = Label(popup, text="🏆 Khel khatam bro! 🎉\nDo you want to play again?", 
                font=("Arial", 16, "bold"), bg="#ffe4e1", fg="#2d033b", justify='center')
    msg.pack(pady=30) 

    # Button frame
    btn_frame = Frame(popup, bg="#ffe4e1")
    btn_frame.pack(pady=10)

    # PLAY AGAIN button
    play_btn = Button(btn_frame, text="🔁 Play Again", font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", width=12, command=lambda: [popup.destroy(), clear(), show_frame(start_frame), loop_sound("sounds/welcome.mp3")])
    play_btn.grid(row=0, column=0, padx=20)

    # EXIT button  
    exit_btn = Button(btn_frame, text="❌ Exit", font=("Arial", 12, "bold"),
                      bg="#f44336", fg="white", width=12, command=lambda: [play_clip('sounds/Quit.mp3',0,2),popup.after(2020,root.destroy)])
    exit_btn.grid(row=0, column=1, padx=20) 

    # Center popup over root window
    popup.transient(root)
    popup.grab_set()
    root.wait_window(popup)  

# game : actual function
def game(player):
 
    global current_round, total_rounds, game_active, score_p, score_b  # Access global variables
    if not game_active: 
        return  # Stop further moves if game is over

    canvas.delete('result')  # clear previous result text
     
    choices = ['r', 'p', 's']  # list of choices for bot 
    bot = random.choice(choices) # randomly selecting bot choice 

     # Hide default hands
    canvas.itemconfig(player_img_id, state='hidden')
    canvas.itemconfig(bot_img_id, state='hidden')

    # Show move hands
    canvas.itemconfig(player_move_id, state='normal')
    canvas.itemconfig(bot_move_id, state='normal')

    # update player's win image
    if player == 'r' and bot=='s' :
        play_sound("sounds/rocks.mp3",0.8) 
        canvas.itemconfig(player_move_id, image=RockAngry_p)  # Player wins with rock
        canvas.itemconfig(bot_move_id, image=ScissorFear_b)  # Bot loses with scissor
    elif player == 'p' and bot=='r':
        play_sound("sounds/paper.mp3")
        canvas.itemconfig(player_move_id, image=PaperAngry_p)  # Player wins with paper 
        canvas.itemconfig(bot_move_id, image=RockFear_b) 
    elif player == 's' and bot=='p':
        play_clip("sounds/scissor.mp3", 0, 1)
        canvas.itemconfig(player_move_id, image=ScissorAngry_p)  # Player wins with scissor 
        canvas.itemconfig(bot_move_id, image=PaperFear_b)  # Bot loses with paper
    # update bot's win image
    elif bot == 'r' and player=='s':
        play_clip("sounds/scissor.mp3", 0, 1)
        canvas.itemconfig(bot_move_id, image=RockAngry_b)  # Bot wins with rock 
        canvas.itemconfig(player_move_id, image=ScissorFear_p)  # Player loses with scissor
    elif bot == 'p' and player=='r' :
        play_sound("sounds/rocks.mp3",0.8) 
        canvas.itemconfig(bot_move_id, image=PaperAngry_b)  # Bot wins with paper            
        canvas.itemconfig(player_move_id, image=RockFear_p)  # Player loses with rock         
    elif bot=='s' and player=='p':
        play_sound("sounds/paper.mp3")
        canvas.itemconfig(bot_move_id, image=ScissorAngry_b)  # Bot wins with scissor
        canvas.itemconfig(player_move_id, image=PaperFear_p)  # Player loses with paper
    # match tie cases
    elif bot == 'r' and player=='r': 
        play_sound("sounds/rocks.mp3",0.8) 
        canvas.itemconfig(player_move_id, image=Rock_p)  # Player ties with rock
        canvas.itemconfig(bot_move_id, image=Rock_b)  # Bot ties with rock 
    elif bot == 's' and player=='s': 
        play_clip("sounds/scissor.mp3", 0, 1)
        canvas.itemconfig(player_move_id, image=Scissor_p)  # Player ties with scissor 
        canvas.itemconfig(bot_move_id, image=Scissor_b)  # Bot ties with scissor 
    else:
        play_sound("sounds/paper.mp3")  
        canvas.itemconfig(player_move_id, image=Paper_p)
        canvas.itemconfig(bot_move_id, image=Paper_b)  # Player ties with paper

    # Determine result with logic
    if player == bot:
        result = "D"
    elif (player == 'r' and bot == 's') or (player == 'p' and bot == 'r') or (player == 's' and bot == 'p'):
        result = "W" 
        score_p += 1 
    else:
        result = "L"
        score_b += 1

    current_round += 1
    canvas.create_text(490,100, text=f"Score - You: {score_p} | Bot: {score_b}", font=('Arial', 17), fill='black', tags='result') 
    # create round text
    canvas.create_text(510, 150, text=f"Round: {current_round}/{total_rounds}", font=('Arial', 17,'bold'), fill='blue', tags='result') 

    if current_round >= total_rounds:
        # disable buttons or show final message
        game_active = False
        if score_p > score_b:
            play_clip("sounds/winner.wav", 0, 3.2,0.5)
            show_result_image(win_img)
        elif score_b > score_p: 
            play_clip("sounds/Lost.wav",0,2.5,0.5)   
            show_result_image(lose_img)
        else:
            play_sound("sounds/draw.mp3")  
            show_result_image(draw_img)

        root.after(1000, end_game_popup)  # Show popup after 1 seconds 
         
    
# creating buttons  
rock_btn = Button(game_frame, text='Rock', font=('Arial', 17), command=lambda: game('r'), bg='deeppink', fg='white') 
rock_btn.place(x=18, y=420)  

paper_btn = Button(game_frame, text='Paper', font=('Arial', 17), command=lambda: game('p'), bg='green', fg='white')
paper_btn.place(x=115, y=420) 

scissor_btn = Button(game_frame, text='Scissor', font=('Arial', 17), command=lambda: game('s'), bg='blue', fg='white') 
scissor_btn.place(x=214, y=420)

clear_btn = Button(game_frame, text='Reset', font=('Times', 15, 'bold'),width=8, command=clear, bg='#C70039', fg='white') 
clear_btn.place(x=430, y=30)   

Button(game_frame, text='Back to Menu', font=('Arial', 12), bg='red', fg='white',
        command=lambda: [play_sound("sounds/reset_and_menu.wav"), show_frame(start_frame),loop_sound("sounds/welcome.mp3")]).place(x=870, y=20)  
  
show_frame(start_frame)  
loop_sound("sounds/welcome.mp3")
root.mainloop() # This line starts the Tkinter event loop  