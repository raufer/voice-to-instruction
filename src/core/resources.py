import logging
import speech_recognition as sr


logger = logging.getLogger(__name__)


def initialize_resources():
    """
    """

    logger.info(f"Creating an instance of a Recognizer")
    recognizer = sr.Recognizer()

    logger.info("Creating a connection to the host Microphone")

    microphones = sr.Microphone.list_microphone_names()
    index = next((i for i, m in enumerate(microphones) if m == 'MacBook Pro Microphone'))
    logger.info(f"Using mic '{microphones[index]}'")

    # instead of using an audio file as the source, we will use the default system microphone.
    microphone = sr.Microphone(device_index=index)

    return recognizer, microphone

