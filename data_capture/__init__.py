import copy
import math

DEFAULT_ITEM = {
    "counter": 0,
    "lt": 0,
    "lte": 0,
    "gt": 0,
    "gte": 0,
}


class DataCapture:
    def __init__(self):
        self._total_items_stored = 0
        self._lower = math.inf
        self._higher = -math.inf
        self._data = {}

    def add(self, value: int):
        tmp_data = self._data.get(value, copy.deepcopy(DEFAULT_ITEM))
        tmp_data["counter"] += 1
        self._data[value] = tmp_data
        self._total_items_stored += 1
        if value < self._lower:
            self._lower = value
        elif value > self._higher:
            self._higher = value

    def build_stats(self):
        total = 0
        data = {}
        for value in range(self._lower, self._higher + 1):
            item = self._data.get(value, copy.deepcopy(DEFAULT_ITEM))
            item["lt"] = total
            item["lte"] = total + item["counter"]
            item["gt"] = self._total_items_stored - total - item["counter"]
            item["gte"] = self._total_items_stored - total
            total += item["counter"]
            data[value] = item

        return Stats(data, self._total_items_stored, self._lower, self._higher)


class Stats:
    def __init__(self, data, total_items, lower, higher):
        self._data = data
        self._total_items = total_items
        self._lower = lower
        self._higher = higher

    def get_stats_by_value(self, value: int):
        data = self._data.get(value, copy.deepcopy(DEFAULT_ITEM))
        if value < self._lower:
            data["gt"] = self._total_items
            data["gte"] = self._total_items
        elif value > self._higher:
            data["lt"] = 0
            data["lte"] = 0
        return data

    def less(self, value: int) -> int:
        """
        Get how many items we have below given number.
        If the current value was bellow or above we can return total_items or 0
        """
        if value < self._lower:
            return 0
        if value > self._higher:
            return self._total_items
        return self.get_stats_by_value(value)["lt"]

    def greater(self, value: int) -> int:
        """
        Get how many items we have above given number.
        If the current value was bellow or above we can return total_items or 0
        """
        if value < self._lower:
            return self._total_items
        if value > self._higher:
            return 0
        return self.get_stats_by_value(value)["gt"]

    def between(self, lower_value: int, greater_value: int) -> int:
        """Get the boundary items and calculate how many items we have between them"""
        if lower_value > greater_value:
            # Ensure that we had correct direction to calculate items between given interval
            lower_value, greater_value = greater_value, lower_value
        lower = self.get_stats_by_value(lower_value)
        greater = self.get_stats_by_value(greater_value)
        return abs(lower["gte"] - greater["gt"])
