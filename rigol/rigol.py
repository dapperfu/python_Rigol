from cached_property import cached_property

from .key import Key
from .usbtmc import Usbtmc


class RigolScope:
    """Class to control a Rigol DS1000 series oscilloscope"""

    def __init__(self, *args, device: [Usbtmc, str] = "/dev/usbtmc0"):
        if len(args) > 0:
            raise Exception("No.")
        if isinstance(device, str):
            device = Usbtmc(device)
        self.device = device

        self.key = Key(device=self.device)

    def write(self, command):
        """Send an arbitrary command directly to the scope"""
        self.device.write(command)

    def read(self, command):
        """Read an arbitrary amount of data directly from the scope"""
        return self.device.read(command)

    def reset(self):
        """Reset the instrument"""
        self.device.reset()

    @cached_property
    def __idn__(self):
        return self.device.name()

    @property
    def model(self):
        return self.__idn__.split(",")[1]

    @property
    def vendor(self):
        return self.__idn__.split(",")[0]

    @property
    def serial(self):
        return self.__idn__.split(",")[2]

    @property
    def version(self):
        return self.__idn__.split(",")[3]

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.model}>"

    def __enter__(self):
        print("in __enter__")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("in __exit__")


if __name__ == "__main__":
    scope = RigolScope()
    print(scope.device.name())
