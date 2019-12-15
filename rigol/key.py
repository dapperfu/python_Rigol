import re


class CommandsFactory:
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            raise Exception("No.")

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.__class__.__name__.upper()}"


Subsystem = type("Subsystem", (CommandsFactory,), {})

with open("../Documentation/DS1000DE_Command_QuickReference.txt", "r") as file:
    DS1000DE_Command_QuickReference = file.read()


def key_factory(key_str: str, wait: int = 0):
    def press_key(self):
        command_string = f":{self}:{key_str}"
        print(command_string)
        self.device.write(f":{self}:{key_str}")

    return press_key


def key_factory2(key_str: str, wait: int = 0):
    key_str = key_str.strip().strip(":").split(":")[-1].upper()
    key_function = key_factory(key_str, wait)
    return key_str.lower(), key_function


command_re = re.compile(r"(:KEY:[\w]+)")
subsystem_commands = dict()
for result in command_re.findall(DS1000DE_Command_QuickReference):
    if result.startswith(":KEY"):
        key_str, key_function = key_factory2(result)
        subsystem_commands[key_str] = key_function

Key = type("Key", (Subsystem,), subsystem_commands)
