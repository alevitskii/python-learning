from typing import Protocol


class CommandProtocol(Protocol):
    def execute(self) -> None: ...
    def undo(self) -> None: ...


class NoCommand:
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class Stereo:
    def __init__(self, location) -> None:
        self.location = location

    def on(self) -> None:
        print(f"{self.location} stereo is on")

    def off(self) -> None:
        print(f"{self.location} stereo is off")

    def set_cd(self) -> None:
        print(f"{self.location} stereo is set for CD input")

    def set_dvd(self) -> None:
        print(f"{self.location} stereo is set for DVD input")

    def set_radio(self) -> None:
        print(f"{self.location} stereo is set for Radio")

    def set_volume(self, volume: int) -> None:
        print(f"{self.location} Stereo volume set to {volume}")


class StereoOnCommand:
    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()

    def undo(self) -> None:
        self.stereo.off()


class StereoOnWithCDCommand:
    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self) -> None:
        self.stereo.off()


class StereoOffCommand:
    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()

    def undo(self) -> None:
        self.stereo.on()


class Hottub:
    def __init__(self, is_on: bool = False, temperature: int = 98) -> None:
        self.is_on = is_on
        self.temperature = temperature

    def on(self) -> None:
        self.is_on = True

    def off(self) -> None:
        self.is_on = False

    def circulate(self) -> None:
        if self.is_on:
            print("Hottub is bubbling!")

    def jest_on(self) -> None:
        if self.is_on:
            print("Hottub jets are on")

    def jest_off(self) -> None:
        if self.is_on:
            print("Hottub jets are off")

    def set_temperature(self, temperature) -> None:
        if self.temperature < temperature:
            print(f"Hottub is heating to a steaming {temperature} degrees")
        else:
            print(f"Hottub is cooling to {temperature} degrees")
        self.temperature = temperature


class HottubOffCommand:
    def __init__(self, hottub: Hottub) -> None:
        self.hottub = hottub

    def execute(self) -> None:
        self.hottub.set_temperature(98)
        self.hottub.off()

    def undo(self) -> None:
        self.hottub.on()


class HottubOnCommand:
    def __init__(self, hottub: Hottub) -> None:
        self.hottub = hottub

    def execute(self) -> None:
        self.hottub.on()
        self.hottub.set_temperature(104)
        self.hottub.circulate()

    def undo(self) -> None:
        self.hottub.off()


class MacroCommand:
    def __init__(self, commands: list[CommandProtocol]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()


class RemoteControlWithUndo:
    def __init__(self) -> None:
        self.on_commands: list[CommandProtocol] = [NoCommand() for _ in range(7)]
        self.off_commands: list[CommandProtocol] = [NoCommand() for _ in range(7)]
        self.undo_command: CommandProtocol = NoCommand()

    def set_command(self, slot: int, on_command: CommandProtocol, off_command: CommandProtocol) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def off_button_was_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def undo_button_was_pushed(self) -> None:
        self.undo_command.execute()

    def __str__(self) -> str:
        s = "\n------ Remote Control -------\n"
        for idx in range(len(self.on_commands)):
            s += f"[slot {idx}] {type(self.on_commands[idx]).__name__}     {type(self.off_commands[idx]).__name__}\n"
        s += f"[undo] {type(self.undo_command).__name__}\n"
        return s


def main() -> None:
    remote_control = RemoteControlWithUndo()

    stereo = Stereo("Living Room")
    hottub = Hottub()

    stereo_on = StereoOnCommand(stereo)
    hottub_on = HottubOnCommand(hottub)
    stereo_off = StereoOffCommand(stereo)
    hottub_off = HottubOffCommand(hottub)

    remote_control.set_command(0, stereo_on, stereo_off)
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()

    party_on = [stereo_on, hottub_on]
    party_off = [stereo_off, hottub_off]

    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control.set_command(1, party_on_macro, party_off_macro)

    print(remote_control)
    print("--- Pushing Macro On---")
    remote_control.on_button_was_pushed(1)
    print("--- Pushing Macro Off---")
    remote_control.off_button_was_pushed(1)
    remote_control.undo_button_was_pushed()


if __name__ == "__main__":
    main()
