from __future__ import annotations

import functools


class Amplifier:
    def __init__(self, description: str) -> None:
        self.description = description
        self.tuner: Tuner | None = None
        self.streaming_player: StreamingPlayer | None = None

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def set_stereo_sound(self) -> None:
        print(f"{self.description} stereo mode on")

    def set_surround_sound(self) -> None:
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, level: int) -> None:
        print(f"{self.description} setting volume to {level}")

    def set_tuner(self, tuner: Tuner) -> None:
        print(f"{self.description} setting tuner to {tuner}")
        self.tuner = tuner

    def set_streaming_player(self, player: StreamingPlayer) -> None:
        print(f"{self.description} setting Streaming player to {player}")
        self.streaming_player = player

    def __str__(self) -> str:
        return self.description


class CdPlayer:
    def __init__(self, description: str, amplifier: Amplifier) -> None:
        self.description = description
        self.amplifier = amplifier
        self.title: str = ""
        self.current_track: int = 0

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def eject(self) -> None:
        print(f"{self.description} eject")

    @functools.singledispatchmethod
    def play(self, _) -> None: ...

    @play.register
    def _(self, title: str) -> None:
        self.title = title
        self.current_track = 0
        print(f'{self.description} playing "{self.title}"')

    @play.register
    def _(self, track: int) -> None:
        if not self.title:
            print(f"{self.description} can't play track {self.current_track}, no cd inserted")
        else:
            self.current_track = track
            print(f"{self.description} playing track {self.current_track}")

    def stop(self) -> None:
        self.current_track = 0
        print(f"{self.description} stopped")

    def paused(self) -> None:
        print(f'{self.description} paused "{self.title}"')

    def __str__(self) -> str:
        return self.description


class Projector:
    def __init__(self, description: str, player: StreamingPlayer) -> None:
        self.description = description
        self.player = player

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def wide_screen_mode(self) -> None:
        print(f"{self.description} in widescreen mode (16x9 aspect ratio)")

    def tv_mode(self) -> None:
        print(f"{self.description} in tv mode (4x3 aspect ratio)")

    def __str__(self) -> str:
        return self.description


class Screen:
    def __init__(self, description: str) -> None:
        self.description = description

    def up(self) -> None:
        print(f"{self.description} going up")

    def down(self) -> None:
        print(f"{self.description} going down")

    def __str__(self) -> str:
        return self.description


class TheaterLights:
    def __init__(self, description: str) -> None:
        self.description = description

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def dim(self, level: int) -> None:
        print(f"{self.description} dimming to {level}%")

    def __str__(self) -> str:
        return self.description


class StreamingPlayer:
    def __init__(self, description: str, amplifier: Amplifier) -> None:
        self.description = description
        self.amplifier = amplifier
        self.current_chapter = 0
        self.movie: str = ""

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    @functools.singledispatchmethod
    def play(self, _) -> None: ...

    @play.register
    def _(self, movie: str) -> None:
        self.movie = movie
        self.current_chapter = 0
        print(f'{self.description} playing "{self.movie}"')

    @play.register
    def _(self, chapter: int) -> None:
        if not self.movie:
            print(f"{self.description} can't play chapter {self.current_chapter}, no movie inserted")
        else:
            self.current_chapter = chapter
            print(f'{self.description} playing chapter {self.current_chapter} of "{self.movie}"')

    def stop(self) -> None:
        self.current_chapter = 0
        print(f'{self.description} stopped "{self.movie}"')

    def paused(self) -> None:
        print(f'{self.description} paused "{self.movie}"')

    def set_two_channel_audio(self) -> None:
        print(f"{self.description} set two channel audio")

    def set_surround_audio(self) -> None:
        print(f"{self.description} set surround audio")

    def __str__(self) -> str:
        return self.description


class Tuner:
    def __init__(self, description: str, amplifier: Amplifier) -> None:
        self.description = description
        self.amplifier = amplifier
        self.frequency: float = 0.0

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def set_frequency(self, frequency: float) -> None:
        print(f"{self.description} setting frequency to {frequency}")
        self.frequency = frequency

    def set_am(self) -> None:
        print(f"{self.description} setting AM mode")

    def set_fm(self) -> None:
        print(f"{self.description} setting FM mode")

    def __str__(self) -> str:
        return self.description


class HomeTheaterFacade:
    def __init__(
        self,
        amp: Amplifier,
        tuner: Tuner,
        player: StreamingPlayer,
        projector: Projector,
        screen: Screen,
        lights: TheaterLights,
    ) -> None:
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights

    def watch_movie(self, movie: str) -> None:
        print("Getting ready to watch movie...")
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)

    def end_movie(self) -> None:
        print("Shutting movie theater down...")
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self, frequency: float) -> None:
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self) -> None:
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()


def main() -> None:
    amp = Amplifier("Amplifier")
    tuner = Tuner("AM/FM Tuner", amp)
    player = StreamingPlayer("Streaming Player", amp)
    _ = CdPlayer("CD Player", amp)
    projector = Projector("Projector", player)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")

    homeTheater = HomeTheaterFacade(amp, tuner, player, projector, screen, lights)

    homeTheater.watch_movie("Raiders of the Lost Ark")
    homeTheater.end_movie()


if __name__ == "__main__":
    main()
