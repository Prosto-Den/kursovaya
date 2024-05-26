from typing import Final

TITLEBAR_COLOUR: Final[int] = 0x00DE5462
BTN_COLOUR: Final[str] = '#AFF2FF'
HOVER_BTN_COLOUR: Final[str] = '#AAEAF7'
OPTION_BTN_COLOUR: Final[str] = '#C2FFCF'
HOVER_OPTION_BTN_COLOUR: Final[str] = '#BAF5C7'
BTN_TEXT_COLOUR: Final[str] = '#38A650'
DELETE_BTN_TEXT_COLOUR: Final[str] = '#D40000'

FONT: tuple = ('Candara', 20)
ENTRY_FONT: tuple = ('Candara', 14)

ADD_VALUES: Final[list[str]] = ['Книгу', 'Журнал', 'Газету', 'Читателя', 'Поставщика', 'Заказ']

MATERIALS_PICTURE_PATH: Final[str] = './pictures/materials/'

DATA_PATH: Final[str] = './temp/'

SELECT_ALL_MATERIALS_PATH: Final[str] = DATA_PATH + 'selectAllMaterials.json'

windows_flag: bool = False