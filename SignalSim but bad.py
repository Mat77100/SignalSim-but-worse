#made 09/09/26
#bored and wanted to ply VotV, but cant cuz chromebook, so ill make smth instead
import numpy as np
import sounddevice as sd

SampleRate = 44100 #values / second played (frequency). 44100 is 44.1 kHz and is th standard

def GenarateNoise(Duration): #Duration is length of messadge in seconds

    Noise = np.random.uniform(-1,1,SampleRate*Duration)
    Noise = np.convolve(Noise, np.ones(25), mode="same")
    Noise /= 100 #NOISE LOUDNESS

    #Crackling within static
    for i in range(Duration+np.random.randint(5,10)):
        Index = np.random.randint(0,(SampleRate*Duration)-1)
        Noise[Index]*= 10

    return Noise



Noise = GenarateNoise(5)

def AlienLowPulse(Duration):
    t = np.arange(0,Duration,1/SampleRate)
    #Sound = np.sin(2*np.pi*220*t)  #Sine wave
    Sound = 2 * (150 *t %1) -1  #Sawtooth wave
    t = t/Duration
    Pulse = np.where(t<0.5, (2*t)**4, (2*(1-t))**6)
    Sound = Sound * Pulse
    return Sound

Pulse = AlienLowPulse(3)
Pulse = np.pad(Pulse, ((len(Noise)-len(Pulse))//2, (len(Noise)-len(Pulse)) - (len(Noise)-len(Pulse))//2), mode="constant")

Audio = Noise + Pulse

sd.play(Audio,SampleRate)
sd.wait()