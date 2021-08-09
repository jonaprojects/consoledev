from typing import Any, AnyStr, Callable, List
from os import path


class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'
    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


def format_colored(text, color=""):
    return color + text + COLORS.CEND


def print_colored(text, color=""):
    print(format_colored(text, color))


class Text:
    def __init__(self, text: str, color: str):
        self.text = text
        self.color = color

    def __str__(self):
        return format_colored(self.text, self.color)


class TextArray:
    def __init__(self, text_objects):
        self.text_objects = []
        if isinstance(text_objects, str):
            self.text_objects.append(Text(text_objects, ""))
            return
        elif isinstance(text_objects, Text):
            self.text_objects.append(text_objects)
            return

        if isinstance(text_objects, tuple):
            text_objects = list(text_objects)
        if isinstance(text_objects, list):
            for text_object in text_objects:
                if isinstance(text_object, Text):
                    self.text_objects.append(text_object)
                elif isinstance(text_object, str):
                    self.text_objects.append(Text(text_object, ""))
        else:
            raise TypeError(f"TextArray.__init__(): Expected types list, tuple or str, but got {type(text_objects)}")

    def __iter__(self):
        self.__current_index = 0
        return self

    def __next__(self):
        if self.__current_index < len(self.text_objects):
            x = self.text_objects[self.__current_index]
            self.__current_index += 1
            return x
        else:
            raise StopIteration

    def __len__(self):
        return len(self.text_objects)

    def __str__(self):
        return "".join([text_object.__str__() for text_object in self.text_objects])


class JConsole:
    def __init__(self, analysis_function: Callable[[str], str] = None, header: Text = None,
                 starting_message=None, ending_message=None,
                 stop_commands: List[str] = ("exit()",)):
        self.analysis_function = analysis_function
        self.header = header
        self.starting_message = starting_message if isinstance(starting_message, TextArray) else TextArray(
            starting_message)
        self.ending_message = ending_message if isinstance(ending_message, TextArray) else TextArray(ending_message)
        self.stop_commands = stop_commands

    def run(self, save_work=True):
        """
        Running the console. The default console is a custom python-like basic console.
        Remark: In the default case:
            The code here can be unsafe due to the use of eval() and exec()
        :return:
        """
        print_colored(self.header.text, color=self.header.color)
        print(self.starting_message)
        current_line = 0
        code = []
        user_input = input(
            f"{format_colored('In', COLORS.CGREEN)} {format_colored(f'[{current_line}]', COLORS.OKGREEN)}: ")
        while user_input not in self.stop_commands:
            if self.analysis_function is None:
                try:
                    output = eval(user_input)  # POTENTIALLY DANGEROUS CODE
                    code.append(user_input)
                    print(output)
                except:  # UGLY CODE, I HAD NO CHOICE ...
                    try:
                        exec(user_input)  # POTENTIALLY DANGEROUS CODE
                        code.append(user_input)
                    except:  # UGLY CODE, I HAD NO CHOICE ...
                        print_colored("Error", COLORS.CRED)
            else:
                print(self.analysis_function(user_input))
                code.append(user_input)
            current_line += 1
            user_input = input(
                f"{format_colored('In', COLORS.CGREEN)} {format_colored(f'[{current_line}]', COLORS.OKGREEN)}: ")

        if save_work:
            answer = input(f'{format_colored("Do you wish to save your work? (Y/N)", COLORS.WARNING)}  ').upper()
            if answer == 'Y':
                file_path = input(f'{format_colored("File path:", COLORS.WARNING)} ')
                if path.exists(file_path):
                    proceed = input(
                        f'{format_colored(f"File already exists! Do you wish to override? (Y/N):", COLORS.WARNING)} ')
                else:
                    proceed = True
                if proceed:
                    with open(file_path, 'w') as code_file:
                        code_file.write("\n".join(code))
                    print(f"{format_colored('Saved!', COLORS.OKGREEN)}")
        if self.ending_message is not None:
            print(self.ending_message)  # Goes to the __str__() in class TextArray()


def main():
    header = Text("BASIC PYTHON CONSOLE V1.0 ", COLORS.WARNING)
    python_console = JConsole(header=header, starting_message="hello and welcome !", ending_message=" goodbye !")
    python_console.run()


if __name__ == '__main__':
    main()
