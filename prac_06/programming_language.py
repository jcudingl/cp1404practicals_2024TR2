class ProgrammingLanguage:
    """Represent a language object."""

    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Initialise a ProgrammingLanguage instance.

        :param name: str. Programming Language name.
        :param typing: str. Typing of Programming Language.
        :param reflection: boolean. Programming Language is reflection or not.
        :param year: int. The year of Programming Language published.
        """
        self.name = name
        self.type = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string.

        :return: f'{self.name}, {self.type} Typing, Reflection={self.reflection}, First appeared in {self.year}'
        """
        return f"{self.name}, {self.type} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not."""
        return self.type == "Dynamic"
