import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import threading
import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- FILTER HELPERS ----------------
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    return butter(order, [low, high], btype='band')

def apply_filter(data, fs, lowcut, highcut, gain_db):
    b, a = butter_bandpass(lowcut, highcut, fs)
    filtered = lfilter(b, a, data)
    gain = 10 ** (gain_db / 20.0)
    return filtered * gain

def apply_equalizer(audio_data, fs, gains):
    low_band = apply_filter(audio_data, fs, 60, 250, gains[0])
    mid_band = apply_filter(audio_data, fs, 250, 4000, gains[1])
    high_band = apply_filter(audio_data, fs, 4000, 12000, gains[2])
    eq_audio = low_band + mid_band + high_band
    eq_audio /= np.max(np.abs(eq_audio))  # normalize
    return eq_audio

# ---------------- GUI APP ----------------
class EqualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎚️ Modern Audio Equalizer")
        self.root.geometry("600x500")

        self.file_path = None
        self.audio_data = None
        self.sample_rate = None

        # Sliders frame
        sliders_frame = ttk.Frame(self.root)
        sliders_frame.pack(pady=20)

        self.sliders = {}
        bands = ["Bass (60–250Hz)", "Mid (250–4kHz)", "Treble (4k–12kHz)"]
        for band in bands:
            label = ttk.Label(sliders_frame, text=band, bootstyle=INFO)
            label.pack(pady=5)
            slider = ttk.Scale(sliders_frame, from_=-12, to=12, orient=HORIZONTAL, length=400)
            slider.set(0)
            slider.pack(pady=5)
            self.sliders[band] = slider

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Load WAV", command=self.load_audio, bootstyle=SUCCESS).pack(side=LEFT, padx=10)
        ttk.Button(btn_frame, text="Play Equalized", command=self.play_equalized, bootstyle=PRIMARY).pack(side=LEFT, padx=10)

        # Frequency visualization
        self.fig, self.ax = plt.subplots(figsize=(6,2))
        self.ax.set_ylim([-1, 1])
        self.ax.set_title("Waveform Preview")
        self.line, = self.ax.plot([], [], color="cyan")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=10)

        pygame.mixer.init()

    def load_audio(self):
        path = filedialog.askopenfilename(title="Select a WAV file", filetypes=[("WAV Files", "*.wav")])
        if not path:
            return
        try:
            fs, data = wavfile.read(path)
            if len(data.shape) > 1:
                data = data.mean(axis=1)
            self.sample_rate = fs
            self.audio_data = data.astype(np.float32) / np.max(np.abs(data))
            self.file_path = path
            messagebox.showinfo("Loaded", f"Loaded: {path.split('/')[-1]}")
            self.update_waveform(self.audio_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load WAV:\n{e}")

    def play_equalized(self):
        if self.audio_data is None:
            messagebox.showwarning("No audio", "Load a file first!")
            return
        gains = tuple(slider.get() for slider in self.sliders.values())
        threading.Thread(target=self._process_and_play, args=(gains,), daemon=True).start()

    def _process_and_play(self, gains):
        eq_audio = apply_equalizer(self.audio_data, self.sample_rate, gains)
        eq_int16 = np.int16(eq_audio * 32767)
        sound = pygame.mixer.Sound(buffer=eq_int16.tobytes())
        sound.play()

    def update_waveform(self, data):
        self.line.set_data(np.arange(len(data)), data)
        self.ax.set_xlim(0, len(data))
        self.canvas.draw()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")  # Modern dark theme
    app = EqualizerApp(root)
    root.mainloop()
