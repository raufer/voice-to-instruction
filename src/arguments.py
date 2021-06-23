import argparse


parser = argparse.ArgumentParser(description='Voice to Instruction')

parser.add_argument("--backend", help='ASR backend engine to use', default='google')
parser.add_argument("--duration", help='Duration of the voice instruction', default=2)
parser.add_argument("--press", help='Press to speak key', default='x')

args = parser.parse_args()