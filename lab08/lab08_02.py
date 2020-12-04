from typing import List, Any, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import wave
import os
import struct


def get_file_names(path: str) -> List[str]:
    will_return: List[str] = os.listdir("./{}".format(path))
    return will_return


def main() -> None:
    file_names = get_file_names("set_a/")
    for i in file_names:
        f = wave.open("./set_a/{}".format(i))
        all_frames = f.readframes(-1)
        print(all_frames[:10])
        getInforFromAudio(f)
        samples = showStructOfFile(f, all_frames)
        drawPicture(f, samples)


def drawPicture(file, samples) -> None:
    framerate = file.getframerate()
    t = [float(i) / framerate for i in range(len(samples))]
    plt.plot(t, samples)
    plt.show()

def showStructOfFile(file, all_frames) -> Tuple[int]:
    print(len(file.readframes(-1)))
    samples: Tuple[int] = struct.unpack('h' * file.getnframes(), all_frames)
    print(samples[0:10])
    return samples


def getInforFromAudio(file) -> None:
    print("the sampleWidth = {} bytes".format(file.getsampwidth()))
    print("the number of channels = {}".format(file.getnchannels()))
    print("the number of frames is {}".format(file.getnframes()))
    print("the sample rate is {} Hz".format(file.getframerate()))


if __name__ == '__main__':
    main()
