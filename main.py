from collections import defaultdict
from typing import List, Dict, Tuple

class FrequencyAnalyzer:
    def __init__(self, data: List[int]) -> None:
        self.data: List[int] = data
        self.frequency_map: Dict[int, int] = defaultdict(int)

    def build_frequency_map(self) -> None:
        for item in self.data:
            self.frequency_map[item] += 1

    def get_most_frequent(self) -> Tuple[int, int]:
        if not self.frequency_map:
            self.build_frequency_map()

        max_count: int = -1
        max_element: int = None

        for element, count in self.frequency_map.items():
            if count > max_count:
                max_count = count
                max_element = element

        return max_element, max_count


if __name__ == "__main__":
    data = [1, 3, 2, 3, 4, 3, 5, 2, 2, 2]
    analyzer = FrequencyAnalyzer(data)
    element, count = analyzer.get_most_frequent()

    print(f"Most frequent element: {element}, Count: {count}")
