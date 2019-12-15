import os
import warnings

from cached_property import cached_property


class Usbtmc:
    """Simple implementation of a USBTMC device driver.
    
    >> The USBTMC (USB Test and Measurement Class) and USBTMC-USB488 are two related USB (Universal Serial Bus) class specifications. They were officially adopted on December 22, 2002. The purpose of USBTMC is to describe the requirements for test-and-measurement devices with a USB interface. USBTMC defines the protocol for exchanging messages between hosts and devices.
      
    https://www.eetimes.com/usbtmc-unwrapped/#
    """

    def __init__(self, device: [str] = "/dev/usbtmc0"):
        self.dev_device = device
        self.channels = list()

    @property
    def __file__(self):
        os_open_configuration = {
            "path": self.dev_devicea,
            "flags": os.O_RDWR | os.O_DIRECT | os.O_SYNC,
        }
        __file = os.open(self.dev_devicea, os.O_RDWR)
        return __file
        # TODO: Test that the__file__ opened

    def write(self, command: [bytes, str], response=None):
        """write a string to the usbtmc device.
        
        Example:
        
        """
        if isinstance(command, str):
            command = command.encode()
        os.write(self.__file__, command)
        if response is not None:
            return self.read(self.response)

    def read(self, length=1024):
        return os.read(self.__file__, length).decode()

    def name(self):
        """# *IDN?
        Command Format:
            *IDN?
        Function Explanation:
            The command queries the ID character string of the instrument, including a field
            separated by 4 commas: manufactory, model, serial number and the version
            number composed of numbers and separated by “.” .
        Returned Format:
            RIGOL TECHNOLOGIES,<model>,<serial number>, <software version>.
        Example:
            RIGOL TECHNOLOGIES,DS1102E,DS1EB104702974,00.02.01.01.00
        """
        self.write("*IDN?")
        return self.read(300)

    def reset(self):
        """The command resets the system parameters."""
        warnings.warn(f"Resetting: {self}")
        self.write("*RST")

    @cached_property
    def __idn__(self):
        return self.name()

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
        return f"{self.__class__.__name__}<{self.dev_device}>"

    def __enter__(self):
        print("in __enter__")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("in __exit__")
