# Voice to Instruction

Simple script to go from voice to instruction

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
