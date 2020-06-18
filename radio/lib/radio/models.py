from dataclasses import dataclass


@dataclass
class Track:
    title: str
    album: str
    artist: str
    year: str

    @classmethod
    def from_dict(cls, response: dict):
        return cls(
            title=response['title'],
            album=response['album'],
            artist=response['artist'],
            year=response['year'],
        )

    def to_dict(self):
        return dict(
            title=self.title,
            album=self.album,
            artist=self.artist,
            year=self.year,
        )
