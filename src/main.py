import sys
sys.path.append('/Users/raulferreira/p01/voice-to-label')

import logging

import keyboard

from typing import List

from src.core.recognition import recognize
from src.core.resources import initialize_resources
from src.ops.phonetic import phonetically_closest
from src.utils.files import parse_labels
from src.constants import PRESS_TO_SPEAK
from src.ops.screen import label_selection

logger = logging.getLogger(__name__)


def main(instruction_set: List[str], backend: str, duration: int, press_to_speak=PRESS_TO_SPEAK):
    """
    Main loop of the program

    * Waits for a "listen" instruction (pressing of a certain key)
    * Speech to text process
    * Searches the phonetically closer instruction amid the instruction set
    """
    logger.info("Voice to Instruction")
    logger.info(f"Using backend '{backend}'")
    logger.info(f"Voice instruction duration '{duration}'")
    logger.info(f"Press to listen key '{press_to_speak}'")

    logger.info("Running main loop")
    recognizer, microphone = initialize_resources()

    while True:
        logger.info(f"Waiting for 'LISTEN' instruction (press '{press_to_speak}')")
        keyboard.wait(press_to_speak)

        transcription = recognize(microphone, recognizer, backend=backend, timeout=duration, phrase_time_limit=duration)

        if transcription:
            min_ = phonetically_closest(instruction_set, transcription)
            closest = instruction_set[min_]
            logger.info(f"> ASR: '{closest}'")

            label_selection(min_)


if __name__ == '__main__':

    import os
    import time

    from src.arguments import args

    filename = '/Users/raulferreira/p01/voice-to-label/resources/labels.txt'
    instruction_set = parse_labels(filename)

    main(instruction_set, args.backend, args.duration, args.press)

