import sys,wave, numpy, pygame
from pygame.locals import *
from scipy.fftpack import dct
from convert import convert
from add import combine

Number = 30 # number of bars
HEIGHT = 600 # HEIGHT of a bar
WIDTH = 40 #WIDTH of a bar
FPS = 10

file_name = sys.argv[0]
status = 'stopped'
fpsclock = pygame.time.Clock()

#screen init, music playback

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([Number * WIDTH, 50 + HEIGHT])
pygame.display.set_caption('Audio Visualizer')
pygame.mixer.music.load("Nevada.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_endevent()
pygame.mixer.music.set_volume(0.2)
status = "Playing"

#process wave data

f = wave.open("Nevada.wav", 'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
f.close()
wave_data = numpy.frombuffer(str_data, dtype = numpy.short)
wave_data.shape = -1, 2
wave_data = wave_data.T

num = nframes

def Visualizer(nums):
    num = int(nums)
    h = abs(dct(wave_data[0][nframes - num:nframes - num + Number]))
    h = [min(HEIGHT, int(i**(1 / 2.5) * HEIGHT / 100)) for i in h]
    draw_bars(h)

def vis(status):
    global num
    if status == "stopped":
        num = nframes
        return
    elif status == "paused":
        Visualizer(num)
    else:
        num -= framerate / FPS
        if num > 0:
            Visualizer(num)
    

def get_time():
    seconds = max(0, pygame.mixer.music.get_pos() / 1000)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    hms = ("%02d:%02d:%02d" % (h, m, s))
    return hms

def controller(key):
    global status
    if status == "stopped":
        if key == K_RETURN:
            pygame.mixer_music.play()
            status = "playing"
    elif status == "paused":
        if key == K_RETURN:
            pygame.mixer_music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.unpause()
            status = "playing"
    elif status == "playing":
        if key == K_RETURN:
            pygame.mixer.music.stop()
            status = "stopped"
        elif key == K_SPACE:
            pygame.mixer.music.pause()
            status = "paused"

def draw_bars(h):
    bars = []
    for i in h:
        bars.append([len(bars) * WIDTH , 50 + HEIGHT - i, WIDTH - 1, i])
    for i in bars:
        pygame.draw.rect(screen, [255,255,255], i, 0)



frame_count = 0
exiting     = False
clock       = pygame.time.Clock()

while True:    
    if num <= 0:
        status = "stopped"
    screen.fill((0,0,0))
    fpsclock.tick(FPS)
    vis(status)
    frame_count += 1
    filename = "C:/Users/VISHNU P C/Desktop/Music/Snaps/screen_%04d.png" % ( frame_count )
    img=pygame.image.save( screen, filename )
    clock.tick( FPS )
    pygame.display.update()
    if status=="stopped":
        break
    print(status)
directory='C:/Users/VISHNU P C/Desktop/Music/Snaps'
pathIn=directory+'/'
pathOut=pathIn+'/vid/video.avi'
fps=10
time=1
convert(pathIn,pathOut,fps,time)
# combine('C:/Users/VISHNU P C/Desktop/Music/Snaps/vid/video.avi','Nevada.wav','C:/Users/VISHNU P C/Desktop/Music/Snaps/vid/final_video.avi')

    