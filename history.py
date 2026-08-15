import os
import pickle
from typing import List

from facts import facts


def save_fact_as_showed(chat_id: int, fact: str):
    history = _load_history(chat_id)
    history.append(fact)

    # checking if history contains all existing facts
    # in case facts are added or removed in the future
    if set(history).issuperset(facts):
        clear_chat_history(chat_id)
    else:
        _save_history(chat_id, history)


def check_fact_is_shown(chat_id: int, fact: str) -> bool:
    data = _load_history(chat_id)
    return fact in data


def clear_chat_history(chat_id: int):
    _save_history(chat_id, [])


def _load_history(chat_id: int) -> List[str]:
    file_path = _history_file_path(chat_id)
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "rb") as file_path:
            data = pickle.load(file_path)
    else:
        data = []
    return data


def _save_history(chat_id: int, data: List[str]):
    file_path = _history_file_path(chat_id)
    with open(file_path, "wb") as file:
        pickle.dump(data, file)


def _history_file_path(chat_id: int):
    return f"./history_data/{chat_id}.pkl"
