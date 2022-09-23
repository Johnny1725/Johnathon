###############################
##Name:
##Date:
##Description:
###############################

#import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from waveform_vis import WaveformVis


MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

class Note(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        self.waveform = form
        pygame.mixer.Sound.__init__(self, buffer = self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        samples = array("h", [0] * period)

        if(self.waveform == "square"):
            for t in range(period):
                if (t < period / 2):
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude
            vis = WaveformVis()
            vis.visSamples(samples, "square")

        elif(self.waveform == "triangle"):
            for t in range(period):
                if (t <= period / 4):
                    samples[t] = int(round(780.166667*t))
                elif(t <= period * 3/4):
                    amplitude -= 780.166667
                    samples[t] = int(round(amplitude))
                else:
                    amplitude += 780.166667
                    samples[t] = int(round(amplitude))
            vis = WaveformVis()
            vis.visSamples(samples, "triangle")

        elif(self.waveform == "sawTooth"):
            for t in range(period):
                if (t <= period / 2):
                    samples[t] = int(round(780.166667/2*t))
                else:
                    amplitude -= 780.166667/2
                    samples[t] = int(round(-amplitude))
                
            vis = WaveformVis()
            vis.visSamples(samples, "sawTooth")
            

        return samples
def wait_for_note_start():
    while(True):
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.01)

def wait_for_note_stop(key):
    while (GPIO.input(key)):
        sleep(0.1)

pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

freq = 261.6
form = ["square", "triangle", "sawTooth" ] # triangle, square, sawTooth
note = Note(freq,1)
keys = [20, 16, 12]
notes = []




GPIO.setmode(GPIO.BCM)



GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

for n in range(len(form)):
    notes.append(Note(form[n], 1))

print "Welcome to Paper Piano!"
print "Press Ctrl+C to exit..."

try:
    while(True):
        key = wait_for_note_start()
        notes[key].play(-1)
        wait_for_note_stop(keys[key])
        notes[key].stop()

except KeyboardInterrupt:
    GPIO.cleanup()
