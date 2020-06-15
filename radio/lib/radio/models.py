from dataclasses import dataclass


@dataclass
class Track:
    name: str
    duration: int
    path_file: str
