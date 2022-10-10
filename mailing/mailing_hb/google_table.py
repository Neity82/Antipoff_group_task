from typing import Dict, List

import gspread

from mailing.settings import GOOGLE_CONFIG, GOOGLE_EMPLOYEE_TABLE, GOOGLE_TEXT_TABLE


def get_employee() -> List[Dict[str, str]]:
    """
    Забираем данные о сотрудниках из googl таблицы
    :return: Список словарей
    """

    gc = gspread.service_account(filename=GOOGLE_CONFIG)
    sh = gc.open(GOOGLE_EMPLOYEE_TABLE)
    worksheet = sh.get_worksheet(0)

    return worksheet.get_all_records()


def get_text() -> List[str]:
    """
    Забираем данные с текстами поздравлений из googl таблицы
    :return: Список с поздравлениями
    """

    gc = gspread.service_account(filename=GOOGLE_CONFIG)
    sh = gc.open(GOOGLE_TEXT_TABLE)
    worksheet = sh.get_worksheet(0)

    return worksheet.col_values(1)
