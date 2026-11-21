class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Sets default values of the Television with default off,
        unmuted, min volume, and min channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """
        Switches between on and off.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Switches between mute and unmute if the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted
    def channel_up(self):
        """
        Increases the television channel by one
        wrapping back to MIN_CHANNEL when reaches MAX_CHANNEL.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases the television channel by one
        wrapping back to MAX_CHANNEL when reaches MIN_CHANNEL.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Increases the television volume by one and unmutes
        stops at MAX_VOLUME.
        """
        if self.__status:
            self.__muted = False
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        """
        Decreases the television volume by one and unmutes
        stops at MIN_VOLUME.
        """
        if self.__status:
            self.__muted = False
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self):
        """
        Returns the value of the television status.
        """
        display_volume = 0 if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}'