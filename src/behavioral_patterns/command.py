import abc
from typing import List


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class GarageDoor:
    def open(self):
        print("Opening garage...")

    def close(self):
        print("Closing garage...")


class Light:
    def __init__(self, light_name: str):
        self._light_name = light_name

    def on(self):
        print("{} light is on".format(self._light_name))

    def off(self):
        print("{} light is off".format(self._light_name))


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class OpenGarageDoorCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.open()

    def undo(self):
        self._garage_door.close()


class CloseGarageDoorCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.close()

    def undo(self):
        self._garage_door.open()


class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class MacroCommand(Command):
    def __init__(self, commands: List):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in self._commands:
            command.undo()


class RemoteControlWithUndo:
    NUM_OF_SLOTS = 7
    _on_commands = []
    _off_commands = []

    def __init__(self):
        slots = range(self.NUM_OF_SLOTS - 1)
        for i in slots:
            self._on_commands.append(NoCommand())
            self._off_commands.append(NoCommand())

        self._undo_command = NoCommand()

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_pushed(self, slot: int):
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_pushed(self, slot: int):
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_pushed(self):
        self._undo_command.undo()


def main():
    remote_control = RemoteControlWithUndo()
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    garage_door = GarageDoor()

    living_room_light_on = TurnOnLightCommand(living_room_light)
    living_room_light_off = TurnOffLightCommand(living_room_light)
    kitchen_light_on = TurnOnLightCommand(kitchen_light)
    kitchen_light_off = TurnOffLightCommand(kitchen_light)
    garage_door_open = OpenGarageDoorCommand(garage_door)
    garage_door_close = CloseGarageDoorCommand(garage_door)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, garage_door_open, garage_door_close)

    remote_control.on_button_pushed(0)
    remote_control.off_button_pushed(0)
    remote_control.undo_button_pushed()
    remote_control.on_button_pushed(1)
    remote_control.off_button_pushed(1)
    remote_control.undo_button_pushed()
    remote_control.on_button_pushed(2)
    remote_control.off_button_pushed(2)
    remote_control.undo_button_pushed()

    party_on_macro = MacroCommand(
        [
            living_room_light_on,
            kitchen_light_on,
            garage_door_open
        ]
    )

    party_off_macro = MacroCommand(
        [
            living_room_light_off,
            kitchen_light_off,
            garage_door_close
        ]
    )

    remote_control.set_command(0, party_on_macro, party_off_macro)
    print("Macro ON!")
    remote_control.on_button_pushed(0)
    print("Macro OFF!")
    remote_control.off_button_pushed(0)



if __name__ == "__main__":
    main()

