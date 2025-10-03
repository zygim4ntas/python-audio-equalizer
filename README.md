# python-audio-equalizer
A sleek, real-time audio equalizer for WAV files built in Python 3.13. Adjust bass, mid, and treble using a modern GUI, preview waveforms, and enjoy threaded audio playback. || beginner project

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
