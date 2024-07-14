import numpy as np

def build_state_transition_matrix(data):
    unique_states = list(set(data))  # Tìm các trạng thái duy nhất
    num_states = len(unique_states)  # Số lượng trạng thái
    state_transition_counts = {state: {next_state: 0 for next_state in unique_states} for state in unique_states}

    # Tính toán số lần chuyển trạng thái
    for i in range(len(data) - 1):
        current_state = data[i]
        next_state = data[i+1]
        state_transition_counts[current_state][next_state] += 1

    # Tính toán xác suất chuyển trạng thái
    state_transition_probabilities = []
    for state in unique_states:
        state_transitions = state_transition_counts[state]
        total_transitions = sum(state_transitions.values())
        state_probabilities = [state_transitions[next_state] / total_transitions for next_state in unique_states]
        state_transition_probabilities.append(state_probabilities)

    # Xây dựng ma trận trạng thái P từ xác suất chuyển trạng thái
    P = np.array(state_transition_probabilities)

    return P, unique_states

def calculate_transition_probability(P, states, current_state, next_state):
    current_index = states.index(current_state)
    next_index = states.index(next_state)
    transition_probability = P[next_index, current_index]
    return transition_probability

# Dữ liệu lịch sử ăn uống buổi sáng
data = ['Banh my', 'Pho', 'Bun', 'Pizza', 'Banh my', 'Pho', 'Bun', 'Pizza', 'Pizza', 'Banh my', 'Banh my', 'Pho', 'Banh my', 'Pho', 'Banh my', 'Pho']

# Xây dựng ma trận trạng thái từ dữ liệu lịch sử
state_matrix, states = build_state_transition_matrix(data)
print("Ma trận trạng thái P:")
print(state_matrix)
print("Các trạng thái duy nhất:", states)

# Tính xác suất để hôm nay ăn 'Pho' biết hôm qua đã ăn 'Banh my'
current_state = 'Banh my'
next_state = 'Pho'
probability = calculate_transition_probability(state_matrix, states, current_state, next_state)
print(f"Xác suất để hôm nay ăn '{next_state}' biết hôm qua đã ăn '{current_state}': {probability}")
