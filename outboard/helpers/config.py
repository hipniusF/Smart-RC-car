from yaml import full_load
from pathlib import Path

path = Path(__file__).parent / 'config.yml'

with path.open() as f:
    config = full_load(f.read())

address = (config['onboard']['address'], config['onboard']['port'])
video_address = (config['onboard']['address'], config['onboard']['video']['port'])
