def heappush(heap: list, data: int) -> None :
    # 힙 가장 마지막에 data를 집어넣는다.
    heap.append(data)
    current_index = len(heap) - 1
    # 그 데이터와 부모의 데이터를 비교해서 더 작다면 위로 올린다 (만약에 Max Heap이라면 더 크다면 위로 올린다.)
    # 이를 반복해서 heap 구조를 만족하게 만든다.
    while current_index > 0:
        parent_index = (current_index - 1) // 2
        if heap[parent_index] > heap[current_index]:
            heap[parent_index], heap[current_index] = heap[current_index], heap[parent_index]
            current_index = parent_index
        else:
            break

def heappop(heap: list) -> any:
    # heap이 비어 있다면 None을 return 시켜줌.
    if not heap:
        return None

    # heap의 가장 앞의 요소를 빼내고, 그 빈 자리를 가장 뒤의 요소로 채워줌
    heap[0], heap[-1] = heap[-1], heap[0]
    pop_data = heap.pop()  # 이제 pop_data는 제거된 최소값

    # 부모에서부터 시작해서 왼쪽 자식과 오른쪽 자식을 비교해서 더 작은 자식과 부모의 값을 바꿔줌
    # 이를 반복해서 heap의 구조를 만족할 때 까지 반복함.
    current_index = 0
    while True:
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2
        min_index = current_index

        if left_index < len(heap) and heap[left_index] < heap[min_index]:
            min_index = left_index

        if right_index < len(heap) and heap[right_index] < heap[min_index]:
            min_index = right_index

        # 최소 힙 조건을 만족하면 반복 중단
        if min_index == current_index:
            break

        # 부모와 더 작은 자식 교환
        heap[current_index], heap[min_index] = heap[min_index], heap[current_index]
        current_index = min_index

    return pop_data


def heapify(arr: list) -> None :
    pass


heap = []
x_items = [6, 5, 4, 3, 2, 1]
for x in x_items:
    heappush(heap, x)
    print(heap)
