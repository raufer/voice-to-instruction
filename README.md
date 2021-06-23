# Voice to Instruction

Simple script to go from voice to instruction:

    1. Waits for a "listen" instruction (pressing of a certain key)
    2. Speech to text process
    3. Searches the most likely instruction amid an instruction set, given a phonetic similarity criterion


### Requirements

Tested in:

* Python `3.7`
* OS `macOS Catalina`

#### Mac OS Catalina Dependencies

Dependencies for `PocketShinx`:

```sh
brew install swig
brew install openal-soft
brew install portaudio

cd /usr/local/include
ln -s /usr/local/Cellar/openal-soft/1.20.1/include/AL/* .
```

Test the installation with:

```sh
python -m speech_recognition
```
