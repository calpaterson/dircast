from logging import basicConfig, INFO, getLogger

def main():
    basicConfig(level=INFO)
    getLogger(__name__).info("started")

