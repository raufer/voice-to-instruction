
def parse_labels(filepath):
    with open(filepath) as f:
        xs = [l.strip() for l in f]
    return xs