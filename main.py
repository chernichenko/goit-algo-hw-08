import heapq

# Основне завдання: Мінімальні витрати на з'єднання кабелів
def min_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        combined = first + second
        total_cost += combined

        # Додаємо назад в купу
        heapq.heappush(cables, combined)

    return total_cost

# Необов'язкове завдання: Злиття k відсортованих списків
def merge_k_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list

if __name__ == "__main__":
    # Тестування основного завдання
    cables = [8, 4, 6, 12]
    min_cost = min_cost_to_connect_cables(cables)
    print("Мінімальні витрати на з'єднання кабелів:", min_cost)

    # Тестування необов'язкового завдання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
