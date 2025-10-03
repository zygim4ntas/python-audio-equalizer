# python-audio-equalizer
A sleek, real-time audio equalizer for WAV files built in Python 3.13. Adjust bass, mid, and treble using a modern GUI, preview waveforms, and enjoy threaded audio playback. Beginner project

# 🎚️ Python Audio Equalizer (Modern GUI)

A **real-time audio equalizer** built in **Python 3.13** with a sleek, modern interface. Load WAV files, adjust bass, mid, and treble levels, and listen to the equalized output—all from a stylish GUI.

---

## Features

- ✅ Modern dark-themed GUI using **ttkbootstrap**
- ✅ Adjustable **Bass, Mid, and Treble sliders**
- ✅ Waveform preview with **matplotlib**
- ✅ Audio playback using **pygame**, no `pydub` needed
- ✅ Cross-platform: works on **Linux, macOS, and Windows**
- ✅ Multithreaded playback keeps the GUI responsive

---

## Installation

```bash
# Clone the repository
git clone https://github.com/zygim4ntas/python-audio-equalizer.git
cd python-audio-equalizer

# Create virtual environment (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
---

## Usage 

```bash
python audio_equalizer.py
```
1. Click **Load WAV** and select a .wav file.

2. Adjust the **Bass, Mid, and Treble sliders** to change the audio output.

3. Click **Play Equalized** to hear the processed audio.

4. Watch the **waveform preview** update in real-time.

## Recommended Workflow

- Start with all sliders at 0 dB.

- Gradually adjust Bass (60–250 Hz), Mid (250–4 kHz), and Treble (4–12 kHz) to taste.

- Use short WAV files first to experiment with settings.

---

## Dependencies

- Python 3.13+

- `numpy`

- `scipy`

- `pygame`

- `matplotlib`

- `ttkbootstrap`

Install with:

```bash
pip install -r requirements.txt
```

---

## Future improvements

- Add **MP3 support** via `ffmpeg`

- Real-time **frequency spectrum visualization**

- Save equalized audio to a new file

- Keyboard shortcuts for playback control

- Option to **load multiple audio files** and switch tracks

- Add **preset EQ modes** like Rock, Jazz, Classical

---

## License

This project is licensed under the **MIT License**.

