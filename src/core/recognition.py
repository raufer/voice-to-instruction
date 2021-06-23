import logging

from typing import Optional

from speech_recognition import Microphone
from speech_recognition import Recognizer

from src.constants import BACKEND

logger = logging.getLogger(__name__)


def recognize(microphone: Microphone, recognizer: Recognizer, backend: str, timeout=2, phrase_time_limit=2) -> Optional[str]:
    """
    Recognizes a short audio input from the microphone
    """

    try:

        with microphone as source:
            # uncomment if in an environment with background noise
            # calibration of the noise level might be required
            # recognizer.adjust_for_ambient_noise(source)
            logger.info(f"Speak")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        if backend == BACKEND.GOOGLE:
            transcription = recognizer.recognize_google(audio)
        elif backend == BACKEND.SPHINX:
            transcription = recognizer.recognize_sphinx(audio)

        logger.info(f"CMD: '{transcription}'")

    except Exception as e:
        transcription = None
        logger.error(str(e))
        logger.info(f"ASR process failed")

    return transcription


