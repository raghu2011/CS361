import re
import heapq
# Text Preprocessing
def preproccont(content):
    content=content.lower()
    content=re.sub(r'[^\w\s]', '', content)
    sentence_list=re.split(r'(?<=[.!?]) +', content)  # Split into sentences
    return [s.strip() for s in sentence_list if s.strip()]
# Levenshtein Distance Function
def levesh(string1, string2):
    if len(string1) < len(string2):
        return levesh(string2, string1)
    if len(string2) == 0:
        return len(string1)
    prev_row = range(len(string2) + 1)
    for index, char1 in enumerate(string1):
        curr_row = [index + 1]
        for j, char2 in enumerate(string2):
            insertcost = prev_row[j + 1] + 1
            deletecost = curr_row[j] + 1
            subcost = prev_row[j] + (char1 != char2)
            curr_row.append(min(insertcost, deletecost, subcost))
        prev_row = curr_row
    return prev_row[-1]
# A* Search Algorithm
def a_star_search(doca, docb):
    initial_state = (0, 0)
    target_state = (len(doca), len(docb))
    open_list = []
    heapq.heappush(open_list, (0, initial_state))
    parent_map = {}
    g_score_map = {initial_state: 0} 
    while open_list:
        current_f, currentstate = heapq.heappop(open_list)
        i, j = currentstate     
        if currentstate == target_state:
            return reconstruct_trace(parent_map, currentstate)
        # Align sentences
        if i < len(doca) and j < len(docb):
            cost = levesh(doca[i], docb[j])
            neighbor = (i + 1, j + 1)
            tentative_g_score =g_score_map[currentstate] + cost
            if neighbor not in g_score_map or tentative_g_score < g_score_map[neighbor]:
                parent_map[neighbor] = currentstate
                g_score_map[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(doca, docb, neighbor)
                heapq.heappush(open_list, (f_score, neighbor))
        # Skip sentences in document A
        if i < len(doca):
            neighbor = (i + 1, j)
            tentative_g_score= g_score_map[currentstate] + 1
            if neighbor not in g_score_map or tentative_g_score < g_score_map[neighbor]:
                parent_map[neighbor] = currentstate
                g_score_map[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(doca, docb, neighbor)
                heapq.heappush(open_list, (f_score, neighbor))
        # Skip sentences in document B
        if j < len(docb):
            neighbor = (i, j+ 1)
            tentative_g_score = g_score_map[currentstate] + 1
            if neighbor not in g_score_map or tentative_g_score < g_score_map[neighbor]:
                parent_map[neighbor] = currentstate
                g_score_map[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(doca, docb, neighbor)
                heapq.heappush(open_list, (f_score, neighbor))
    return None  # No path found
def heuristic(doca, docb, state):
    i, j = state
    return abs(len(doca) - i) +abs(len(docb) - j)
def reconstruct_trace(parent_map, current):
    path = [current]
    while current in parent_map:
        current = parent_map[current]
        path.append(current)
    return path[::-1]
# Function to read file content
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
# Plagiarism Detection
def detect_plagiarism(doca_path, docb_path):
    docatext = read_file(doca_path)
    docbtext = read_file(docb_path)
    if docatext is None or docbtext is None:
        return
    doca = preproccont(docatext)
    docb = preproccont(docbtext)
    alignment = a_star_search(doca, docb)
    if alignment is None:
        print("No alignment found.")
        return
    for i, j in alignment:
        if i < len(doca) and j < len(docb):
            distance = levesh(doca[i], docb[j])
            print(f"Edit Distance: {distance}")
# Test Cases
if __name__ == "__main__":
    # Replace with the paths to your document files
    doc1_path = "./test-1/doc1"
    doc2_path = "./test-1/doc1"
    print("Identical files:")
    detect_plagiarism(doc1_path, doc2_path)   
    print("")   
    test_2_doc_1 = "./test-2/doc1"
    test_2_doc_2 = "./test-2/doc2"
    print("Slightly modified document:")
    detect_plagiarism(test_2_doc_1, test_2_doc_2)  
    test_3_doc_1 = "./test-3/doc1"
    test_3_doc_2 = "./test-3/doc2"
    print("")  
    print("Completely Different Documents:")
    detect_plagiarism(test_3_doc_1, test_3_doc_2)
